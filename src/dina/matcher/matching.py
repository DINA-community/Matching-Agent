import json
import re
from rapidfuzz.distance import Levenshtein
import polars as pl
from rapidfuzz import fuzz
from packaging.version import Version, InvalidVersion

class Matching:
    def __init__(self, freetext_fields: list[str], ordered_fields: list[str], other_fields: list[str]):
        self.freetext_fields = freetext_fields
        self.ordered_fields = ordered_fields
        self.other_fields = other_fields

    def _safe_version(self, val: str):
        if not val:
            return None
        try:
            return Version(str(val))
        except InvalidVersion:
            return None

    def _range_in_range(self, asset_range, csaf_range):
        asset_min = self._safe_version(asset_range.get("min"))
        asset_max = self._safe_version(asset_range.get("max"))
        csaf_min = self._safe_version(csaf_range.get("min"))
        csaf_max = self._safe_version(csaf_range.get("max"))

        if (asset_min is None and asset_max is None) and (csaf_min is None and csaf_max is None):
            return True
        if asset_min is None and asset_max is None:
            return False
        if csaf_min is None and csaf_max is None:
            return False

        if asset_min and csaf_min and asset_min < csaf_min:
            return False
        if asset_max and csaf_max and asset_max > csaf_max:
            return False
        return True


    def _compare_versions(self, csaf_version: dict | list, asset_version: dict | list) -> float:
        if isinstance(csaf_version, list):
            score = 0.0
            if isinstance(asset_version, list):
                for v1 in asset_version:
                    for v2 in csaf_version:
                        score = max(score, self._compare_versions(v1, v2))
            else:
                for v2 in csaf_version:
                    score = max(score, self._compare_versions(v2, asset_version))

            return score

        if not isinstance(csaf_version, dict) or not isinstance(asset_version, dict):
            return 0.0
        
        # TODO: add version-subfields in a separate file
        subfields = {
            "raw": 0.05,
            "package": 0.15, 
            "release_prefix": 0.05, 
            "release_number": 0.10,
            "release_branch": 0.07, 
            "build_number": 0.05, 
            "qualifier": 0.02,
            "architecture": 0.07, 
            "date": 0.01, 
            "epoch": 0.03, 
            "min_max_version": 0.40
        }
        
        scores = 0.0

        for subfield in subfields.keys():
            if subfield == "min_max_version":
                csaf_ranges = csaf_version.get("min_max_version") or []
                asset_ranges = asset_version.get("min_max_version") or []

                csaf_ranges = [r for r in csaf_ranges if r.get("min") or r.get("max")]
                asset_ranges = [r for r in asset_ranges if r.get("min") or r.get("max")]

                if not csaf_ranges or not asset_ranges:
                    scores += 0.0
                    continue

                valid = all(
                    any(self._range_in_range(a_range, c_range) for c_range in csaf_ranges)
                    for a_range in asset_ranges
                )

                scores = round(scores + round(1.0 * subfields[subfield], 2), 2) if valid else scores + 0.0
                continue
            elif subfield == "qualifier":
                csaf_qualifier = csaf_version.get("qualifier") or []
                asset_qualifier = asset_version.get("qualifier") or []

                if not csaf_qualifier and not asset_qualifier:
                    scores = round(scores + subfields[subfield], 2)
                    continue

                if not csaf_qualifier or not asset_qualifier:
                    scores += 0.0
                    continue

                if len(csaf_qualifier) != len(asset_qualifier):
                    scores += 0.0
                    continue  

                part_scores = []

                for c, a in zip(csaf_qualifier, asset_qualifier):
                    ft_score = self._compare_freetext_with_order(str(c), str(a))
                    part_scores.append(round(ft_score * subfields[subfield], 2))

                if part_scores:
                    scores = round(scores + round(sum(part_scores) / len(part_scores), 2), 2)
                    continue
            else:
                csaf_field = str(csaf_version.get(subfield) or "")
                asset_field = str(asset_version.get(subfield) or "")

                ft_score = self._compare_freetext_with_order(csaf_field, asset_field)
                scores = round(scores + (round(ft_score * subfields[subfield], 2)), 2)

        return scores
        
    def _compare_freetext_with_order(self, s1: str, s2: str) -> float:
        s1 = (s1 or "").strip().lower()
        s2 = (s2 or "").strip().lower()

        if not s1 and not s2:
            return 1.0

        if not s1 or not s2:
            return 0.0
        
        # TODO: get separator from a separate file
        tokens1 = [t for t in s1.split(":") if len(t) >= 2]
        tokens2 = [t for t in s2.split(":") if len(t) >= 2]

        if not tokens1 or not tokens2:
            return 0.0
        
        # TODO: clarify whether token order should matter for matching
        best_score = 0.0
        for t1 in tokens1:
            for t2 in tokens2:
                score = 0.0
                dist = Levenshtein.distance(t1, t2)
                if dist <= 2:
                    score = fuzz.ratio(t1, t2) / 100.0
                best_score = max(best_score, score)

        return best_score
        
    def _compare_freetext(self, s1: str, s2: str) -> float:
        s1 = (s1 or "").strip().lower()
        s2 = (s2 or "").strip().lower()

        if not s1 and not s2:
            return 1.0

        if not s1 or not s2:
            return 0.0

        tokens1 = [t for t in re.findall(r"\w+", s1) if len(t) > 2]
        tokens2 = [t for t in re.findall(r"\w+", s2) if len(t) > 2]

        if not tokens1 or not tokens2:
            return 0.0

        scores = []
        for t1 in tokens1:
            best_score = 0
            for t2 in tokens2:
                dist = Levenshtein.distance(t1, t2)
                if dist <= 2:
                    score = fuzz.ratio(t1, t2) / 100.0
                else:
                    score = 0
                best_score = max(best_score, score)
            scores.append(best_score)

        return float(sum(scores) / len(scores))
    
    def _safe_load(self, val):
        if not val:
            return {}
        try:
            return json.loads(val)
        except Exception:
            return {}
        
    def _extract_field(self, data: str, field: str) -> dict | str | None:
        if not data or not isinstance(data, str):
            return None

        try:
            obj = json.loads(data)
        except json.JSONDecodeError:
            return None

        value = obj.get(field)
        if not value:
            return None

        if field == "version":
            if isinstance(value, dict):
                return value
            elif isinstance(value, str):
                try:
                    inner = json.loads(value)
                    return inner if isinstance(inner, dict) else {"raw": value}
                except json.JSONDecodeError:
                    return {"raw": value}
            else:
                return {"raw": str(value)}

        return value
    
    def _has_valid_json(self, df, col):
            return (
                df is not None
                and col in df.columns
                and not df[col].is_null().all()
                and any(
                    json.loads(x) != {} for x in df[col].to_list() if x not in (None, "null")
                )
            )
    
    def compare_fields(self, csaf_field: dict | str | None, asset_field: dict | str | None, weight: dict = None) -> float:
        if not csaf_field and not asset_field:
            return 1.0
              
        if not csaf_field or not asset_field:
            return 0.0

        if isinstance(csaf_field, str) and isinstance(asset_field, str):
            return self._compare_freetext_with_order(csaf_field, asset_field)
        
        if isinstance(csaf_field, list) and isinstance(asset_field, list):            
            for a_field in asset_field:
                for c_field in csaf_field:
                    if isinstance(a_field, str) and isinstance(c_field, str):
                        if c_field == a_field:
                            return 1.0

        if weight and isinstance(csaf_field, dict) and isinstance(asset_field, dict):
            matches = 0.0

            for key in csaf_field.keys() & asset_field.keys():
                val1 = csaf_field[key]
                val2 = asset_field[key]
                cpe_weight = weight.get(key, 0.0)

                if key == "version" and isinstance(val1, dict) and isinstance(val2, dict):
                    matches += self._compare_versions(val1, val2) * cpe_weight
                    continue

                if isinstance(val1, (str, dict)) and isinstance(val2, (str, dict)):
                    similarity = self._compare_freetext_with_order(val1, val2) * cpe_weight
                    matches += similarity
            
            return matches
                        
        return 0.0

    def df_matching(self, df_norm: pl.DataFrame) -> pl.DataFrame:
        csaf_cpe_norm = "csaf_cpe_norm"
        csaf_purl_norm = "csaf_purl_norm"

        df_norm_csaf_purl_cpe = df_norm.select([csaf_cpe_norm, csaf_purl_norm])

        for field in self.freetext_fields:
            csaf_norm, asset_norm = f"csaf_{field}_norm", f"asset_{field}_norm"

            if csaf_norm in df_norm and asset_norm in df_norm:
                df_norm = df_norm.with_columns(
                    pl.struct([csaf_norm, asset_norm])
                    .map_elements(
                        lambda row: self._compare_freetext(row[csaf_norm], row[asset_norm]),
                        return_dtype=pl.Float64,
                    )
                    .alias(f"{field}_match")
                )
                
                if field == "manufacturer_name" and self._has_valid_json(df_norm_csaf_purl_cpe, csaf_cpe_norm):
                    df_norm = df_norm.with_columns(
                        pl.struct([csaf_cpe_norm, asset_norm])
                        .map_elements(
                            lambda row: self._compare_freetext(
                                self._safe_load(self._extract_field(row[csaf_cpe_norm], "vendor")),
                                self._safe_load(row[asset_norm]),
                            ),
                            return_dtype=pl.Float64,
                        )
                        .alias(f"{field}_{csaf_cpe_norm}_match")
                    )
                if field == "name" and self._has_valid_json(df_norm_csaf_purl_cpe, csaf_cpe_norm):
                    df_norm = df_norm.with_columns(
                        pl.struct([csaf_cpe_norm, asset_norm])
                        .map_elements(
                            lambda row: self._compare_freetext(
                                self._safe_load(self._extract_field(row[csaf_cpe_norm], "product")),
                                self._safe_load(row[asset_norm]),
                            ),
                            return_dtype=pl.Float64,
                        )
                        .alias(f"{field}_{csaf_cpe_norm}_match")
                    )

        for field in self.ordered_fields:
            csaf_norm, asset_norm = f"csaf_{field}_norm", f"asset_{field}_norm"

            if csaf_norm in df_norm and asset_norm in df_norm:
                df_norm = df_norm.with_columns(
                    pl.struct([csaf_norm, asset_norm])
                    .map_elements(
                        lambda row: self._compare_versions(
                            self._safe_load(row[csaf_norm]),
                            self._safe_load(row[asset_norm]),
                        ),
                        return_dtype=pl.Float64,
                    )
                    .alias(f"{field}_match")
                )

                if field == "version" and self._has_valid_json(df_norm_csaf_purl_cpe, csaf_cpe_norm):
                    df_norm = df_norm.with_columns(
                        pl.struct([csaf_cpe_norm, asset_norm])
                        .map_elements(
                            lambda row: self._compare_versions(
                                self._safe_load(self._extract_field(row[csaf_cpe_norm], field)),
                                self._safe_load(row[asset_norm]),
                            ),
                            return_dtype=pl.Float64,
                        )
                        .alias(f"{field}_{csaf_cpe_norm}_match")
                    )

                if field == "version" and self._has_valid_json(df_norm_csaf_purl_cpe, csaf_purl_norm):
                    df_norm = df_norm.with_columns(
                        pl.struct([csaf_purl_norm, asset_norm])
                        .map_elements(
                            lambda row: self._compare_versions(
                                self._safe_load(self._extract_field(row[csaf_purl_norm], field)),
                                self._safe_load(row[asset_norm]),
                            ),
                            return_dtype=pl.Float64,
                        )
                        .alias(f"{field}_{csaf_purl_norm}_match")
                    )

                    # print(df_norm.select([csaf_purl_norm, asset_norm, f"{field}_{csaf_purl_norm}_match"]))

        for field in self.other_fields:
            csaf_norm, asset_norm = f"csaf_{field}_norm", f"asset_{field}_norm"

            weight = None

            # TODO: add weights in a separate file
            match field: 
                case "cpe": 
                    weight = {
                        "raw": 0.01,
                        "part": 0.05,
                        "vendor": 0.15,
                        "product": 0.35,
                        "version": 0.30,
                        "update": 0.05,
                        "edition": 0.02,
                        "language": 0.00,
                        "sw_edition": 0.02,
                        "target_sw": 0.02,
                        "target_hw": 0.02,
                        "other": 0.01,
                    }
                case "purl": 
                    weight = {
                        "raw": 0.02,
                        "type": 0.15,
                        "namespace": 0.10,
                        "name": 0.35,
                        "version": 0.30,
                        "qualifiers": 0.05,
                        "subpath": 0.03,
                    }

            if csaf_norm in df_norm and asset_norm in df_norm:
                df_norm = df_norm.with_columns(
                    pl.struct([csaf_norm, asset_norm])
                    .map_elements(
                        lambda row: self.compare_fields(
                            self._safe_load(row[csaf_norm]),
                            self._safe_load(row[asset_norm]),
                            weight
                        ),
                        return_dtype=pl.Float64,
                    )
                    .alias(f"{field}_match")
                )

                # print(df_norm.select([f"csaf_{field}_norm", f"asset_{field}_norm", f"{field}_match"]))

        return df_norm
    

