from datetime import datetime
import re
import polars as pl
import enum
from packaging.version import Version
# from pathlib import Path
# import tomllib


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


class Normalizer:
    def __init__(self, config: dict):
        db = config.get("database", {})
        self.freetext_fields_separator = db.get("freetext_fields_separator", ":")

        version = config.get("version", {})
        self.version_weights = version.get("weights", {})

        cpe = config.get("cpe", {})
        self.cpe_weights = cpe.get("weights", {})

        purl = config.get("purl", {})
        self.purl_weights = purl.get("weights", {})

    # ============================================================
    # PUBLIC METHODS
    # ============================================================

    def parse_version(self, expr: str):
        if isinstance(expr, pl.Series) or isinstance(expr, list):
            expr_list = []

            if isinstance(expr, pl.Series):
                if expr.is_empty():
                    return expr_list
                expr = expr.to_list()

            if not expr or expr is None:
                return expr_list

            for e in expr:
                value = self.parse_version(e)

                if value:
                    expr_list.append(value)

            return expr_list

        if not expr or expr is None:
            return None

        expr = expr.lower()
        expr = re.sub(r"\s*\+\s*", "+", expr).strip()
        schema = self._detect_schema(expr)

        match schema:
            case Standards.VERS:
                result = self._parse_csaf(Standards.VERS, expr)
            case Standards.VLS:
                result = self._parse_csaf(Standards.VLS, expr)
            case Standards.CALVER:
                result = self._parse_calver(expr)
            case Standards.RPM:
                result = self._parse_rpm(expr)
            case Standards.SAP:
                result = self._parse_sap(expr)
            case Standards.PEP440:
                result = self._parse_pep440(expr)
            case Standards.ERICSSON_RELEASE_SCHEMA:
                result = self._parse_ericsson(expr)
            case Standards.SEMVER:
                result = self._parse_semver(expr)
            case Standards.WILDCARD:
                result = self._parse_csaf_wildcard(expr)
            case Standards.DEB:
                result = self._parse_deb(expr)
            case _:
                result = self._parse_version_freetext(expr)

        return result or None

    def parse_freetext(self, expr: str):
        if not expr or expr is None:
            return None

        separator = self.freetext_fields_separator
        expr = expr.lower()
        expr = re.sub(r"[^a-z0-9]+", separator, expr)
        expr = expr.strip(separator)
        expr = re.sub(r"\%s+" % re.escape(separator), separator, expr)

        return expr

    def parse_cpe(self, cpe: str) -> dict:
        d = self._base_cpe_dict(cpe)

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
            d["version"] = (
                self.parse_version(parts_raw[4]) if len(parts_raw) > 4 else {}
            )
            d["update"] = (
                parts_raw[5] if len(parts_raw) > 5 and parts_raw[5] != "" else None
            )
            d["edition"] = parts_raw[6] if len(parts_raw) > 6 else None

            fields_23 = [f for f in self.cpe_weights.keys() if f != "raw"]

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
            return None

        return d

    def parse_purl(self, purl: str) -> dict:
        d = self._base_purl_dict(purl)

        if not purl.startswith("pkg:"):
            return None

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
            d["version"] = self.parse_version(version) or {}

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

    def parse_files(self, files: list[dict]) -> list[dict]:
        results = []

        for file in files:
            name = file.get("name")
            hash_algorithm = file.get("hash_algorithm")
            file_hash = file.get("file_hash")

            name = self.parse_freetext(name) if name else None
            file_hash = self.parse_freetext(file_hash) if file_hash else None

            d = self._base_file_dict(name)
            d["hash_algorithm"] = hash_algorithm or None
            d["file_hash"] = file_hash or None

            results.append(d)

        return results

    # ============================================================
    # PRIVATE UTILITIES
    # ============================================================

    def _detect_schema(self, s: str) -> str:
        """
        Detect the version schema (standard) for a given version string.

        The method checks the input string `s` against a prioritized list of
        regular expression patterns, each representing a known versioning
        standard (e.g., PEP440, SEMVER, SAP, RPM, CALVER, etc.).

        The order of patterns is significant — certain schemas (like CALVER or
        SAP) must be checked before more generic ones (like SEMVER or WILDCARD)
        to ensure correct classification.

        Args:
            s (str): Input version string to analyze.

        Returns:
            str: The detected schema name from the `Standards` enum,
                or `Standards.FREETEXT` if no pattern matches.
        """

        if not s or s is None:
            return None

        patterns_in_order = [
            (Standards.VERS, r"^vers:[a-z0-9_\-]+/.+"),
            (
                Standards.VLS,
                r"^(<=|>=|<|>|==|!=)\s*v?[0-9][0-9A-Za-z:._+\-]*(\|.*|,.*)?$",
            ),
            # Standards.CALVER should stand before Standards.WILDCARD and Standards.SEMVER
            (Standards.CALVER, r"^([0-9]{2}|[0-9]{4})\.\d{2}(?:\.\d{1,2})?$"),
            # Standards.SEMVER should stand before Standards.PEP440
            (
                Standards.SEMVER,
                r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
                r"(?:-[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?"
                r"(?:\+[0-9A-Za-z.-]+(?:\.[0-9A-Za-z.-]+)*)?$",
            ),
            # Standards.RPM should stand before Standards.DEB
            (
                Standards.RPM,
                r"^[a-z0-9+._-]+(-\d+:)?[0-9][0-9A-Za-z._-]*-[0-9A-Za-z._-]+\.(src|[a-z0-9_]+)(?:\.rpm)?$",
            ),
            (
                Standards.SAP,
                r"^[vV]?\d+(?:[ ._+]+(?:sp\d+|r\d+|upd\d+|update\d+|hf\d+|patch\d+|build\d+|h\d+|lts\d+))+$",
            ),
            (
                Standards.ERICSSON_RELEASE_SCHEMA,
                r"^r[0-9]+[a-z](?:_(?:pc|sp|uc|mr)[0-9]+)?$",
            ),
            (
                Standards.PEP440,
                r"^(0|[1-9]\d*)(?:\.(0|[1-9]\d*))*"
                r"(?:(a|b|rc)(\d+))?"
                r"(?:\.post(\d+))?"
                r"(?:\.dev(\d+))?$",
            ),
            # Standards.WILDCARD should stand before Standards.DEB
            (
                Standards.WILDCARD,
                r"^(?:\d+|\+)(?:\.(?:\d+|\+))*$",
            ),
            (
                Standards.DEB,
                r"^(?:\d+:)?(0|[1-9]\d*)(\.(0|[1-9]\d*))*([A-Za-z.+:~\-]*)?(?:-[0-9A-Za-z.+:~]+)?$",
            ),
        ]

        for name, pat in patterns_in_order:
            if re.match(pat, s, re.IGNORECASE):
                return name

        return Standards.FREETEXT

    def _safe_version(self, val: str) -> str:
        """Return a normalized version string if valid, otherwise the original value."""
        try:
            return str(Version(val))
        except Exception:
            return val

    def _base_dict(self, schema, raw) -> dict:
        """Initialize a version dict from config fields, setting all values to None."""

        base = {"schema": schema, "raw": raw}

        for field in self.version_weights.keys():
            if field not in ("schema", "raw"):
                base[field] = None
        return base

    def _base_cpe_dict(self, raw) -> dict:
        base = {"raw": raw}

        for field in self.cpe_weights.keys():
            if field == "version":
                base[field] = {}
            elif field not in ("schema", "raw"):
                base[field] = None
        return base

    def _base_purl_dict(self, raw) -> dict:
        base = {"raw": raw}

        for field in self.purl_weights.keys():
            if field == "version" or field == "qualifiers":
                base[field] = {}
            elif field not in ("schema", "raw"):
                base[field] = None
        return base

    def _base_file_dict(self, name: str) -> dict:
        return {
            "name": name if name else None,
            "hash_algorithm": None,
            "file_hash": None,
        }

    # ============================================================
    # PRIVATE PARSER
    # ============================================================

    def _parse_csaf(self, schema, expr: str):
        """
        Parse CSAF-style version expressions into a structured version dictionary.
        Handles both `vers:` and comparison-based (`VLS`) schemas by extracting
        package information and version range constraints (min/max) from the input.
        Returns a normalized dictionary compatible with the internal version model.
        """

        if not expr or expr is None:
            return None

        parts = expr.split("/", 1)

        d = self._base_dict(
            Standards.VERS.value if schema == Standards.VERS else Standards.VLS.value,
            expr,
        )

        if schema == Standards.VERS:
            d["package"] = parts[0].replace("vers:", "") if len(parts) > 1 else None
            constraints = parts[1] if len(parts) > 1 else None
        else:
            constraints = expr

        results = []

        if constraints:
            for alt in constraints.split("|"):
                min_v, max_v = None, None
                for cond in alt.split(","):
                    cond = cond.strip()

                    op = None
                    for symbol in (">=", "<=", ">", "<", "="):
                        if cond.startswith(symbol):
                            op = symbol
                            cond = cond[len(symbol) :]
                            break

                    cond = cond.lstrip("v")
                    min_inclusive = True
                    max_inclusive = True

                    if cond in ("*", ""):
                        min_v, max_v = None, None
                    elif op == ">=":
                        min_v = self._safe_version(cond)
                    elif op == ">":
                        min_v = self._safe_version(cond)
                        min_inclusive = False
                    elif op == "<=":
                        max_v = self._safe_version(cond)
                    elif op == "<":
                        max_v = self._safe_version(cond)
                        max_inclusive = False
                    elif op == "=":
                        val = self._safe_version(cond)
                        min_v = max_v = val
                    else:
                        val = self._safe_version(cond)
                        min_v = max_v = val

                results.append(
                    {
                        "min": min_v,
                        "max": max_v,
                        "min_inclusive": min_inclusive,
                        "max_inclusive": max_inclusive,
                    }
                )

        d["min_max_version"] = results if results else None
        return d

    def _parse_calver(self, expr: str):
        m = re.match(r"^([0-9]{2}|[0-9]{4})\.(\d{2})(?:\.(\d{1,2}))?$", expr)

        if not m or m is None:
            return None

        year, month, day = m.groups()
        year = int(year)
        month = int(month)
        day = int(day) if day else None

        if year < 100:
            year += 2000

        d = self._base_dict(Standards.CALVER.value, expr)
        d["date"] = {"year": year, "month": month, "day": day}
        d["min_max_version"] = [{"min": expr, "max": expr}]

        return d

    def _parse_csaf_wildcard(self, expr: str):
        if not expr or expr is None:
            return None

        d = self._base_dict(Standards.WILDCARD.value, expr)
        parts = expr.split(".")

        min_parts = ["0" if p == "+" else p for p in parts]
        max_parts = ["9999" if p == "+" else p for p in parts]

        d["min_max_version"] = [
            {"min": ".".join(min_parts), "max": ".".join(max_parts)}
        ]

        return d

    def _parse_rpm(self, expr: str):
        if not expr or expr is None:
            return None

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
            d = self._base_dict(Standards.RPM.value, expr)
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
            d = self._base_dict(Standards.RPM.value, expr)
            d["epoch"] = g["epoch"]
            d["build_number"] = g["release"]
            d["min_max_version"] = [{"min": g["version"], "max": g["version"]}]
            return d

        return None

    def _parse_deb(self, expr: str):
        if ":" not in expr and "-" not in expr:
            return None

        m = re.match(r"^(?:(\d+):)?([0-9A-Za-z.+:~]+)(?:-([0-9A-Za-z+.~]+))?$", expr)

        if not m or m is None:
            return None

        epoch, upstream, revision = m.groups()

        d = self._base_dict(Standards.DEB.value, expr)
        d["build_number"] = revision
        d["epoch"] = epoch
        d["min_max_version"] = [{"min": upstream, "max": upstream}]

        return d

    def _parse_sap(self, expr: str):
        normalized = expr.lower().replace("+", "").replace(" ", "")

        m = re.match(r"v?(\d+)(?:[.+_]?(\d+))?(?:sp(\d+))?(?:upd(\d+))?", normalized)

        if not m or m is None:
            return None

        major, minor, sp, upd = m.groups()

        major = int(major) if major else 0
        minor = int(minor) if minor else 0
        sp = int(sp) if sp else 0
        upd = int(upd) if upd else 0

        d = self._base_dict(Standards.SAP.value, expr)
        d["release_prefix"] = "v"
        d["release_number"] = major
        d["release_branch"] = minor
        d["qualifier"] = ["sp", sp] if sp else [None, None]
        d["build_number"] = f"upd{upd}" if upd else None

        normalized_version = f"{major}.{minor}.{sp}.{upd}"
        d["min_max_version"] = [{"min": normalized_version, "max": normalized_version}]

        return d

    def _parse_semver(self, expr: str):
        if not expr:
            return None

        main = expr
        pre = None
        build = None

        if "+" in expr:
            main, build = expr.split("+", 1)
        if "-" in main:
            main, pre = main.split("-", 1)

        m = re.match(r"^(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)$", main)
        if not m:
            parts = main.split(".")
            while len(parts) < 3:
                parts.append("0")
            m = re.match(
                r"^(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)$", ".".join(parts)
            )

        major = int(m.group("major"))
        minor = int(m.group("minor"))
        patch = int(m.group("patch"))

        d = self._base_dict(Standards.SEMVER.value, expr)
        d["release_number"] = f"{major}.{minor}.{patch}"
        d["qualifier"] = None
        d["build_number"] = None
        d["date"] = None

        if pre:
            d["qualifier"] = pre

        if build:
            if re.match(r"^\d{14}$", build):  # YYYYMMDDHHMMSS
                try:
                    dt = datetime.strptime(build, "%Y%m%d%H%M%S")
                    d["date"] = dt.isoformat()
                except ValueError:
                    d["build_number"] = build
            else:
                d["build_number"] = build

        d["min_max_version"] = [
            {"min": f"{major}.{minor}.{patch}", "max": f"{major}.{minor}.{patch}"}
        ]

        return d

    def _parse_ericsson(self, expr: str):
        m = re.match(r"^r(\d+)([a-z])(?:_(pc|sp|uc|mr)(\d+))?$", expr.lower())

        if not m or m is None:
            return None

        rel, branch, qtype, qnum = m.groups()
        rel = int(rel)

        d = self._base_dict(Standards.ERICSSON_RELEASE_SCHEMA.value, expr)
        d["release_prefix"] = "r"
        d["release_number"] = rel
        d["release_branch"] = branch
        d["qualifier"] = [qtype.upper(), int(qnum)] if qtype and qnum else [None, None]

        norm = f"{rel}.{branch}.{qnum}" if qnum else f"{rel}.{branch}"

        d["min_max_version"] = [{"min": norm, "max": norm}]

        return d

    def _parse_pep440(self, expr: str):
        m = re.match(
            r"^([0-9]+(?:\.[0-9]+)*)"  # base
            r"(?:(a|b|rc)(\d+))?"  # prerelease
            r"(?:\.post(\d+))?"  # post-release
            r"(?:\.dev(\d+))?$",  # dev-release
            expr,
        )

        if not m or m is None:
            return None

        base, pre_tag, pre_num, post_num, dev_num = m.groups()

        d = self._base_dict(Standards.PEP440.value, expr)
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

    def _parse_version_freetext(self, expr: str):
        if not expr or expr is None:
            return None

        separator = self.freetext_fields_separator
        expr = expr.lower()
        expr = re.sub(r"[^a-z0-9.]+", separator, expr)
        expr = expr.strip(separator)

        d = self._base_dict(Standards.FREETEXT.value, expr)

        return d


