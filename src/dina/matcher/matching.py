import json
import re
import numpy as np
from rapidfuzz.distance import Levenshtein
import polars as pl
from rapidfuzz import fuzz
from packaging.version import Version, InvalidVersion

class Matching:
    def __init__(self, freetext_fields: dict, ordered_fields: dict, other_fields: dict):
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
        if (csaf_version is None and asset_version is None) or (csaf_version == {} and asset_version == {}):
            return None
        
        if not csaf_version or not asset_version:
            return 0.0
        
        if isinstance(csaf_version, list):
            scores = np.array([], dtype=float)

            if isinstance(asset_version, list):
                for v1 in asset_version:
                    for v2 in csaf_version:
                        scores = np.append(scores, self._compare_versions(v1, v2))
            else:
                for v2 in csaf_version:
                    scores = np.append(scores, self._compare_versions(v2, asset_version))

            valid_scores = [s for s in scores if isinstance(s, (int, float)) and s is not None]

            return max(valid_scores) if valid_scores else None

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
        
        scores = np.array([], dtype=float)
        scores_weights = np.array([], dtype=float)

        for subfield in subfields.keys():
            scores_weights = np.append(scores_weights, subfields[subfield])

            if subfield == "min_max_version":
                csaf_ranges = csaf_version.get("min_max_version") or []
                asset_ranges = asset_version.get("min_max_version") or []

                csaf_ranges = [r for r in csaf_ranges if r.get("min") or r.get("max")]
                asset_ranges = [r for r in asset_ranges if r.get("min") or r.get("max")]

                if not csaf_ranges and not asset_ranges:
                    scores = np.append(scores, np.nan)
                    continue

                if not csaf_ranges or not asset_ranges:
                    scores = np.append(scores, 0.0)
                    continue

                valid = all(
                    any(self._range_in_range(a_range, c_range) for c_range in csaf_ranges)
                    for a_range in asset_ranges
                )
                if valid:
                    scores = np.append(scores, 1.0)
                else: 
                    scores = np.append(scores, 0.0)
                continue
            elif subfield == "qualifier":
                csaf_qualifier = csaf_version.get("qualifier") or []
                asset_qualifier = asset_version.get("qualifier") or []

                if not csaf_qualifier and not asset_qualifier:
                    scores = np.append(scores, np.nan)
                    continue

                if not csaf_qualifier or not asset_qualifier:
                    scores = np.append(scores, 0.0)
                    continue

                if len(csaf_qualifier) != len(asset_qualifier):
                    scores = np.append(scores, 0.0)
                    continue  

                part_scores = []

                for c, a in zip(csaf_qualifier, asset_qualifier):
                    ft_score = self._compare_freetext_with_order(str(c), str(a))
                    if ft_score is not None: 
                        part_scores.append(ft_score)

                if part_scores:
                    if sum(part_scores) == 0.0 or len(part_scores) == 0: 
                        scores = np.append(scores, np.nan)
                    else: 
                        scores = np.append(scores, sum(part_scores) / len(part_scores))
                    continue
            else:
                csaf_field = str(csaf_version.get(subfield) or "")
                asset_field = str(asset_version.get(subfield) or "")

                ft_score = self._compare_freetext_with_order(csaf_field, asset_field) 

                if ft_score is None: 
                    scores = np.append(scores, np.nan)
                else:
                    scores = np.append(scores, ft_score)

        weighted_sum = np.nansum(scores * scores_weights)
        weight_sum   = np.nansum(scores_weights[~np.isnan(scores)])
        normalized_score = weighted_sum / weight_sum if weight_sum > 0 else None

        return normalized_score
        
    def _compare_freetext_with_order(self, s1: str, s2: str) -> float:
        s1 = (s1 or "").strip().lower()
        s2 = (s2 or "").strip().lower()

        if not s1 and not s2:
            return None

        if not s1 or not s2:
            return 0.0
        
        # TODO: get separator from a separate file
        tokens1 = [t for t in s1.split(":")]
        tokens2 = [t for t in s2.split(":")]

        if not tokens1 or not tokens2:
            return 0.0

        shorter, longer = (tokens1, tokens2) if len(tokens1) <= len(tokens2) else (tokens2, tokens1)
        matched_scores = []

        for token in shorter:
            best = 0.0
            max_dist = 0

            if len(token) > 3:
                max_dist = max(1, len(token) // 3)
            
            for candidate in longer:
                dist = Levenshtein.distance(token, candidate)
                
                if dist <= max_dist:
                    score = fuzz.ratio(token, candidate) / 100.0
                    if score > best:
                        best = score
                    if best == 1.0:
                        break
            matched_scores.append(best)

        if not matched_scores:
            return 0.0

        return round(sum(matched_scores) / len(shorter), 4)
        
    def _compare_freetext(self, s1: str, s2: str) -> float:
        s1 = (s1 or "").strip().lower()
        s2 = (s2 or "").strip().lower()

        if not s1 and not s2:
            return None

        if not s1 or not s2:
            return 0.0

        tokens1 = [t for t in re.findall(r"\w+", s1)]
        tokens2 = [t for t in re.findall(r"\w+", s2)]

        if not tokens1 or not tokens2:
            return 0.0

        shorter, longer = (tokens1, tokens2) if len(tokens1) <= len(tokens2) else (tokens2, tokens1)
        matched_scores = []

        for token in shorter:
            best = 0.0
            max_dist = 0

            if len(token) > 3:
                max_dist = max(1, len(token) // 3)
            
            for candidate in longer:
                dist = Levenshtein.distance(token, candidate)
                
                if dist <= max_dist:
                    score = fuzz.ratio(token, candidate) / 100.0
                    if score > best:
                        best = score
                    if best == 1.0:
                        break
            matched_scores.append(best)

        if not matched_scores:
            return 0.0

        return round(sum(matched_scores) / len(shorter), 4)
    
    def _safe_load(self, val):
        if val == {}:
            return val
        
        if not val:
            return None
        
        try:
            return json.loads(val)
        except Exception:
            return None
        
    def _extract_field(self, data: str | dict, field: str) -> dict | str | None:
        if not data:
            return None
        
        if isinstance(data, dict):
            return data.get(field)
        
        if not isinstance(data, str):
            return None

        try:
            obj = json.loads(data)

            if obj == {}:
                return obj
            
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
            return None
              
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
            scores = np.array([], dtype=float)
            scores_weights = np.array([], dtype=float)

            for key in csaf_field.keys() & asset_field.keys():
                val1 = csaf_field[key]
                val2 = asset_field[key]
                cpe_weight = weight.get(key, 0.0)

                scores_weights = np.append(scores_weights, csaf_field[key])

                if val1 is None and val2 is None:
                    scores = np.append(scores, np.nan)
                    continue

                if key == "version" and isinstance(val1, dict) and isinstance(val2, dict):
                    similarity = self._compare_versions(val1, val2) * cpe_weight

                    if similarity is None: 
                        scores = np.append(scores, np.nan)
                    else:
                        scores = np.append(scores, similarity)
                    continue

                if isinstance(val1, (str, dict)) and isinstance(val2, (str, dict)):
                    similarity = self._compare_freetext_with_order(val1, val2) * cpe_weight

                    if similarity is None: 
                        scores = np.append(scores, np.nan)
                    else:
                        scores = np.append(scores, similarity)

            weighted_sum = np.nansum(scores * scores_weights)
            weight_sum   = np.nansum(scores_weights[~np.isnan(scores)])
            normalized_score = weighted_sum / weight_sum if weight_sum > 0 else None
            
            return normalized_score
                        
        return 0.0

    def df_matching(self, df_norm: pl.DataFrame) -> pl.DataFrame:
        # TODO: add csaf_cpe_norm and csaf_purl_norm in a separate file
        csaf_cpe_norm = "csaf_cpe_norm"
        csaf_purl_norm = "csaf_purl_norm"

        df_norm_csaf_purl_cpe = df_norm.select([csaf_cpe_norm, csaf_purl_norm])

        if self.freetext_fields and self.freetext_fields.keys():
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
                                    self._extract_field(row[csaf_cpe_norm], "vendor"),
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
                                    self._extract_field(row[csaf_cpe_norm], "product"),
                                    self._safe_load(row[asset_norm]),
                                ),
                                return_dtype=pl.Float64,
                            )
                            .alias(f"{field}_{csaf_cpe_norm}_match")
                        )

        if self.ordered_fields and self.ordered_fields.keys():
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
                                    self._extract_field(row[csaf_cpe_norm], field),
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
                                    self._extract_field(row[csaf_purl_norm], field),
                                    self._safe_load(row[asset_norm]),
                                ),
                                return_dtype=pl.Float64,
                            )
                            .alias(f"{field}_{csaf_purl_norm}_match")
                        )

                        # print(df_norm.select([csaf_purl_norm, asset_norm, f"{field}_{csaf_purl_norm}_match"]))

        if self.other_fields and self.other_fields.keys():
            for field in self.other_fields.keys():
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

                        df_norm = df_norm.with_columns(
                            pl.struct([csaf_norm, asset_norm])
                            .map_elements(
                                lambda row: self._compare_versions(
                                    self._extract_field(row[csaf_norm], "version"),
                                    self._extract_field(row[asset_norm], "version")
                                ),
                                return_dtype=pl.Float64,
                            )
                            .alias(f"asset_{csaf_cpe_norm}_match")
                        )
                        # print(df_norm.select([csaf_norm, asset_norm,f"asset_{csaf_cpe_norm}_match"]))
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

                        df_norm = df_norm.with_columns(
                            pl.struct([csaf_norm, asset_norm])
                            .map_elements(
                                lambda row: self._compare_versions(
                                    self._extract_field(row[csaf_norm], "version"),
                                    self._extract_field(row[asset_norm], "version")
                                ),
                                return_dtype=pl.Float64,
                            )
                            .alias(f"asset_{csaf_purl_norm}_match")
                        )

                        # print(df_norm.select([csaf_norm, asset_norm, f"asset_{csaf_purl_norm}_match"]))

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

#     # # print(matcher._extract_field(csaf_field, "version"))

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

#     # a = {'schema': 'freetext', 'raw': '7:sp2', 'package': None, 'release_prefix': None, 'release_number': None, 'release_branch': None, 'qualifier': None, 'build_number': None, 'architecture': None, 'date': None, 'epoch': None, 'min_max_version': [{'min': '7:sp2', 'max': '7:sp2'}]}
#     # c = {'schema': 'freetext', 'raw': 'all:versions:v5.7:sp1:hf1', 'package': None, 'release_prefix': None, 'release_number': None, 'release_branch': None, 'qualifier': None, 'build_number': None, 'architecture': None, 'date': None, 'epoch': None, 'min_max_version': [{'min': 'all:versions:v5:7:sp1:hf1', 'max': 'all:versions:v5:7:sp1:hf1'}]}
#     # print(matcher._compare_versions(c, a))

# if __name__ == "__main__":
#     main()
