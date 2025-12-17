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
        self.freetext_fields_separator = db.get("freetext_fields_separator", ":")
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

    # ============================================================
    # PUBLIC METHODS
    # ============================================================

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

    # ============================================================
    # PRIVATE UTILITIES
    # ============================================================

    def _safe_load(self, val):
        if not val or val is None or val == {}:
            return None

        if isinstance(val, dict):
            return val

        try:
            val = json.loads(val)
            if val:
                return val
            else:
                return {}
        except Exception:
            return None

    def _extract_field(self, data: str | dict | None, field: str) -> dict | str | None:
        """
        Extract a specific field from a JSON-like string or dictionary.
        Handles both JSON strings and already-parsed dicts.
        Special case: when field == "version", always returns a dict.

        Args:
            data (str | dict | None): Input data, possibly JSON encoded.
            field (str): Field name to extract.

        Returns:
            dict | str | None: Extracted field value or None if missing/invalid.
        """
        if not data:
            return None

        # --- Already a dict ---
        if isinstance(data, dict):
            value = data.get(field)
        # --- JSON string ---
        elif isinstance(data, str):
            try:
                obj = json.loads(data)
            except json.JSONDecodeError:
                return None
            if not isinstance(obj, dict) or obj == {}:
                return None
            value = obj.get(field)
        # --- Invalid type ---
        else:
            return None

        if value is None or value == "":
            return None

        # --- Special handling for "version" fields ---
        if field == "version":
            if isinstance(value, dict):
                return value
            if isinstance(value, str):
                try:
                    parsed = json.loads(value)
                    return parsed if isinstance(parsed, dict) else {"raw": value}
                except json.JSONDecodeError:
                    return {"raw": value}
            return {"raw": str(value)}

        return value

    def _has_valid_json(self, df, col: str) -> bool:
        """
        Check if the given DataFrame column contains at least one valid non-empty JSON object.
        """
        if df is None or col not in df.columns or df[col].is_null().all():
            return False

        for x in df[col].to_list():
            if not x or str(x).strip().lower() in ("null", "none", "nan", ""):
                continue
            try:
                val = json.loads(x)
                if isinstance(val, dict) and val != {}:
                    return True
            except json.JSONDecodeError:
                continue

        return False

    def _weighted_mean(self, scores: list[float], weights: list[float]) -> float:
        """Compute weighted mean, ignoring NaN values."""
        if not scores or not weights:
            return 0.0

        scores_arr, weights_arr = (
            np.array(scores, dtype=float),
            np.array(weights, dtype=float),
        )
        valid_mask = ~np.isnan(scores_arr)

        weighted_sum = np.nansum(scores_arr * weights_arr)
        total_weight = np.nansum(weights_arr[valid_mask])

        if total_weight == 0:
            return 0.0

        return round(weighted_sum / total_weight, 4)

    # ============================================================
    # FREETEXT COMPARISON
    # ============================================================

    def _compare_freetext(
        self, s1: str | None, s2: str | None, ignore_order: bool = True
    ) -> float | None:
        """
        Compare two freetext strings using token, n-gram, and overlap similarity.
        Returns 1.0 for exact matches.
        """
        # --- Normalize ---
        s1 = self._normalize_text(s1)
        s2 = self._normalize_text(s2)

        # --- Early exits ---
        if (not s1 and not s2) or (s1 is None and s2 is None):
            return None
        if (not s1 or not s2) or (s1 is None or s2 is None):
            return None

        # --- Exact match shortcut ---
        if s1 == s2:
            return 1.0

        # --- Tokenize ---
        tokens1, tokens2 = self._tokenize_freetext(s1, s2, ignore_order)

        # --- Token-level similarity ---
        token_similarity = self._token_similarity(tokens1, tokens2)
        if token_similarity == 0.0:
            return 0.0

        # --- N-gram similarity ---
        ngram_score = self._weighted_ngram_similarity(tokens1, tokens2, ignore_order)

        # --- Token overlap ---
        overlap_ratio = len(set(tokens1) & set(tokens2)) / max(
            len(tokens1), len(tokens2)
        )

        # --- Weighted combination ---
        weights = self.freetext_fields_weights or {}
        final_score = (
            weights.get("token", 0.0) * token_similarity
            + weights.get("ngram", 0.0) * ngram_score
            + weights.get("overlap", 0.0) * overlap_ratio
        )

        return round(final_score, 4)

    def _normalize_text(self, text: str | None) -> str:
        """Normalize a text string for comparison."""
        if not text:
            return ""
        return (
            str(text)
            .strip()
            .lower()
            .replace("none", "")
            .replace("null", "")
            .replace("nan", "")
        )

    def _tokenize_freetext(
        self, s1: str, s2: str, ignore_order: bool
    ) -> tuple[list[str], list[str]]:
        """Split and optionally sort tokens by separator delimiter."""
        separator = self.freetext_fields_separator

        tokens1 = [t for t in s1.split(separator) if t]
        tokens2 = [t for t in s2.split(separator) if t]

        if ignore_order:
            tokens1.sort()
            tokens2.sort()
        return tokens1, tokens2

    def _token_similarity(self, tokens1: list[str], tokens2: list[str]) -> float:
        """Compute token-level Levenshtein similarity."""
        token_scores = []
        similar_pairs = 0

        for t1 in tokens1:
            best_score = 0.0
            for t2 in tokens2:
                dist = Levenshtein.distance(t1, t2)
                if dist <= self.levenshtein_max_distance:
                    similar_pairs += 1
                    best_score = max(best_score, 1 - dist / max(len(t1), len(t2)))
            token_scores.append(best_score)

        if similar_pairs == 0 or not token_scores:
            return 0.0

        return float(np.mean(token_scores))

    def _weighted_ngram_similarity(
        self, tokens1: list[str], tokens2: list[str], ignore_order: bool
    ) -> float:
        """Compute weighted similarity across multiple n-gram sizes."""
        if not self.ngram_weights:
            return 0.0

        scores, weights = [], []

        for n, w in self.ngram_weights.items():
            if not isinstance(n, int) or not isinstance(w, float):
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
            scores.append(sim if sim is not None else np.nan)
            weights.append(w)

        return self._weighted_mean(scores, weights)

    def _clean_tokens(self, tokens: list[str]) -> list[str]:
        """Remove invalid or placeholder tokens."""
        return [
            str(t).strip()
            for t in tokens or []
            if t not in (None, "", "none", "null", "nan")
            and str(t).strip().lower() not in ("none", "null", "nan")
        ]

    def _ngrams_from_tokens(
        self, tokens: list[str], n: int, ignore_order: bool = True
    ) -> list[str]:
        """
        Generate n-grams from a list of tokens.

        Args:
            tokens (list[str]): List of input tokens.
            n (int): Size of the n-gram.
            ignore_order (bool): Whether to sort the resulting n-grams.

        Returns:
            list[str]: A list of n-gram strings joined by ':'.
        """
        # Clean and normalize tokens
        clean_tokens = self._clean_tokens(tokens)

        if not clean_tokens:
            return []

        # If fewer tokens than n, return one joined sequence
        if len(clean_tokens) < n:
            ngrams = [":".join(clean_tokens)]
        else:
            ngrams = [
                ":".join(clean_tokens[i : i + n])
                for i in range(len(clean_tokens) - n + 1)
            ]

        return sorted(ngrams) if ignore_order else ngrams

    def _ngram_similarity(
        self, tokens1: list[str], tokens2: list[str], max_distance: int = 2
    ) -> float:
        """
        Compute the average similarity between two n-gram token lists
        based on normalized Levenshtein distance.

        Args:
            tokens1 (list[str]): First n-gram list.
            tokens2 (list[str]): Second n-gram list.
            max_distance (int): Maximum Levenshtein distance threshold.

        Returns:
            float: Mean similarity between 0.0 and 1.0.
        """
        if not tokens1 or not tokens2:
            return 0.0

        tokens1 = self._clean_tokens(tokens1)
        tokens2 = self._clean_tokens(tokens2)

        scores = []
        for t1 in tokens1:
            best = 0.0
            for t2 in tokens2:
                dist = Levenshtein.distance(t1, t2)
                if dist <= max_distance:
                    score = 1 - (dist / max(len(t1), len(t2)))
                    best = max(best, score)
            scores.append(best)

        return float(np.mean(scores)) if scores else 0.0

    # ============================================================
    # VERSION COMPARISON
    # ============================================================

    def _safe_version(self, val: str | None):
        """
        Safely convert a string into a Version object.
        Returns None if the value is invalid or empty.
        """
        if not val:
            return None
        try:
            return Version(str(val))
        except InvalidVersion:
            return None

    def _bool_or_default(self, value, default=True):
        """
        Returns the given value if it's not None,
        otherwise returns the default (True by default).
        """
        return value if value is not None else default

    def _range_in_range(self, asset_range: dict, csaf_range: dict) -> bool:
        """
        Check if an asset's version range overlaps with (or fits within)
        a CSAF version range.

        This means: returns True if there is any intersection between the two ranges.
        Missing bounds are treated as open (±∞).
        Missing inclusive flags default to True.
        """

        def _to_float(value):
            try:
                return float(value)
            except (TypeError, ValueError):
                return None

        # --- Extract numbers ---
        a_min = _to_float(asset_range.get("min"))
        a_max = _to_float(asset_range.get("max"))
        c_min = _to_float(csaf_range.get("min"))
        c_max = _to_float(csaf_range.get("max"))

        # --- Inclusivity flags (default True) ---
        a_min_inc = self._bool_or_default(asset_range.get("min_inclusive"))
        a_max_inc = self._bool_or_default(asset_range.get("max_inclusive"))
        c_min_inc = self._bool_or_default(csaf_range.get("min_inclusive"))
        c_max_inc = self._bool_or_default(csaf_range.get("max_inclusive"))

        # --- Case 1: both ranges empty
        if all(v is None for v in (a_min, a_max, c_min, c_max)):
            return True

        # --- Case 2: CSAF has no bounds, cannot compare
        if c_min is None and c_max is None:
            return False

        # --- Case 3: Asset has no bounds, not within CSAF
        if a_min is None and a_max is None:
            return False

        # --- Replace None with ±∞ ---
        a_min = a_min if a_min is not None else float("-inf")
        a_max = a_max if a_max is not None else float("inf")
        c_min = c_min if c_min is not None else float("-inf")
        c_max = c_max if c_max is not None else float("inf")

        # --- Check if they overlap ---
        # Overlap exists if left edge of one is <= right edge of the other, and vice versa
        if a_max < c_min:
            return False
        if a_min > c_max:
            return False

        # Handle exclusive bounds equality
        if a_max == c_min and (not a_max_inc or not c_min_inc):
            return False
        if a_min == c_max and (not a_min_inc or not c_max_inc):
            return False

        return True

    def _compare_versions(
        self, csaf_version: dict | list | None, asset_version: dict | list | None
    ) -> float | None:
        """
        Compare version structures (dict or list) using configured version subfield weights.

        This function handles nested lists of versions, version ranges, and qualifiers,
        and computes a weighted similarity score between 0.0 and 1.0.

        Returns:
            float | None: Weighted similarity score, or None if both versions are empty.
        """
        # --- 1. Base cases ---
        if not csaf_version and not asset_version:
            return None
        if not csaf_version or not asset_version:
            return 0.0

        # --- 2. Handle list of versions recursively ---
        if isinstance(csaf_version, list):
            return self._compare_version_lists(csaf_version, asset_version)

        # --- 3. Ensure both are dicts ---
        if not isinstance(csaf_version, dict) or not isinstance(asset_version, dict):
            return 0.0

        # --- 4. Weighted field comparison ---
        scores, weights = [], []

        score_min_max_version = self._compare_version_ranges(
            csaf_version, asset_version
        )

        if score_min_max_version > 0:
            for field, w in (self.version_weights or {}).items():
                if not isinstance(w, float):
                    continue

                if field == "min_max_version":
                    score = score_min_max_version
                elif field == "qualifier":
                    score = self._compare_qualifiers(csaf_version, asset_version)
                elif field == "release_number":
                    csaf_rel = csaf_version.get("release_number")
                    asset_rel = asset_version.get("release_number")
                    score = self._compare_release_numbers(csaf_rel, asset_rel)
                else:
                    # fallback freetext
                    csaf_val = str(csaf_version.get(field) or "")
                    asset_val = str(asset_version.get(field) or "")
                    score = self._compare_freetext(
                        csaf_val, asset_val, ignore_order=False
                    )

                if score is None or np.isnan(score):
                    continue

                weights.append(w)
                scores.append(score)

        return self._weighted_mean(scores, weights)

    def _compare_version_lists(
        self, csaf_list: list, asset_versions: dict | list | None
    ) -> float | None:
        """Compare lists of version dictionaries recursively."""
        if not csaf_list:
            return None

        scores = []

        for csaf_v in csaf_list:
            if isinstance(asset_versions, list):
                scores.extend(
                    self._compare_versions(csaf_v, asset_v)
                    for asset_v in asset_versions
                    if asset_v
                )
            else:
                scores.append(self._compare_versions(csaf_v, asset_versions))

        valid = [s for s in scores if isinstance(s, (int, float)) and s is not None]

        return round(max(valid), 4) if valid else None

    def _compare_version_ranges(
        self, csaf_version: dict, asset_version: dict
    ) -> float | None:
        """Compare version ranges (min/max) between CSAF and asset."""
        if not csaf_version and not asset_version:
            return np.nan

        if (
            not csaf_version
            or not asset_version
            or not isinstance(csaf_version, dict)
            or not isinstance(asset_version, dict)
        ):
            return 0.0

        csaf_ranges = [
            r
            for r in csaf_version.get("min_max_version", [])
            if r.get("min") or r.get("max")
        ]
        asset_ranges = [
            r
            for r in asset_version.get("min_max_version", [])
            if r.get("min") or r.get("max")
        ]

        if not csaf_ranges and not asset_ranges:
            return np.nan
        if not csaf_ranges or not asset_ranges:
            return 0.0

        valid = all(
            any(self._range_in_range(a_range, c_range) for c_range in csaf_ranges)
            for a_range in asset_ranges
        )
        return 1.0 if valid else 0.0

    def _compare_qualifiers(
        self, csaf_version: dict, asset_version: dict
    ) -> float | None:
        """
        Compare pre-release (qualifier) parts according to SemVer precedence:
        - pre-release < release
        - Numeric identifiers compared numerically
        - Non-numeric identifiers compared lexically
        Returns:
            1.0 if asset is same or newer pre-release than CSAF
            0.0 if asset is older
            np.nan if both empty
        """
        if not csaf_version and not asset_version:
            return np.nan

        if not csaf_version or not asset_version:
            return 0.0

        csaf_q = csaf_version.get("qualifier")
        asset_q = asset_version.get("qualifier")

        if not csaf_q and not asset_q:
            return np.nan
        if not csaf_q and asset_q:
            return np.nan
        if csaf_q and not asset_q:
            return 0.0

        csaf_parts = str(csaf_q).split(".")
        asset_parts = str(asset_q).split(".")

        for c, a in zip(csaf_parts, asset_parts):
            if c == a:
                continue
            c_is_num, a_is_num = c.isdigit(), a.isdigit()
            if c_is_num and a_is_num:
                return 1.0 if int(a) > int(c) else 0.0
            elif c_is_num and not a_is_num:
                return 1.0
            elif not c_is_num and a_is_num:
                return 0.0
            else:
                return 1.0 if a > c else 0.0

        return 1.0 if len(asset_parts) >= len(csaf_parts) else 0.0

    def _compare_release_numbers(self, csaf_rel: str, asset_rel: str) -> float:
        """
        Compare two release numbers (major.minor.patch) numerically.
        Returns:
            1.0 if equal
            0.5 if same major but different minor/patch
            0.0 otherwise
        """
        if not csaf_rel and not asset_rel:
            return np.nan
        if not csaf_rel or not asset_rel:
            return 0.0

        def to_tuple(v):
            parts = str(v).split(".")
            nums = []
            for p in parts[:3]:
                try:
                    nums.append(int(p))
                except ValueError:
                    nums.append(0)
            while len(nums) < 3:
                nums.append(0)
            return tuple(nums)

        c = to_tuple(csaf_rel)
        a = to_tuple(asset_rel)

        if a == c:
            return 1.0
        if a[0] == c[0]:
            return 0.5
        return 0.0

    # ============================================================
    # FIELD COMPARISON HELPERS
    # ============================================================

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

    def _compare_fields(
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

    # ============================================================
    # DATAFRAME MATCHING
    # ============================================================

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
                    lambda row: self._compare_fields(
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

#     # print(matcher._safe_version("1.2.3") == Version("1.2.3"))
#     # print(matcher._safe_version("") is None)
#     # print(matcher._safe_version("not_a_version") is None)

#     # test_cases = [
#     #     ({"min": "0.8", "max": "0.9", "min_inclusive": False}, {"min": "0.9", "max": "1.3"}, True),
#     #     ({"min": "1.0", "max": "1.2"}, {"min": "1.0", "max": "1.2"}, True),
#     # ]

#     # for asset_range, csaf_range, expected in test_cases:
#     #     result = matcher._range_in_range(asset_range, csaf_range)
#     #     if result == expected:
#     #         print(f"Passed for asset_range={asset_range} csaf_range={csaf_range}")
#     #     else:
#     #         print(f"Failed for asset_range={asset_range} csaf_range={csaf_range} got {result}, expected {expected}")

#     # print(matcher._compare_freetext("nginx", "nginx") == 1.0)
#     # print(matcher._compare_freetext("nginx", "apache") < 1.0)
#     # print(matcher._compare_freetext("", "") is None)
#     # print(matcher._compare_freetext("foo", "") == 0.0)

#     # tokens1 = ["nginx", "server"]
#     # tokens2 = ["nginx", "proxy"]

#     # score = matcher._weighted_ngram_similarity(tokens1, tokens2, ignore_order=True)
#     # print(0.0 <= score <= 1.0)

#     # asset_field = {'schema': 'pep-440', 'raw': '21.0.0.0', 'package': None, 'release_prefix': None, 'release_number': '21.0.0.0', 'release_branch': None, 'qualifier': [None, None], 'build_number': None, 'architecture': None, 'date': None, 'epoch': None, 'min_max_version': [{'min': '21.0.0.0', 'max': '21.0.0.0'}]}
#     # csaf_field = {'schema': 'pep-440', 'raw': '21.0.0.0', 'package': None, 'release_prefix': None, 'release_number': '21.0.0.0', 'release_branch': None, 'qualifier': [None, None], 'build_number': None, 'architecture': None, 'date': None, 'epoch': None, 'min_max_version': [{'min': None, 'max': '21.0.0.0'}]}
#     # csaf_field = {
#     #     "schema": "semantic-versioning",
#     #     "release_number": None,
#     #     "qualifier": None,
#     #     "min_max_version": [{"min": "1.0.0", "max": "1.0.0"}]
#     # }

#     # asset_field = {
#     #     "schema": "semantic-versioning",
#     #     "release_number": None,
#     #     "qualifier": "alpha",
#     #     "min_max_version": [{"min": "1.0.0", "max": "1.0.0"}]
#     # }
#     # print(matcher._extract_field(csaf_field, "min_max_version"))
#     # print(matcher._compare_versions(csaf_field, asset_field))
#     # print(matcher._compare_fields(
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

#     # csaf_sbom_urls = ["https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/", "https://www.test.org"]
#     # asset_sbom_urls = ["https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/"]
#     # print(matcher._compare_fields(csaf_sbom_urls, asset_sbom_urls))

#     # csaf_product_type = "Device"
#     # asset_product_type = "Undefined"
#     # print(matcher._compare_fields(csaf_product_type, asset_product_type))

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
