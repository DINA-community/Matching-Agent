import json
import re
import polars as pl
import enum
from packaging.version import Version

class Standards(enum.Enum):
    VERS = "csaf-cpe-syntax-vers"
    VLS = "csaf-constraint-vls"
    WILDCARD = "csaf-wildcard-syntax"
    RPM = "rpm-package-naming"
    DEB = "debian-ubuntu-deb-package-policy"
    CALVER = "calendar-versioning-ubuntu"
    SAP = "windows-sap-schema"
    ERICSSON_RELEASE_SCHEMA = "ericsson-release-schema"
    PEP440 = "pep-440"
    SEMVER = "semantic-versioning"
    FREETEXT = "freetext"

def detect_schema(s: str) -> str:    
    patterns_in_order = [
        (Standards.VERS, r"^vers:[a-z0-9_\-]+/.+"),
        (Standards.VLS, r"^(<=|>=|<|>|==|!=)\s*v?[0-9][0-9A-Za-z:._+\-]*(\|.*|,.*)?$"),
        # Standards.CALVER should stand before Standards.WILDCARD and Standards.SEMVER
        (Standards.CALVER, r"^([0-9]{2}|[0-9]{4})\.\d{2}(?:\.\d{1,2})?$"),
        # Standards.RPM should stand before Standards.DEB
        (Standards.RPM, r"^[a-z0-9+._-]+(-\d+:)?[0-9][0-9A-Za-z._-]*-[0-9A-Za-z._-]+\.(src|[a-z0-9_]+)(?:\.rpm)?$"),
        (Standards.SAP, r"^v[0-9]+(\.[0-9]+)?([\s+]*sp[0-9]+)?([\s+]*upd[0-9]+)?$"),
        (Standards.ERICSSON_RELEASE_SCHEMA, r"^r[0-9]+[a-z](?:_(?:pc|sp|uc|mr)[0-9]+)?$"),
        # Standards.SEMVER should stand before Standards.PEP440
        (Standards.SEMVER, r"^(0|[1-9]\d*)\.(0|[1-9]\d*)(?:\.(0|[1-9]\d*))?$"),
        (Standards.PEP440, r"^(0|[1-9]\d*)(\.(0|[1-9]\d*))*((a|b|rc)([1-9]\d*))?(\.post([1-9]\d*))?(\.dev([1-9]\d*))?$"),
        # Standards.WILDCARD should stand before Standards.DEB
        (Standards.WILDCARD, r"^(?:\d+|\+)(?:\.(?:\d+|\+))*\+$|^(?:\+)(?:\.(?:\d+|\+))*$"),
        (Standards.DEB, r"^(?:\d+:)?(0|[1-9]\d*)(\.(0|[1-9]\d*))*([A-Za-z.+:~\-]*)?(?:-[0-9A-Za-z.+:~]+)?$")
    ]

    for name, pat in patterns_in_order:
        if re.match(pat, s, re.IGNORECASE):
            return name

    return Standards.FREETEXT

def _base_dict(schema, raw):
    return {
        "schema": schema,
        "raw": raw,
        "package": None,
        "release_prefix": None,
        "release_number": None,
        "release_branch": None,
        "qualifier": None,
        "build_number": None,
        "architecture": None,
        "date": None,
        "epoch": None,
        "min_max_version": None
    }

