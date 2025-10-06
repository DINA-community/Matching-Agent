
class Score:
    def __init__(self, freetext_fields: list[str], ordered_fields: list[str], other_fields: list[str]):
        self.fields = freetext_fields + ordered_fields + other_fields

    def calculate_overall_score(self, df_norm):
        vendor_score = product_name_score = product_family_score = version_score = keyword_score = 0.0
        vendor_threshold = 0
        product_family_threshold = 0
        product_name_threshold = 20
        keyword_threshold = 0
        version_threshold = 20

        keyword_scores = []

        for field in self.fields:
            match field:
                case "manufacturer_name":
                    val = df_norm.select([f"{field}_match"]).to_series()
                    if not val.is_empty():
                        vendor_score = val.item() * 100
                case "name":
                    val = df_norm.select([f"{field}_match"]).to_series()
                    if not val.is_empty():
                        product_name_score = val.item() * 100
                case "device_family":
                    val = df_norm.select([f"{field}_match"]).to_series()
                    if not val.is_empty():
                        product_family_score = val.item() * 100
                case "version":
                    val = df_norm.select([f"{field}_match"]).to_series()
                    if not val.is_empty():
                        version_score = val.item() * 100
                case _:
                    val = df_norm.select([f"{field}_match"]).to_series()
                    if not val.is_empty():
                        keyword_scores.append(val.item() * 100)

        keyword_score = sum(keyword_scores) / len(keyword_scores) if keyword_scores else 0.0

        score_percent = (vendor_score + product_name_score + product_family_score + version_score + keyword_score) / 5

        if score_percent > 100:
            print(score_percent)
        # Check if vendor score is missing
        if vendor_score is None:
            return 0, "No Match vendor missing", score_percent
        # Check if vendor score meets threshold
        elif vendor_score >= vendor_threshold:
            # Check if product family score is missing
            if product_family_score is None:
                # Check if product name score is missing
                if product_name_score is None:
                    return 0, "No Match Product Name and Family missing", score_percent
                # Check if product name score meets threshold
                if product_name_score >= product_name_threshold:
                    # Check if version score exists and meets threshold
                    if version_score is not None and version_score < version_threshold:
                        return 0, f"No Match - Version Score is below {version_threshold}% ({version_score}%)", score_percent
                    return 1, "Match - Family Missing", score_percent
                # Check if product name score is within a certain range and version and keyword scores exist
                elif (product_name_threshold-20) <= product_name_score < product_name_threshold and version_score is not None and keyword_score is not None:
                    # Perform version and keyword boost
                    overall_score = (3*vendor_score + 2*product_name_score + version_score + keyword_score) / 7
                    if overall_score >= keyword_threshold:
                        return 1, "Possible match - version and keyword boost", score_percent
                else:
                    return 0, f"No match - Product name score is below {product_name_threshold}% ({product_name_score}%)", score_percent
            # Check if product family score meets threshold
            elif product_family_score >= product_family_threshold:
                # Check if product name score is missing
                if product_name_score is None:
                    return 1, "Possible Match - Product Name missing", score_percent
                # Check if product name score meets threshold
                elif product_name_score >= product_name_threshold:
                    # Check if version score exists and meets threshold
                    if version_score is not None and version_score < version_threshold:
                        return 0, f"No Match - Version Score is below {version_threshold}% ({version_score}%)", score_percent
                    else:
                        return 1, "Match - Product Name and Family is given", score_percent
                # Check if product name score is within a certain range and version and keyword scores exist
                elif (product_name_threshold-20) <= product_name_score < product_name_threshold and version_score is not None and keyword_score is not None:
                    # Perform version and keyword boost
                    overall_score = (3*vendor_score + 2*product_name_score + version_score + keyword_score) / 7
                    if overall_score >= keyword_threshold:
                        return 1, "Possible match - version and keyword boost", score_percent
                else:
                    return 0, f"No match: Product name score is below {product_name_threshold}% ({product_name_score}%)", score_percent
            else:
                return 0, f"No match: Product family score is below {product_family_threshold}% ({product_family_score}%)", score_percent
        # Check if vendor score is below threshold
        elif vendor_score <= vendor_threshold:
            return 0, f"No match: Vendor score is below {vendor_threshold}% ({vendor_score}%)", score_percent
        return 0, "Loop Error", score_percent
