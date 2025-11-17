import numpy as np
import polars as pl
from polars.exceptions import ColumnNotFoundError


class Score:
    def __init__(self, matching_config: dict):
        db = matching_config.get("database", {})
        freetext_fields = db.get("freetext_fields", {})
        ordered_fields = db.get("ordered_fields", {})
        other_fields = db.get("other_fields", {})

        cpe = matching_config.get("cpe", {})
        self.csaf_cpe_field_name = cpe.get("csaf_cpe_field_name", "csaf_cpe")

        purl = matching_config.get("purl", {})
        self.csaf_purl_field_name = purl.get("csaf_purl_field_name", "csaf_purl")

        threshold = matching_config.get("threshold", {})
        self.vendor_threshold = threshold.get("vendor", 0)
        self.product_family_threshold = threshold.get("product_family", 0)
        self.product_name_threshold = threshold.get("product_name", 0)
        self.keyword_threshold = threshold.get("keyword", 0)
        self.version_threshold = threshold.get("version", 0)

        self.fields = {**freetext_fields, **ordered_fields, **other_fields}

    def calculate_overall_score(self, df_norm: pl.DataFrame):
        """
        Compute an overall matching score with threshold-based classification.
        Returns:
            (int, str, float): (match_flag, message, score_percent)
        """
        scores, weights = [], []
        keyword_scores = []
        cpe_score, purl_score = 0.0, 0.0

        vendor_score = product_name_score = product_family_score = version_score = None

        # Extract base field matches
        for field, weight in (self.fields or {}).items():
            weights.append(weight)

            try:
                val = df_norm.select([f"{field}_match"])
                val = val.to_series()
            except ColumnNotFoundError:
                scores.append(np.nan)
                continue

            v = val.item() if not val.is_empty() else np.nan

            if v is None or np.isnan(v):
                scores.append(np.nan)
                continue

            if field == "cpe":
                cpe_score = v

            if field == "purl":
                purl_score = v

            # Compute field-specific score
            score = self._compute_field_score(df_norm, field, v)
            scores.append(score)

            # Keep for reporting
            if field == "manufacturer_name":
                vendor_score = score * 100
            elif field == "name":
                product_name_score = score * 100
            elif field == "device_family":
                product_family_score = score * 100
            elif field == "version":
                version_score = score * 100
            else:
                keyword_scores.append(score * 100)

        # Compute combined weighted score
        keyword_score = np.mean(keyword_scores) if keyword_scores else None

        if cpe_score == 1.0 or purl_score == 1.0:
            score_percent = 1.0
        else:
            scores = np.array(scores, dtype=float)
            weights = np.array(weights, dtype=float)
            valid_mask = ~np.isnan(scores)

            score_percent = (
                np.nansum(scores * weights) / np.nansum(weights[valid_mask]) * 100
                if np.any(valid_mask)
                else 0.0
            )

        return self._evaluate_thresholds(
            vendor_score,
            product_name_score,
            product_family_score,
            version_score,
            keyword_score,
            score_percent,
        )

    def _compute_field_score(
        self, df: pl.DataFrame, field: str, base_value: float
    ) -> float:
        """Compute the best score for a given field, considering CPE and PURL enhancements."""
        score = base_value

        # ---- Vendor and Product fields can be improved via CPE ----
        if field in {"manufacturer_name", "name", "version"}:
            score = self._max_field_score(df, field, base_value)

        return score

    def _max_field_score(self, df: pl.DataFrame, field: str, score: float) -> float:
        """Return max score among base, CPE and PURL fields if available."""
        check_fields = []

        if "cpe" in self.fields:
            check_fields.extend(
                [
                    f"asset_{self.csaf_cpe_field_name}_match",
                    f"{field}_{self.csaf_cpe_field_name}_match",
                ]
            )
        if "purl" in self.fields and field == "version":
            check_fields.extend(
                [
                    f"asset_{self.csaf_purl_field_name}_match",
                    f"{field}_{self.csaf_purl_field_name}_match",
                ]
            )

        for col in check_fields:
            if col in df.columns:
                val = df.select([col]).to_series().item()
                if val is not None:
                    score = max(score, val)

        return score

    def _evaluate_thresholds(
        self,
        vendor_score,
        product_name_score,
        product_family_score,
        version_score,
        keyword_score,
        score_percent,
    ):
        """Apply threshold-based match logic and return classification."""

        # Check if vendor score is missing
        if vendor_score is None:
            return 0, "No Match vendor missing", score_percent
        # Check if vendor score meets threshold
        elif vendor_score >= self.vendor_threshold:
            # Check if product family score is missing
            if product_family_score is None:
                # Check if product name score is missing
                if product_name_score is None:
                    return 0, "No Match Product Name and Family missing", score_percent
                # Check if product name score meets threshold
                if product_name_score >= self.product_name_threshold:
                    # Check if version score exists and meets threshold
                    if (
                        version_score is not None
                        and version_score < self.version_threshold
                    ):
                        return (
                            0,
                            f"No Match - Version Score is below {self.version_threshold}% ({version_score}%)",
                            score_percent,
                        )
                    return 1, "Match - Family Missing", score_percent
                # Check if product name score is within a certain range and version and keyword scores exist
                elif (
                    (self.product_name_threshold - 20)
                    <= product_name_score
                    < self.product_name_threshold
                    and version_score is not None
                    and keyword_score is not None
                ):
                    # Perform version and keyword boost
                    overall_score = (
                        3 * vendor_score
                        + 2 * product_name_score
                        + version_score
                        + keyword_score
                    ) / 7
                    if overall_score >= self.keyword_threshold:
                        return (
                            1,
                            "Possible match - version and keyword boost",
                            score_percent,
                        )
                else:
                    return (
                        0,
                        f"No match - Product name score is below {self.product_name_threshold}% ({product_name_score}%)",
                        score_percent,
                    )
            # Check if product family score meets threshold
            elif product_family_score >= self.product_family_threshold:
                # Check if product name score is missing
                if product_name_score is None:
                    return 1, "Possible Match - Product Name missing", score_percent
                # Check if product name score meets threshold
                elif product_name_score >= self.product_name_threshold:
                    # Check if version score exists and meets threshold
                    if (
                        version_score is not None
                        and version_score < self.version_threshold
                    ):
                        return (
                            0,
                            f"No Match - Version Score is below {self.version_threshold}% ({version_score}%)",
                            score_percent,
                        )
                    else:
                        return (
                            1,
                            "Match - Product Name and Family is given",
                            score_percent,
                        )
                # Check if product name score is within a certain range and version and keyword scores exist
                elif (
                    (self.product_name_threshold - 20)
                    <= product_name_score
                    < self.product_name_threshold
                    and version_score is not None
                    and keyword_score is not None
                ):
                    # Perform version and keyword boost
                    overall_score = (
                        3 * vendor_score
                        + 2 * product_name_score
                        + version_score
                        + keyword_score
                    ) / 7
                    if overall_score >= self.keyword_threshold:
                        return (
                            1,
                            "Possible match - version and keyword boost",
                            score_percent,
                        )
                else:
                    return (
                        0,
                        f"No match: Product name score is below {self.product_name_threshold}% ({product_name_score}%)",
                        score_percent,
                    )
            else:
                return (
                    0,
                    f"No match: Product family score is below {self.product_family_threshold}% ({product_family_score}%)",
                    score_percent,
                )
        # Check if vendor score is below threshold
        elif vendor_score <= self.vendor_threshold:
            return (
                0,
                f"No match: Vendor score is below {self.vendor_threshold}% ({vendor_score}%)",
                score_percent,
            )
        return 0, "Loop Error", score_percent
