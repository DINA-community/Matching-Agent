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
                
        subfields = [
            "package", "release_prefix", "release_number",
            "release_branch", "build_number", "qualifier",
            "architecture", "date", "epoch", "min_max_version"
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
                    any(self._range_in_range(a_range, c_range) for c_range in csaf_ranges)
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
    
    def compare_fields(self, csaf_field: dict | str | None, asset_field: dict | str | None) -> float:        
        if not csaf_field or not asset_field:
            return 0.0

        if isinstance(csaf_field, str) and isinstance(asset_field, str):
            return self._compare_freetext_with_order(csaf_field, asset_field)

        if isinstance(csaf_field, dict) and isinstance(asset_field, dict):
            matches = 0.0
            total = 0

            for key in csaf_field.keys() & asset_field.keys():
                val1 = csaf_field[key]
                val2 = asset_field[key]

                if key == "version" and isinstance(val1, dict) and isinstance(val2, dict):
                    total += 1
                    matches += self._compare_versions(val1, val2)
                    continue

                if isinstance(val1, (str, dict)) and isinstance(val2, (str, dict)):
                    total += 1
                    similarity = self.compare_fields(val1, val2)
                    matches += similarity

            if total == 0:
                return 0.0
            
            return matches / total
        
        if isinstance(csaf_field, list) and isinstance(asset_field, list):            
            for a_field in asset_field:
                for c_field in csaf_field:
                    if isinstance(a_field, str) and isinstance(c_field, str):
                        if c_field == a_field:
                            return 1.0
                        
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

            if csaf_norm in df_norm and asset_norm in df_norm:
                df_norm = df_norm.with_columns(
                    pl.struct([csaf_norm, asset_norm])
                    .map_elements(
                        lambda row: self.compare_fields(
                            self._safe_load(row[csaf_norm]),
                            self._safe_load(row[asset_norm]),
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

#     # score = matcher.compare_fields(csaf_field, asset_field)
#     # csaf_sbom_urls = ["https://www.free.org/news/python-switch-statement-switch-case-example/", "https://www.test.org"]
#     # asset_sbom_urls = ["https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/"]

#     # score = matcher.compare_fields(csaf_sbom_urls, asset_sbom_urls)

#     # csaf_product_type = "Device"
#     # asset_product_type = "Undefined"

#     # score = matcher.compare_fields(csaf_product_type, asset_product_type)

# if __name__ == "__main__":
#     main()
