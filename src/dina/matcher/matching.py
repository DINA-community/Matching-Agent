import json
import re
from rapidfuzz.distance import Levenshtein
import polars as pl
from rapidfuzz import fuzz
from packaging.version import Version, InvalidVersion


class Matching:
    def __init__(self, freetext_fields: list[str], ordered_fields: list[str]):
        self.freetext_fields = freetext_fields
        self.ordered_fields = ordered_fields

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

        if asset_min is None and asset_max is None:
            return False
        if csaf_min is None and csaf_max is None:
            return False

        if asset_min and csaf_min and asset_min < csaf_min:
            return False
        if asset_max and csaf_max and asset_max > csaf_max:
            return False
        return True

    def _compare_versions(self, csaf_version: dict, asset_version: dict) -> float:
        subfields = [
            "package",
            "release_prefix",
            "release_number",
            "release_branch",
            "build_number",
            "qualifier",
            "architecture",
            "date",
            "epoch",
            "min_max_version",
        ]

        scores = []

        for subfield in subfields:
            if subfield == "min_max_version":
                csaf_ranges = csaf_version.get("min_max_version") or []
                asset_ranges = asset_version.get("min_max_version") or []

                csaf_ranges = [r for r in csaf_ranges if r.get("min") or r.get("max")]
                asset_ranges = [r for r in asset_ranges if r.get("min") or r.get("max")]

                if not csaf_ranges or not asset_ranges:
                    scores.append(0.0)
                    continue

                valid = all(
                    any(
                        self._range_in_range(a_range, c_range)
                        for c_range in csaf_ranges
                    )
                    for a_range in asset_ranges
                )

                scores.append(1.0 if valid else 0.0)
            elif subfield == "qualifier":
                csaf_qualifier = csaf_version.get("qualifier") or []
                asset_qualifier = asset_version.get("qualifier") or []

                if not csaf_qualifier or not asset_qualifier:
                    scores.append(0.0)
                    continue

                if len(csaf_qualifier) != len(asset_qualifier):
                    scores.append(0.0)
                    continue

                part_scores = []

                for c, a in zip(csaf_qualifier, asset_qualifier):
                    if c is None or a is None:
                        scores.append(0.0)
                        continue
                    ft_score = self._compare_freetext_with_order(str(c), str(a))
                    part_scores.append(ft_score / 100.0)

                if part_scores:
                    scores.append(sum(part_scores) / len(part_scores))
            else:
                csaf_field = str(csaf_version.get(subfield) or "")
                asset_field = str(asset_version.get(subfield) or "")

                if not csaf_field or not asset_field:
                    scores.append(0.0)
                    continue

                ft_score = self._compare_freetext_with_order(csaf_field, asset_field)
                scores.append(ft_score / 100.0)

        return sum(scores) / len(scores) if scores else 0.0

    def _compare_freetext_with_order(self, s1: str, s2: str) -> float:
        s1 = (s1 or "").strip().lower()
        s2 = (s2 or "").strip().lower()

        if not s1 or not s2:
            return 0.0

        tokens1 = [t for t in s1.split(".") if len(t) > 2]
        tokens2 = [t for t in s2.split(".") if len(t) > 2]

        if not tokens1 or not tokens2:
            return 0.0

        # TODO: clarify whether token order should matter for matching
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

    def _compare_freetext(self, s1: str, s2: str) -> float:
        s1 = (s1 or "").strip().lower()
        s2 = (s2 or "").strip().lower()

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
            val = json.loads(val)
            if val:
                return val
            else:
                return {}
        except Exception:
            return {}

    def df_matching(self, df_norm):
        for field in self.freetext_fields:
            csaf_norm = f"csaf_{field}_norm"
            asset_norm = f"asset_{field}_norm"

            if csaf_norm in df_norm and asset_norm in df_norm:
                df_norm = df_norm.with_columns(
                    [
                        pl.struct([csaf_norm, asset_norm])
                        .map_elements(
                            lambda row: self._compare_freetext(
                                row[csaf_norm], row[asset_norm]
                            ),
                            return_dtype=pl.Float64,
                        )
                        .alias(f"{field}_match")
                    ]
                )

                # print(df_norm.select([csaf_norm, asset_norm, f"{field}_match"]))

        for field in self.ordered_fields:
            csaf_norm = f"csaf_{field}_norm"
            asset_norm = f"asset_{field}_norm"

            if csaf_norm in df_norm and asset_norm in df_norm:
                df_norm = df_norm.with_columns(
                    [
                        pl.struct([csaf_norm, asset_norm])
                        .map_elements(
                            lambda row: self._compare_versions(
                                self._safe_load(row[csaf_norm]),
                                self._safe_load(row[asset_norm]),
                            ),
                            return_dtype=pl.Float64,
                        )
                        .alias(f"{field}_match")
                    ]
                )

                # print(df_norm.select([csaf_norm, asset_norm, f"{field}_match"]))

        return df_norm