# def main():
#     config_path = Path("./assets/plugin_configs/default/matching_config.toml")

#     if not config_path.exists():
#         raise FileNotFoundError(f"Config file not found: {config_path}")

#     with open(config_path, "rb") as f:
#         mc = tomllib.load(f)

#     normalizer = Normalizer(mc)

#     examples = [
#         # "<V4.2.5015",
#         # "grafana-0:5.2.4-6.el7rhgs.src",
#         # "22.1.4_2024-11-11_Hot_Fix",
#         # "< 3.12.0",
#         # "> 3.12.0",
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
#         # "7 sp2",
#         # "All versions < V5.7 SP1 HF1"
#         # "13",
#         # "<V3.0"
#         # "14 Sp1",
#         # "All versions < V5.7 SP1 HF1"
#         # "21.0.0.0",
#         # "1.0.0-0.3.7",
#         # "1.0.0-alpha",
#         # "1.0.0-alpha.1",
#         # "1.0.0-x.7.z.92",
#         # "1.0.0-x-y-z.-",
#         # "1.0.0+20130313144700",
#         # "1.0.0+21AF26D3--117B344092BD",
#         # "1.0.0-alpha+001",
#         # "1.0.0-beta+exp.sha.5114f85"
#     ]

#     for ex in examples:
#         ex = ex.lower()
#         ex = re.sub(r"\s*\+\s*", "+", ex).strip()
#         detect = normalizer._detect_schema(ex)

