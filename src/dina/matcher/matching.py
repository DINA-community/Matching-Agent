import json

# from pathlib import Path
# import tomllib
import numpy as np
from rapidfuzz.distance import Levenshtein
import polars as pl
from packaging.version import Version, InvalidVersion


class Matching:
    def __init__(self, matching_config: dict):
        db = matching_config.get("database", {})
        self.freetext_fields = db.get("freetext_fields", {})
        self.ordered_fields = db.get("ordered_fields", {})
        self.other_fields = db.get("other_fields", {})
        self.freetext_fields_weights = db.get("freetext_fields_weights", {})

        version = matching_config.get("version", {})
        self.version_weights = version.get("weights", {})

        cpe = matching_config.get("cpe", {})
        self.csaf_cpe_field_name = cpe.get("csaf_cpe_field_name", "csaf_cpe")
        self.cpe_weights = cpe.get("weights", {})

        purl = matching_config.get("purl", {})
        self.csaf_purl_field_name = purl.get("csaf_purl_field_name", "csaf_purl")
        self.purl_weights = purl.get("weights", {})

        ngram = matching_config.get("ngram", {})
        self.ngram_weights = ngram.get("weights", {})

        levenshtein = matching_config.get("levenshtein", {})
        self.levenshtein_max_distance = levenshtein.get("max_distance", 0)

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

        if (asset_min is None and asset_max is None) and (
            csaf_min is None and csaf_max is None
        ):
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

    def _compare_versions(
        self, csaf_version: dict | list, asset_version: dict | list
    ) -> float:
        if (csaf_version is None and asset_version is None) or (
            csaf_version == {} and asset_version == {}
        ):
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
                    scores = np.append(
                        scores, self._compare_versions(v2, asset_version)
                    )

            valid_scores = [
                s for s in scores if isinstance(s, (int, float)) and s is not None
            ]

            return round(max(valid_scores), 4) if valid_scores else None

        if not isinstance(csaf_version, dict) or not isinstance(asset_version, dict):
            return 0.0

        subfields = self.version_weights

        scores = np.array([], dtype=float)
        scores_weights = np.array([], dtype=float)

        for subfield in subfields.keys():
            if not isinstance(subfields[subfield], float):
                continue

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
                    any(
                        self._range_in_range(a_range, c_range)
                        for c_range in csaf_ranges
                    )
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
                    ft_score = self._compare_freetext(
                        str(c), str(a), ignore_order=False
                    )
                    if ft_score is not None:
                        part_scores.append(ft_score)

                if part_scores:
                    if sum(part_scores) == 0.0 or len(part_scores) == 0:
                        scores = np.append(scores, np.nan)
                    else:
                        scores = np.append(scores, sum(part_scores) / len(part_scores))

                    continue

                scores = np.append(scores, np.nan)
            else:
                csaf_field = str(csaf_version.get(subfield) or "")
                asset_field = str(asset_version.get(subfield) or "")

                ft_score = self._compare_freetext(
                    csaf_field, asset_field, ignore_order=False
                )

                if ft_score is None:
                    scores = np.append(scores, np.nan)
                else:
                    scores = np.append(scores, ft_score)

        valid_scores = scores[~np.isnan(scores)]

        if valid_scores.size < 2:
            return 0.0

        weighted_sum = np.nansum(scores * scores_weights)
        weight_sum = np.nansum(scores_weights[~np.isnan(scores)])
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
            ":".join(clean_tokens[i : i + n]) for i in range(len(clean_tokens) - n + 1)
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

    def _compare_freetext(self, s1, s2, ignore_order=True):
        s1 = (s1 or "").strip().lower().replace("none", "")
        s2 = (s2 or "").strip().lower().replace("none", "")

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
                if dist <= self.levenshtein_max_distance:
                    similar_pairs += 1
                    score = 1 - (dist / max(len(t1), len(t2)))
                    best = max(best, score)
            token_scores.append(best)

        if similar_pairs == 0:
            return 0.0

        token_similarity = np.mean(token_scores) if token_scores else 0.0
        ngram_total = np.array([], dtype=float)
        total_w = np.array([], dtype=float)

        if self.ngram_weights:
            for n, w in self.ngram_weights.items():
                if not isinstance(n, int) and not isinstance(w, float):
                    continue

                ngram1 = self._ngrams_from_tokens(
                    tokens1, int(n), ignore_order=ignore_order
                )
                ngram2 = self._ngrams_from_tokens(
                    tokens2, int(n), ignore_order=ignore_order
                )

                sim = self._ngram_similarity(
                    ngram1, ngram2, max_distance=self.levenshtein_max_distance
                )

                if sim is None:
                    ngram_total = np.append(ngram_total, np.nan)
                else:
                    ngram_total = np.append(ngram_total, sim)
                total_w = np.append(total_w, w)

        ngram_weighted_sum = np.nansum(ngram_total * total_w)
        ngram_weight_sum = np.nansum(total_w[~np.isnan(ngram_total)])
        ngram_normalized_score = (
            ngram_weighted_sum / ngram_weight_sum if ngram_weight_sum > 0 else 0.0
        )

        overlap = len(set(tokens1) & set(tokens2)) / max(len(tokens1), len(tokens2))

        final_score = 0.0

        token_weight = self.freetext_fields_weights.get("token", 0)
        ngram_weight = self.freetext_fields_weights.get("ngram", 0)
        overlap_weight = self.freetext_fields_weights.get("overlap", 0)

        final_score = (
            token_weight * token_similarity
            + ngram_weight * ngram_normalized_score
            + overlap_weight * overlap
        )

        return round(final_score, 4)

    def _safe_load(self, val):
        if not val or val is None:
            return None

        if val == {}:
            return val

        try:
            val = json.loads(val)
            if val:
                return val
            else:
                return {}
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
                json.loads(x) != {}
                for x in df[col].to_list()
                if x not in (None, "null")
            )
        )

    def compare_fields(
        self,
        csaf_field: dict | str | list | None,
        asset_field: dict | str | list | None,
        weight: dict | None = None,
    ) -> float | None:
        """
        Compare two CSAF and asset fields using the most appropriate method
        based on their data type (string, list, dict).

        Returns:
            float | None: Similarity score between 0.0 and 1.0, or None if both fields are empty.
        """
        # --- Base cases ---
        if not csaf_field and not asset_field:
            return None
        if not csaf_field or not asset_field:
            return 0.0

        # --- Delegate based on type ---
        if isinstance(csaf_field, str) and isinstance(asset_field, str):
            return self._compare_string_fields(csaf_field, asset_field)

        if isinstance(csaf_field, list) and isinstance(asset_field, list):
            return self._compare_list_fields(csaf_field, asset_field)

        if isinstance(csaf_field, dict) and isinstance(asset_field, dict):
            return self._compare_dict_fields(csaf_field, asset_field, weight)

        return 0.0

    def _compare_string_fields(self, csaf_field: str, asset_field: str) -> float:
        """Compare two string fields using Levenshtein-based freetext comparison."""
        return (
            self._compare_freetext(csaf_field, asset_field, ignore_order=False) or 0.0
        )

    def _compare_list_fields(self, csaf_list: list, asset_list: list) -> float:
        """Compare lists of string values and return 1.0 if any overlap exists."""
        for asset in asset_list:
            for csaf in csaf_list:
                if isinstance(asset, str) and isinstance(csaf, str) and asset == csaf:
                    return 1.0
        return 0.0

    def _compare_dict_fields(
        self, csaf_dict: dict, asset_dict: dict, weight: dict | None = None
    ) -> float:
        """Compare dictionary-based fields using weighted subfield similarity."""
        if not weight:
            return 0.0

        scores, weights = [], []

        for key in csaf_dict.keys() & asset_dict.keys():
            val1, val2 = csaf_dict[key], asset_dict[key]
            w = weight.get(key, 0.0)
            weights.append(w)

            # Both None → neutral
            if val1 is None and val2 is None:
                scores.append(np.nan)
                continue

            # Special case: version
            if key == "version" and isinstance(val1, dict) and isinstance(val2, dict):
                sim = self._compare_versions(val1, val2)
                scores.append(sim if sim is not None else np.nan)
                continue

            # Freetext fallback
            if isinstance(val1, (str, dict)) and isinstance(val2, (str, dict)):
                sim = self._compare_freetext(val1, val2, ignore_order=False)
                scores.append(sim if sim is not None else np.nan)
                continue

            scores.append(np.nan)

        return self._weighted_mean(scores, weights)

    def _weighted_mean(self, scores: list[float], weights: list[float]) -> float:
        """Compute weighted mean, ignoring NaN values."""
        if not scores or not weights:
            return 0.0

        scores_arr, weights_arr = (
            np.array(scores, dtype=float),
            np.array(weights, dtype=float),
        )
        valid_mask = ~np.isnan(scores_arr)
        valid_scores = scores_arr[valid_mask]

        if valid_scores.size < 2:
            return 0.0

        weighted_sum = np.nansum(scores_arr * weights_arr)
        total_weight = np.nansum(weights_arr[valid_mask])

        if total_weight == 0:
            return 0.0

        return round(weighted_sum / total_weight, 4)

    def df_matching(self, df_norm: pl.DataFrame) -> pl.DataFrame:
        """
        Apply all configured field comparisons (freetext, version, other)
        to a normalized Polars DataFrame and return a DataFrame
        containing similarity scores for each field.
        """

        csaf_cpe = self.csaf_cpe_field_name
        csaf_purl = self.csaf_purl_field_name

        df_norm_csaf = df_norm.select([csaf_cpe, csaf_purl])

        df_norm = self._match_freetext_fields(df_norm, df_norm_csaf, csaf_cpe)
        df_norm = self._match_ordered_fields(df_norm, df_norm_csaf, csaf_cpe, csaf_purl)
        df_norm = self._match_other_fields(df_norm, csaf_cpe, csaf_purl)

        return df_norm

    def _match_freetext_fields(
        self, df: pl.DataFrame, df_csaf: pl.DataFrame, csaf_cpe: str
    ) -> pl.DataFrame:
        """Compare all configured freetext fields (e.g., name, manufacturer)."""
        for field in (self.freetext_fields or {}).keys():
            csaf_col, asset_col = f"csaf_{field}", f"asset_{field}"
            if csaf_col not in df or asset_col not in df:
                continue

            # Base freetext comparison
            df = df.with_columns(
                pl.struct([csaf_col, asset_col])
                .map_elements(
                    lambda row: self._compare_freetext(row[csaf_col], row[asset_col]),
                    return_dtype=pl.Float64,
                )
                .alias(f"{field}_match")
            )

            # Special handling for manufacturer and product (via CPE)
            if field in {"manufacturer_name", "name"} and self._has_valid_json(
                df_csaf, csaf_cpe
            ):
                key = "vendor" if field == "manufacturer_name" else "product"
                df = df.with_columns(
                    pl.struct([csaf_cpe, asset_col])
                    .map_elements(
                        lambda row: self._compare_freetext(
                            self._extract_field(row[csaf_cpe], key),
                            self._safe_load(row[asset_col]),
                        ),
                        return_dtype=pl.Float64,
                    )
                    .alias(f"{field}_{csaf_cpe}_match")
                )
        return df

    def _match_ordered_fields(
        self, df: pl.DataFrame, df_csaf: pl.DataFrame, csaf_cpe: str, csaf_purl: str
    ) -> pl.DataFrame:
        """Compare ordered fields such as version information."""
        for field in (self.ordered_fields or {}).keys():
            csaf_col, asset_col = f"csaf_{field}", f"asset_{field}"
            if csaf_col not in df or asset_col not in df:
                continue

            # Main comparison
            df = df.with_columns(
                pl.struct([csaf_col, asset_col])
                .map_elements(
                    lambda row: self._compare_versions(
                        self._safe_load(row[csaf_col]),
                        self._safe_load(row[asset_col]),
                    ),
                    return_dtype=pl.Float64,
                )
                .alias(f"{field}_match")
            )

            # Special handling for version from CSAF CPE/PURL
            if field == "version":
                for ref_field in [csaf_cpe, csaf_purl]:
                    if self._has_valid_json(df_csaf, ref_field):
                        df = df.with_columns(
                            pl.struct([ref_field, asset_col])
                            .map_elements(
                                lambda row: self._compare_versions(
                                    self._extract_field(row[ref_field], field),
                                    self._safe_load(row[asset_col]),
                                ),
                                return_dtype=pl.Float64,
                            )
                            .alias(f"{field}_{ref_field}_match")
                        )

        # pl.Config.set_fmt_str_lengths(2000)
        # print("test version: ", df.select([f"csaf_version", f"asset_version", f"version_match"]))
        # print("test name: ", df.select([f"csaf_name", f"asset_name", f"name_match"]))

        return df

    def _match_other_fields(
        self, df: pl.DataFrame, csaf_cpe: str, csaf_purl: str
    ) -> pl.DataFrame:
        """
        Compare structured fields such as CPE and PURL, including
        sub-version matching and weighted field comparisons.
        """
        for field in (self.other_fields or {}).keys():
            csaf_col, asset_col = f"csaf_{field}", f"asset_{field}"
            if csaf_col not in df or asset_col not in df:
                continue

            weight = None

            match field:
                case "cpe":
                    weight = self.cpe_weights
                    # Extra: compare version field inside CPE
                    df = df.with_columns(
                        pl.struct([csaf_col, asset_col])
                        .map_elements(
                            lambda row: self._compare_versions(
                                self._extract_field(row[csaf_col], "version"),
                                self._extract_field(row[asset_col], "version"),
                            ),
                            return_dtype=pl.Float64,
                        )
                        .alias(f"asset_{csaf_cpe}_match")
                    )

                case "purl":
                    weight = self.purl_weights
                    # Extra: compare version field inside PURL
                    df = df.with_columns(
                        pl.struct([csaf_col, asset_col])
                        .map_elements(
                            lambda row: self._compare_versions(
                                self._extract_field(row[csaf_col], "version"),
                                self._extract_field(row[asset_col], "version"),
                            ),
                            return_dtype=pl.Float64,
                        )
                        .alias(f"asset_{csaf_purl}_match")
                    )

            # Generic field-level comparison (final weighted score)
            df = df.with_columns(
                pl.struct([csaf_col, asset_col])
                .map_elements(
                    lambda row: self.compare_fields(
                        self._safe_load(row[csaf_col]),
                        self._safe_load(row[asset_col]),
                        weight,
                    ),
                    return_dtype=pl.Float64,
                )
                .alias(f"{field}_match")
            )

        return df


