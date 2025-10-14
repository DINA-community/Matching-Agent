import json
import numpy as np
from rapidfuzz.distance import Levenshtein
import polars as pl
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

        if csaf_min is None and csaf_max is None:
            return False

        if asset_min is None and asset_max is None:
            return False

        if asset_min is not None and csaf_min is not None and asset_min < csaf_min:
            return False

        if asset_max is not None and csaf_max is not None and asset_max > csaf_max:
            return False

        if asset_min is None and csaf_min is not None:
            if csaf_min > asset_max:
                return False

        if asset_max is None and csaf_max is not None:
            if csaf_max < asset_min:
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

            return round(max(valid_scores), 4) if valid_scores else None

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
                    ft_score = self._compare_freetext(str(c), str(a), ignore_order=False)
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

                ft_score = self._compare_freetext(csaf_field, asset_field, ignore_order=False) 

                if ft_score is None: 
                    scores = np.append(scores, np.nan)
                else:
                    scores = np.append(scores, ft_score)

        valid_scores = scores[~np.isnan(scores)]

        if valid_scores.size < 2:
            return 0.0

        weighted_sum = np.nansum(scores * scores_weights)
        weight_sum   = np.nansum(scores_weights[~np.isnan(scores)])
        normalized_score = weighted_sum / weight_sum if weight_sum > 0 else None

        return round(normalized_score, 4)

    def _ngrams_from_tokens(self, tokens, n, ignore_order=True):
        clean_tokens = [
            str(t).strip()
            for t in tokens
            if t not in (None, "", "none", "null", "nan")
            and str(t).strip().lower() not in ("none", "null", "nan")
        ]

        if not clean_tokens:
            return []

        if len(clean_tokens) < n:
            return [":".join(clean_tokens)]

        ngrams = [
            ":".join(clean_tokens[i:i + n])
            for i in range(len(clean_tokens) - n + 1)
        ]

        return sorted(ngrams) if ignore_order else ngrams


    def _ngram_similarity(self, tokens1, tokens2, max_distance=2):        
        if not tokens1 or not tokens2:
            return 0.0

        scores = []

        for t1 in tokens1:
            best = 0.0
            for t2 in tokens2:
                dist = Levenshtein.distance(t1, t2)
                if dist > max_distance:
                    continue 
                score = 1 - (dist / max(len(t1), len(t2)))
                best = max(best, score)
            scores.append(best)
        return np.mean(scores) if scores else 0.0


    def _compare_freetext(
        self, 
        s1,
        s2,
        weights={1: 0.2, 2: 0.3, 3: 0.5},
        global_weights={"token": 0.5, "ngram": 0.3, "overlap": 0.2},
        ignore_order=True,
        max_distance=2
    ):
        s1 = (s1 or "").strip().lower()
        s2 = (s2 or "").strip().lower()

        if not s1 and not s2:
            return None
        
        if not s1 or not s2:
            return 0.0

        tokens1 = [t for t in s1.split(":") if t]
        tokens2 = [t for t in s2.split(":") if t]

        if ignore_order:
            tokens1.sort()
            tokens2.sort()

        if not tokens1 or not tokens2:
            return 0.0

        token_scores = []
        similar_pairs = 0

        for t1 in tokens1:
            best = 0.0
            for t2 in tokens2:
                dist = Levenshtein.distance(t1, t2)
                if dist <= max_distance:
                    similar_pairs += 1
                    score = 1 - (dist / max(len(t1), len(t2)))
                    best = max(best, score)
            token_scores.append(best)

        if similar_pairs == 0:
            return 0.0

        token_similarity = np.mean(token_scores) if token_scores else 0.0

        ngram_total = np.array([], dtype=float)
        total_w = np.array([], dtype=float)
        for n, w in weights.items():
            ngram1 = self._ngrams_from_tokens(tokens1, n, ignore_order=ignore_order)
            ngram2 = self._ngrams_from_tokens(tokens2, n, ignore_order=ignore_order)

            sim = self._ngram_similarity(
                ngram1,
                ngram2,
                max_distance=max_distance
            )
            if sim is None: 
                ngram_total = np.append(ngram_total, np.nan)
            else:
                ngram_total = np.append(ngram_total, sim)
            total_w = np.append(total_w, w)
        
        ngram_weighted_sum = np.nansum(ngram_total * total_w)
        ngram_weight_sum   = np.nansum(total_w[~np.isnan(ngram_total)])
        ngram_normalized_score = ngram_weighted_sum / ngram_weight_sum if ngram_weight_sum > 0 else None

        overlap = len(set(tokens1) & set(tokens2)) / max(len(tokens1), len(tokens2))

        final_score = (
            global_weights["token"] * token_similarity +
            global_weights["ngram"] * ngram_normalized_score +
            global_weights["overlap"] * overlap
        )

        return round(final_score, 4)
    
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
            return self._compare_freetext(csaf_field, asset_field, ignore_order=False)
        
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

                if val1 is None and val2 is None:
                    scores_weights = np.append(scores_weights, cpe_weight)
                    scores = np.append(scores, np.nan)
                    continue

                if key == "version" and isinstance(val1, dict) and isinstance(val2, dict):
                    scores_weights = np.append(scores_weights, cpe_weight)
                    similarity = self._compare_versions(val1, val2)

                    if similarity is None: 
                        scores = np.append(scores, np.nan)
                    else:
                        scores = np.append(scores, similarity)
                    continue

                if isinstance(val1, (str, dict)) and isinstance(val2, (str, dict)):
                    scores_weights = np.append(scores_weights, cpe_weight)
                    similarity = self._compare_freetext(val1, val2, ignore_order=False)

                    if similarity is None: 
                        scores = np.append(scores, np.nan)
                    else:
                        scores = np.append(scores, similarity)
            
            valid_scores = scores[~np.isnan(scores)]

            if valid_scores.size < 2:
                return 0.0

            weighted_sum = np.nansum(scores * scores_weights)
            weight_sum   = np.nansum(scores_weights[~np.isnan(scores)])
            normalized_score = weighted_sum / weight_sum if weight_sum > 0 else None
            
            return round(normalized_score, 4)
                        
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