#         print(f"'{ex}': '{detect}'")
#         match detect:
#             case Standards.VERS:
#                 print(normalizer._parse_csaf(Standards.VERS, ex))
#             case Standards.VLS:
#                 print(normalizer._parse_csaf(Standards.VLS, ex))
#             case Standards.CALVER:
#                 print(normalizer._parse_calver(ex))
#             case Standards.RPM:
#                 print(normalizer._parse_rpm(ex))
#             case Standards.SAP:
#                 print(normalizer._parse_sap(ex))
#             case Standards.PEP440:
#                 print(normalizer._parse_pep440(ex))
#             case Standards.ERICSSON_RELEASE_SCHEMA:
#                 print(normalizer._parse_ericsson(ex))
#             case Standards.SEMVER:
#                 print(normalizer._parse_semver(ex))
#             case Standards.WILDCARD:
#                 print(normalizer._parse_csaf_wildcard(ex))
#             case Standards.DEB:
#                 print(normalizer._parse_deb(ex))
#             case _:
#                 print(normalizer.parse_freetext(ex))

#     # print(normalizer.parse_cpe("cpe:/a:redhat:rhel_eus:8.1::appstream"))
#     # print(normalizer.parse_cpe("cpe:/a:redhat:jboss_fuse:6.3"))
#     # print(normalizer.parse_cpe("cpe:2.3:a:versa-networks:versa_director:22.1.4:2024-11-11_Hot_Fix:*:*:*:*:*:*"))