def parse_csaf(schema, expr: str):
    """Parser für CSAF / CPE-Syntax (vers:/vls-Form)."""
    parts = expr.split("/", 1)

    d = _base_dict(
        Standards.VERS.value if schema == Standards.VERS else Standards.VLS.value,
        expr
    )

    if schema == Standards.VERS:
        d["package"] = parts[0].replace("vers:", "") if len(parts) > 1 else None
        constraints = parts[1] if len(parts) > 1 else None
    else:
        constraints = expr

    results = []

    def safe_version(val: str) -> str:
        try:
            return str(Version(val))
        except Exception:
            return val

    if constraints:
        for alt in constraints.split("|"):
            min_v, max_v = None, None
            for cond in alt.split(","):
                cond = cond.strip()

                op = None
                for symbol in (">=", "<=", ">", "<", "="):
                    if cond.startswith(symbol):
                        op = symbol
                        cond = cond[len(symbol):]
                        break

                cond = cond.lstrip("v")

                if cond in ("*", ""):
                    min_v, max_v = None, None
                elif op == ">=":
                    min_v = safe_version(cond)
                elif op == ">":
                    min_v = safe_version(cond)
                elif op == "<=":
                    max_v = safe_version(cond)
                elif op == "<":
                    max_v = safe_version(cond)
                elif op == "=":
                    val = safe_version(cond)
                    min_v = max_v = val
                else:
                    val = safe_version(cond)
                    min_v = max_v = val

            results.append({"min": min_v, "max": max_v})

    d["min_max_version"] = results if results else None
    return d

def parse_calver(expr: str):
    m = re.match(r"^([0-9]{2}|[0-9]{4})\.(\d{2})(?:\.(\d{1,2}))?$", expr)

    if not m:
        return None

    year, month, day = m.groups()
    year = int(year)
    month = int(month)
    day = int(day) if day else None

    if year < 100:
        year += 2000

    d = _base_dict(Standards.CALVER.value, expr)
    d["date"] = {"year": year, "month": month, "day": day}
    d["min_max_version"] = [{"min": expr, "max": expr}]

    return d

def parse_csaf_wildcard(expr: str):
    d = _base_dict(Standards.WILDCARD.value, expr)
    parts = expr.split(".")
    
    min_parts = ["0" if p == "+" else p for p in parts]
    max_parts = ["9999" if p == "+" else p for p in parts]

    d["min_max_version"] = [{"min": ".".join(min_parts), "max": ".".join(max_parts)}]

    return d

def parse_rpm(expr: str):
    full = re.match(
        r"^(?P<name>[a-z0-9+._-]+)"
        r"-(?:(?P<epoch>\d+):)?"
        r"(?P<version>[0-9][0-9A-Za-z._-]*)"
        r"-(?P<release>[0-9A-Za-z._-]+)"
        r"\.(?P<arch>[a-z0-9_]+)"
        r"(?:\.rpm)?$",
        expr,
    )

    if full:
        g = full.groupdict()
        d = _base_dict(Standards.RPM.value, expr)
        d["package"] = g["name"]
        d["epoch"] = g["epoch"]
        d["architecture"] = g["arch"]
        d["build_number"] = g["release"]
        d["min_max_version"] = [{"min": g["version"], "max": g["version"]}]
        return d

    evr = re.match(
        r"^(?:(?P<epoch>\d+):)?"
        r"(?P<version>[0-9][0-9A-Za-z._-]*)"
        r"-(?P<release>[0-9A-Za-z.+~:_-]+)$",
        expr,
    )

    if evr:
        g = evr.groupdict()
        d = _base_dict(Standards.RPM.value, expr)
        d["epoch"] = g["epoch"]
        d["build_number"] = g["release"]
        d["min_max_version"] = [{"min": g["version"], "max": g["version"]}]
        return d

    return None


def parse_deb(expr: str):
    if ":" not in expr and "-" not in expr:
        return None
    
    m = re.match(r"^(?:(\d+):)?([0-9A-Za-z.+:~]+)(?:-([0-9A-Za-z+.~]+))?$", expr)

    if not m:
        return None
    
    epoch, upstream, revision = m.groups()

    d = _base_dict(Standards.DEB.value, expr)
    d["build_number"] = revision
    d["epoch"] = epoch
    d["min_max_version"] = [{"min": upstream, "max": upstream}]

    return d