#     # asset_field = {'schema': 'pep-440', 'raw': '21.0.0.0', 'package': None, 'release_prefix': None, 'release_number': '21.0.0.0', 'release_branch': None, 'qualifier': [None, None], 'build_number': None, 'architecture': None, 'date': None, 'epoch': None, 'min_max_version': [{'min': '21.0.0.0', 'max': '21.0.0.0'}]}

#     # csaf_field = {'schema': 'pep-440', 'raw': '21.0.0.0', 'package': None, 'release_prefix': None, 'release_number': '21.0.0.0', 'release_branch': None, 'qualifier': [None, None], 'build_number': None, 'architecture': None, 'date': None, 'epoch': None, 'min_max_version': [{'min': '21.0.0.0', 'max': '21.0.0.0'}]}
#     # print(matcher._extract_field(csaf_field, "version"))
    
#     # score = matcher._compare_versions(csaf_field, asset_field)
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
#     #     }
#     #     )
#     # print(score)
#     # csaf_sbom_urls = ["https://www.free.org/news/python-switch-statement-switch-case-example/", "https://www.test.org"]
#     # asset_sbom_urls = ["https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/"]

#     # print(matcher.compare_fields(csaf_sbom_urls, asset_sbom_urls))

#     # csaf_product_type = "Device"
#     # asset_product_type = "Undefined"

#     # print(matcher.compare_fields(csaf_product_type, asset_product_type))

#     # csaf_version = {'schema': 'pep-440', 'raw': '1.15.0.0', 'package': None, 'release_prefix': None, 'release_number': '1.15.0.0', 'release_branch': None, 'qualifier': [None, None], 'build_number': None, 'architecture': None, 'date': None, 'epoch': None, 'min_max_version': [{'min': '1.15.0.0', 'max': '1.15.0.0'}]}
#     # asset_version1 = {'schema': 'pep-440', 'raw': '1.15.0.0', 'package': None, 'release_prefix': None, 'release_number': '1.15.0.0', 'release_branch': None, 'qualifier': [None, None], 'build_number': None, 'architecture': None, 'date': None, 'epoch': None, 'min_max_version': [{'min': '1.15.0.0', 'max': '1.15.0.0'}]}
#     # asset_version2 = {'schema': 'rpm-package-naming', 'raw': 'rubygem-activemodel-0:5.2.0-1.el7rhgs.src', 'package': 'rubygem-activemodel', 'release_prefix': None, 'release_number': None, 'release_branch': None, 'qualifier': None, 'build_number': '1.el7rhgs', 'architecture': 'src', 'date': None, 'epoch': '0', 'min_max_version': [{'min': '5.2.0', 'max': '5.2.0'}]}
#     # print(matcher._compare_versions(csaf_version, asset_version1))

#     # a = {'schema': 'windows-sap-schema', 'raw': 'v17 upd1', 'package': None, 'release_prefix': 'v', 'release_number': 17, 'release_branch': 0, 'qualifier': [None, None], 'build_number': 'upd1', 'architecture': None, 'date': None, 'epoch': None, 'min_max_version': [{'min': '17.0.0.1', 'max': '17.0.0.1'}]}
#     # c = {'schema': 'csaf-constraint-vls', 'raw': '<v5.7', 'package': None, 'release_prefix': None, 'release_number': None, 'release_branch': None, 'qualifier': None, 'build_number': None, 'architecture': None, 'date': None, 'epoch': None, 'min_max_version': [{'min': None, 'max': '5.7'}]}
#     # print(matcher._compare_versions(c, a))
    
#     # textc = "21.0.0.0".lower()
#     # texta = "21.0.0.0".lower()

#     # print(matcher._compare_freetext(textc, texta))

# if __name__ == "__main__":
#     main()