# def main():
#     config_path = Path("./assets/plugin_configs/default/matching_config.toml")

#     if not config_path.exists():
#         raise FileNotFoundError(f"Config file not found: {config_path}")

#     with open(config_path, "rb") as f:
#         mc = tomllib.load(f)

#     matcher = Matching(mc)
#     #
#     # asset_field = {'schema': 'pep-440', 'raw': '21.0.0.0', 'package': None, 'release_prefix': None, 'release_number': '21.0.0.0', 'release_branch': None, 'qualifier': [None, None], 'build_number': None, 'architecture': None, 'date': None, 'epoch': None, 'min_max_version': [{'min': '22.0.0.0', 'max': '22.0.0.0'}]}
#     # csaf_field = {'schema': 'pep-440', 'raw': '21.0.0.0', 'package': None, 'release_prefix': None, 'release_number': '21.0.0.0', 'release_branch': None, 'qualifier': [None, None], 'build_number': None, 'architecture': None, 'date': None, 'epoch': None, 'min_max_version': [{'min': None, 'max': '21.0.0.0'}]}
#     # print(matcher._extract_field(csaf_field, "min_max_version"))
#     # print(matcher._compare_versions(csaf_field, asset_field))
#     # print(matcher.compare_fields(
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
#     #     ))
#     #
#     # csaf_sbom_urls = ["https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/", "https://www.test.org"]
#     # asset_sbom_urls = ["https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/"]
#     # print(matcher.compare_fields(csaf_sbom_urls, asset_sbom_urls))
#     #
#     # csaf_product_type = "Device"
#     # asset_product_type = "Undefined"
#     # print(matcher.compare_fields(csaf_product_type, asset_product_type))
#     #
#     # csaf_version = {'schema': 'pep-440', 'raw': '1.15.0.0', 'package': None, 'release_prefix': None, 'release_number': '1.15.0.0', 'release_branch': None, 'qualifier': [None, None], 'build_number': None, 'architecture': None, 'date': None, 'epoch': None, 'min_max_version': [{'min': '1.15.0.0', 'max': '1.15.0.0'}]}
#     # asset_version1 = {'schema': 'pep-440', 'raw': '1.15.0.0', 'package': None, 'release_prefix': None, 'release_number': '1.15.0.0', 'release_branch': None, 'qualifier': [None, None], 'build_number': None, 'architecture': None, 'date': None, 'epoch': None, 'min_max_version': [{'min': '1.15.0.0', 'max': '1.15.0.0'}]}
#     # asset_version2 = {'schema': 'rpm-package-naming', 'raw': 'rubygem-activemodel-0:5.2.0-1.el7rhgs.src', 'package': 'rubygem-activemodel', 'release_prefix': None, 'release_number': None, 'release_branch': None, 'qualifier': None, 'build_number': '1.el7rhgs', 'architecture': 'src', 'date': None, 'epoch': '0', 'min_max_version': [{'min': '5.2.0', 'max': '5.2.0'}]}
#     # print(matcher._compare_versions(csaf_version, asset_version1))
#     #
#     # a = {'schema': 'windows-sap-schema', 'raw': 'v17 upd1', 'package': None, 'release_prefix': 'v', 'release_number': 17, 'release_branch': 0, 'qualifier': [None, None], 'build_number': 'upd1', 'architecture': None, 'date': None, 'epoch': None, 'min_max_version': [{'min': '17.0.0.1', 'max': '17.0.0.1'}]}
#     # c = {'schema': 'csaf-constraint-vls', 'raw': '<v5.7', 'package': None, 'release_prefix': None, 'release_number': None, 'release_branch': None, 'qualifier': None, 'build_number': None, 'architecture': None, 'date': None, 'epoch': None, 'min_max_version': [{'min': None, 'max': '5.7'}]}
#     # print(matcher._compare_versions(c, a))
#     #
#     # textc = "21.0.0.0".lower()
#     # texta = "21.0.0.0".lower()
#     # print(matcher._compare_freetext(textc, texta))

# if __name__ == "__main__":
#     main()