def parse_sap(expr: str):
    normalized = expr.lower().replace("+", "").replace(" ", "")

    m = re.match(r"v(\d+)(?:\.(\d+))?(?:sp(\d+))?(?:upd(\d+))?", normalized)
    if not m:
        return None
    
    major, minor, sp, upd = m.groups()

    major = int(major) if major else 0
    minor = int(minor) if minor else 0
    sp = int(sp) if sp else 0
    upd = int(upd) if upd else 0

    d = _base_dict(Standards.SAP.value, expr)
    d["release_prefix"] = "v"
    d["release_number"] = major
    d["release_branch"] = minor
    d["qualifier"] = ["sp", sp] if sp else [None, None]
    d["build_number"] = f"upd{upd}" if upd else None

    normalized_version = f"{major}.{minor}.{sp}.{upd}"
    d["min_max_version"] = [{"min": normalized_version, "max": normalized_version}]

    return d

def parse_semver(expr: str):
    parts = expr.split(".")
    major, minor, patch = None, None, None

    if len(parts) > 0:
        if parts[0] == "+":
            major = 0
        elif parts[0].isdigit():
            major = int(parts[0])
        else:
            major = None

    if len(parts) > 1:
        if parts[1] == "+":
            minor = 9999
        elif parts[1].isdigit():
            minor = int(parts[1])
        else:
            minor = None

    if len(parts) > 2:
        if parts[2] == "+":
            patch = 9999
        elif parts[2].isdigit():
            patch = int(parts[2])
        else:
            patch = None

    d = _base_dict(Standards.SEMVER.value, expr)
    d["min_max_version"] = [{"min": f"{major or 0}.{minor or 0}.{patch or 0}", "max": f"{major or 9999}.{minor or 9999}.{patch or 9999}"}]

    return d

def parse_ericsson(expr: str):
    m = re.match(r"^r(\d+)([a-z])(?:_(pc|sp|uc|mr)(\d+))?$", expr.lower())

    if not m:
        return None
 
    rel, branch, qtype, qnum = m.groups()
    rel = int(rel)

    d = _base_dict(Standards.ERICSSON_RELEASE_SCHEMA.value, expr)
    d["release_prefix"] = "r"
    d["release_number"] = rel
    d["release_branch"] = branch
    d["qualifier"] = [qtype.upper(), int(qnum)] if qtype and qnum else [None, None]

    norm = f"{rel}.{branch}.{qnum}" if qnum else f"{rel}.{branch}"

    d["min_max_version"] = [{"min": norm, "max": norm}]

    return d

def parse_pep440(expr: str):
    m = re.match(
        r"^([0-9]+(?:\.[0-9]+)*)" # base
        r"(?:(a|b|rc)(\d+))?" # prerelease
        r"(?:\.post(\d+))?" # post-release
        r"(?:\.dev(\d+))?$", # dev-release
        expr
    )

    if not m:
        return None

    base, pre_tag, pre_num, post_num, dev_num = m.groups()

    d = _base_dict(Standards.PEP440.value, expr)
    d["release_number"] = base
    d["qualifier"] = [None, None]

    if pre_tag and pre_num:
        d["qualifier"] = [pre_tag, int(pre_num)]
    elif post_num:
        d["qualifier"] = ["post", int(post_num)]
    elif dev_num:
        d["qualifier"] = ["dev", int(dev_num)]

    d["min_max_version"] = [{"min": expr, "max": expr}]

    return d

def parse_version_freetext(expr: str):
    separator = "."
    expr = expr.lower()
    expr = re.sub(r"[^a-z0-9]+", separator, expr)
    expr = expr.strip(separator)

    d = _base_dict(Standards.FREETEXT.value, expr)
    d["min_max_version"] = [{"min": expr, "max": expr}]

    return d