# def main():
#     matcher = Matching([], [], [])

#     # csaf_field = {
#     #     "raw": "cpe:2.3:o:redhat:enterprise_linux:7:*:computenode:*:*:*:*:*:*",
#     #     "part": "o",
#     #     "vendor": "redhat",
#     #     "product": "enterprise_linux",
#     #     "version": {
#     #         "schema": "pep-440",
#     #         "raw": "7",
#     #         "release_number": "7",
#     #         "min_max_version": [{"min": "7", "max": "7"}],
#     #     },
#     #     "edition": "computenode",
#     # }

#     # asset_field = {
#     #     "raw": "cpe:2.3:o:redhat:enterprise_linux:6:*:workstation:*:*:*:*:*:*",
#     #     "part": "o",
#     #     "vendor": "redhat",
#     #     "product": "enterprise_linux",
#     #     "version": {
#     #         "schema": "pep-440",
#     #         "raw": "6",
#     #         "release_number": "6",
#     #         "min_max_version": [{"min": "6", "max": "6"}],
#     #     },
#     #     "edition": "workstation",
#     # }

#     # score = matcher.compare_fields(
#     #     csaf_field, 
#     #     asset_field, 
#     #     {
#     #         "raw": 0.01,
#     #         "part": 0.05,
#     #         "vendor": 0.15,
#     #         "product": 0.35,
#     #         "version": 0.30,
#     #         "update": 0.05,
#     #         "edition": 0.02,
#     #         "language": 0.00,
#     #         "sw_edition": 0.02,
#     #         "target_sw": 0.02,
#     #         "target_hw": 0.02,
#     #         "other": 0.01,
#     #     })
#     # print(score)
#     # csaf_sbom_urls = ["https://www.free.org/news/python-switch-statement-switch-case-example/", "https://www.test.org"]
#     # asset_sbom_urls = ["https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/"]