#     # print(normalizer.parse_purl("pkg:npm/angular/animation@12.3.1"))
#     # print(normalizer.parse_purl("pkg:deb/debian/curl@7.50.3-1?arch=i386&distro=jessie"))
#     # print(normalizer.parse_purl("pkg:rpm/redhat/openssl"))
#     # print(normalizer.parse_purl("pkg:oci/multicluster-observability-rhel8-operator@sha256:94974d6bf61f1c71b46e270464caefb9c90b5006533a894cffada70f836ff19b?arch=s390x&repository_url=registry.redhat.io/rhacm2/multicluster-observability-rhel8-operator&tag=v2.6.1-1"))
#     # print(normalizer.parse_purl("pkg:rpm/redhat/servicemesh-proxy-wasm@2.1.3-1.el8?arch=noarch"))
#     # files = [
#     #     {"name": "mybinary-1.0.0-linux-x86_64.tar.gz", "hash_algorithm": "sha256", "file_hash": "abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890"},
#     #     {"name": "test-1.0.0-linux-x86_64.tar.gz", "hash_algorithm": "sha256", "file_hash": "94974d6bf61f1c71b46e270464caefb9c90b5006533a894cffada70f836ff19b?arch=s390x"},
#     # ]

#     # print(normalizer.parse_files(files))

#     # print(normalizer.parse_version(examples))

#     # textc = "Oracle Database 21c Express Edition"
#     # texta = "Oracle Database 21c Express Edition"

#     # print(normalizer.parse_freetext(texta))

# if __name__ == "__main__":
#     main()