def parse_version(expr: str):
    if isinstance(expr, pl.Series) or isinstance(expr, list):
        if isinstance(expr, pl.Series):
            if expr.is_empty():
                return {}
            expr = expr.to_list()

        if not expr:
            return {}

        expr_list = []

        for e in expr:
            expr_list.append(parse_version(e))

        return expr_list

    if expr is None:
        return {}       
    
    expr = expr.lower()
    expr = re.sub(r"\s*\+\s*", "+", expr).strip()
    schema = detect_schema(expr)

    match schema:
        case Standards.VERS:
            result = parse_csaf(Standards.VERS, expr)
        case Standards.VLS:
            result = parse_csaf(Standards.VLS, expr)
        case Standards.CALVER:
            result = parse_calver(expr)
        case Standards.RPM:
            result = parse_rpm(expr)
        case Standards.SAP:
            result = parse_sap(expr)
        case Standards.PEP440:
            result = parse_pep440(expr)
        case Standards.ERICSSON_RELEASE_SCHEMA:
            result = parse_ericsson(expr)
        case Standards.SEMVER:
            result = parse_semver(expr)
        case Standards.WILDCARD:
            result = parse_csaf_wildcard(expr)
        case Standards.DEB:
            result = parse_deb(expr)
        case _:
            result = parse_version_freetext(expr)

    return result or {}

def parse_freetext(expr: str):
    # TODO: add separator in a separate file
    separator = ":"
    expr = expr.lower()
    expr = re.sub(r"[^a-z0-9]+", separator, expr)
    expr = expr.strip(separator)
    expr = re.sub(r"\%s+" % re.escape(separator), separator, expr)

    return expr

# TODO: add cpe_dict in a separate file
def _base_cpe_dict(raw: str) -> dict:
    return {
        "raw": raw,
        "part": None,
        "vendor": None,
        "product": None,
        "version": {},
        "update": None,
        "edition": None,
        "language": None,
        "sw_edition": None,
        "target_sw": None,
        "target_hw": None,
        "other": None,
    }

def parse_cpe(cpe: str) -> dict:
    d = _base_cpe_dict(cpe)

    if cpe.startswith("cpe:2.3:"):
        parts = cpe.split(":")[2:]
        fields = list(d.keys())[1:]
        for i, field in enumerate(fields):
            if i < len(parts):
                d[field] = parts[i] if parts[i] else None

        d["raw"] = "cpe:2.3:" + ":".join(d.get(f, "*") or "*" for f in fields)

    elif cpe.startswith("cpe:/"):
        parts_raw = cpe.split(":")
        d["part"] = parts_raw[1][1:] if len(parts_raw) > 1 else None
        d["vendor"] = parts_raw[2] if len(parts_raw) > 2 else None
        d["product"] = parts_raw[3] if len(parts_raw) > 3 else None
        d["version"] = parse_version(parts_raw[4]) if len(parts_raw) > 4 else {}
        d["update"] = parts_raw[5] if len(parts_raw) > 5 and parts_raw[5] != "" else None
        d["edition"] = parts_raw[6] if len(parts_raw) > 6 else None
        fields_23 = [
            "part", "vendor", "product", "version", "update", "edition",
            "language", "sw_edition", "target_sw", "target_hw", "other",
        ]

        raw_parts = []

        for f in fields_23:
            val = d.get(f, "*")

            if isinstance(val, dict):
                val = val.get("raw", "*")

            if not isinstance(val, str) or not val:
                val = "*"

            raw_parts.append(val)

        d["raw"] = f"cpe:2.3:{':'.join(raw_parts)}"

    else:
         return {}

    return d

# TODO: add purl_dict in a separate file
def _base_purl_dict(raw: str) -> dict:
    return {
        "raw": raw,
        "type": None,
        "namespace": None,
        "name": None,
        "version": {},
        "qualifiers": {},
        "subpath": None,
    }