#     # score = matcher.compare_fields(csaf_sbom_urls, asset_sbom_urls)

#     # csaf_product_type = "Device"
#     # asset_product_type = "Undefined"

#     # score = matcher.compare_fields(csaf_product_type, asset_product_type)

#     # csaf_version = {'schema': 'pep-440', 'raw': '1.15.0.0', 'package': None, 'release_prefix': None, 'release_number': '1.15.0.0', 'release_branch': None, 'qualifier': [None, None], 'build_number': None, 'architecture': None, 'date': None, 'epoch': None, 'min_max_version': [{'min': '1.15.0.0', 'max': '1.15.0.0'}]}
#     # asset_version1 = {'schema': 'pep-440', 'raw': '1.15.0.0', 'package': None, 'release_prefix': None, 'release_number': '1.15.0.0', 'release_branch': None, 'qualifier': [None, None], 'build_number': None, 'architecture': None, 'date': None, 'epoch': None, 'min_max_version': [{'min': '1.15.0.0', 'max': '1.15.0.0'}]}
#     # asset_version2 = {'schema': 'rpm-package-naming', 'raw': 'rubygem-activemodel-0:5.2.0-1.el7rhgs.src', 'package': 'rubygem-activemodel', 'release_prefix': None, 'release_number': None, 'release_branch': None, 'qualifier': None, 'build_number': '1.el7rhgs', 'architecture': 'src', 'date': None, 'epoch': '0', 'min_max_version': [{'min': '5.2.0', 'max': '5.2.0'}]}
#     # print(matcher._compare_versions(csaf_version, asset_version1))

# if __name__ == "__main__":
#     main()