def parse_purl(purl: str) -> dict:
    d = _base_purl_dict(purl)

    if not purl.startswith("pkg:"):
         return {}

    purl_body = purl[4:]

    if "#" in purl_body:
        purl_body, subpath = purl_body.split("#", 1)
        d["subpath"] = subpath or None

    if "?" in purl_body:
        purl_body, qualifiers_str = purl_body.split("?", 1)
        qualifiers = {}
        for q in qualifiers_str.split("&"):
            if "=" in q:
                k, v = q.split("=", 1)
                qualifiers[k] = v
            else:
                qualifiers[q] = None
        d["qualifiers"] = qualifiers

    version = None
    if "@" in purl_body:
        purl_body, version = purl_body.split("@", 1)
        d["version"] = parse_version(version) or {}

    parts = purl_body.split("/")
    d["type"] = parts[0] if len(parts) > 0 else None

    if len(parts) == 2:
        d["name"] = parts[1] or None
    elif len(parts) >= 3:
        d["namespace"] = "/".join(parts[1:-1]) or None
        d["name"] = parts[-1] or None
    else:
        d["name"] = None

    for key in ("type", "namespace", "name", "subpath"):
        if d[key] in (None, ""):
            d[key] = None

    if not d["qualifiers"]:
        d["qualifiers"] = {}

    return d

# TODO: add file_dict in a separate file
def _base_file_dict(name: str) -> dict:
    return {
        "name": name if name else None,
        "hash_algorithm": None,
        "file_hash": None
    }

def parse_files(files: list[dict]) -> list[dict]:
    results = []

    for file in files:
        name = file.get("name")
        hash_algorithm = file.get("hash_algorithm")
        file_hash = file.get("file_hash")

        name = parse_freetext(name) if name else None
        file_hash = parse_freetext(file_hash) if file_hash else None

        d = _base_file_dict(name)
        d["hash_algorithm"] = hash_algorithm or None
        d["file_hash"] = file_hash or None

        results.append(d)

    return results

class Normalizer:
    def __init__(self, freetext_fields: list[str], ordered_fields: list[str], other_fields: list[str]):
        self.freetext_fields = freetext_fields
        self.ordered_fields = ordered_fields
        self.other_fields = other_fields

    def apply(self, df: pl.DataFrame) -> pl.DataFrame:
        updates = []

        for col in self.freetext_fields:
            for prefix in ("csaf_", "asset_"):
                full_col = f"{prefix}{col}"

                if full_col in df.columns:
                    expr = pl.col(full_col)
                    expr = expr.map_elements(lambda x: json.dumps(parse_freetext(x)), return_dtype=pl.Utf8)
                    expr = expr.alias(f"{full_col}_norm")
                    updates.append(expr)

        for col in self.ordered_fields:
            for prefix in ("csaf_", "asset_"):
                full_col = f"{prefix}{col}"

                if full_col in df.columns:
                    expr = pl.col(full_col).map_elements(lambda x: json.dumps(parse_version(x)), return_dtype=pl.Utf8)
                    expr = expr.alias(f"{full_col}_norm")
                    updates.append(expr)

        for col in self.other_fields:
            for prefix in ("csaf_", "asset_"):
                full_col = f"{prefix}{col}"

                if full_col in df.columns:
                    parsers = {
                        "cpe": parse_cpe,
                        "purl": parse_purl,
                        "files": parse_files,
                    }

                    if col in parsers:
                        parser = parsers[col]

                        if parser:
                            expr = (
                                pl.col(full_col)
                                .map_elements(lambda x, parser=parser: json.dumps(parser(x)), return_dtype=pl.Utf8)
                                .alias(f"{full_col}_norm")
                            )
                    else: 
                        expr = pl.col(full_col).alias(f"{full_col}_norm")

                    updates.append(expr)


        # ---- for tests   
        # if updates:
        #     df = df.with_columns(updates)

        # full_col = f"{"csaf_"}{col}"
        # print(df.select([full_col, f"{full_col}_norm"]))

        # return df
        # -----

        return df.with_columns(updates)

# def main():
#     examples = [
#         # "<V4.2.5015",
#         # "grafana-0:5.2.4-6.el7rhgs.src",
#         # "22.1.4_2024-11-11_Hot_Fix",
#         # ">= 3.12.0",
#         # "vers:all/*",
#         # "vers:all/<V3.1.2.1",
#         # "<=3.4.2.2.6",
#         # "0.81",
#         # "R15B_PC4",
#         # "22.04",
#         # "V6 + SP9 + Upd2",
#         # "6.+.9.+.2",
#         # "1.0.post1",
#         # "1.0a1",
#         # "1:2.31.1-0ubuntu9.9",
#         # ">=0.68|<=0.80",
#         # "vers:pypi/>=1.0,<2.0|>=2.0",
#         # "vers:pypi/>=1.0|<2.0",
#         # "vers:pypi/1.5",
#         # "5.1.106.0",
#         # "1.3.4",
#         # "R15B",
#         # "R15B_PC4",
#         # "R17A_SP3",
#         # "2024.11.11",
#         # "nginx-1:1.18.0-1.amd64.rpm",
#         # "v4.2sp3",
#         # "R18C_MR2",
#         # "0.81.0",
#         # "2.1.0rc2",
#         # "1.0.dev2",
#         # "6.+.9",
#         # "+.1",
#         # "2.31.1-1",
#         # "random-string",
#     ]

#     for ex in examples:
#         ex = ex.lower()
#         ex = re.sub(r"\s*\+\s*", "+", ex).strip()
#         detect = detect_schema(ex)

#         print(f"'{ex}': '{detect}'")
#         match detect:
#             case Standards.VERS: 
#                 print(parse_csaf(Standards.VERS, ex))
#             case Standards.VLS:
#                 print(parse_csaf(Standards.VLS, ex))
#             case Standards.CALVER: 
#                 print(parse_calver(ex))
#             case Standards.RPM: 
#                 print(parse_rpm(ex))
#             case Standards.SAP: 
#                 print(parse_sap(ex))
#             case Standards.PEP440: 
#                 print(parse_pep440(ex))
#             case Standards.ERICSSON_RELEASE_SCHEMA:
#                 print(parse_ericsson(ex))
#             case Standards.SEMVER:
#                 print(parse_semver(ex))
#             case Standards.WILDCARD:
#                 print(parse_csaf_wildcard(ex))
#             case Standards.DEB: 
#                 print(parse_deb(ex))
#             case _:
#                 print(parse_freetext(ex))

#     # print(parse_cpe("cpe:/a:redhat:rhel_eus:8.1::appstream"))
#     # print(parse_cpe("cpe:/a:redhat:jboss_fuse:6.3"))
#     # print(parse_cpe("cpe:2.3:a:versa-networks:versa_director:22.1.4:2024-11-11_Hot_Fix:*:*:*:*:*:*"))

#     # print(parse_purl("pkg:npm/angular/animation@12.3.1"))
#     # print(parse_purl("pkg:deb/debian/curl@7.50.3-1?arch=i386&distro=jessie"))
#     # print(parse_purl("pkg:rpm/redhat/openssl"))
#     # print(parse_purl("pkg:oci/multicluster-observability-rhel8-operator@sha256:94974d6bf61f1c71b46e270464caefb9c90b5006533a894cffada70f836ff19b?arch=s390x&repository_url=registry.redhat.io/rhacm2/multicluster-observability-rhel8-operator&tag=v2.6.1-1"))
#     # print(parse_purl("pkg:rpm/redhat/servicemesh-proxy-wasm@2.1.3-1.el8?arch=noarch"))
#     # files = [
#     #     {"name": "mybinary-1.0.0-linux-x86_64.tar.gz", "hash_algorithm": "sha256", "file_hash": "abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890"},
#     #     {"name": "test-1.0.0-linux-x86_64.tar.gz", "hash_algorithm": "sha256", "file_hash": "94974d6bf61f1c71b46e270464caefb9c90b5006533a894cffada70f836ff19b?arch=s390x"},
#     # ]

#     # print(parse_files(files))

#     print(parse_version(examples))

# if __name__ == "__main__":
#     main()
