import numpy as np

class Score:
    def __init__(self, freetext_fields: dict, ordered_fields: dict, other_fields: dict):
        self.fields = {**freetext_fields, **ordered_fields, **other_fields}

    def calculate_overall_score(self, df_norm):
        # TODO: add csaf_cpe_norm and csaf_purl_norm in a separate file
        csaf_cpe_norm = "csaf_cpe_norm"
        csaf_purl_norm = "csaf_purl_norm"
        vendor_score = product_name_score = product_family_score = version_score = keyword_score = 0.0
        vendor_threshold = 40
        product_family_threshold = 0
        product_name_threshold = 60
        keyword_threshold = 0
        version_threshold = 60

        keyword_scores = []

        scores = np.array([], dtype=float)
        scores_weights = np.array([], dtype=float)

        if self.fields and self.fields.items():
            for field, weight in self.fields.items():
                val = df_norm.select([f"{field}_match"]).to_series()
                scores_weights = np.append(scores_weights, weight)

                if val.item() is None:
                    scores = np.append(scores, np.nan)
                    continue

                if val.is_empty():
                    scores = np.append(scores, np.nan)
                    continue

                v = val.item()                
                
                field_csaf_cpe_norm_match = f"{field}_{csaf_cpe_norm}_match"

                match field:
                    case "manufacturer_name":
                        vendor_score = max(v, vendor_score)

                        if "cpe" in self.fields:
                            if field_csaf_cpe_norm_match in df_norm.columns:
                                cpe_asset = df_norm.select([field_csaf_cpe_norm_match]).to_series()

                                if cpe_asset.item() is not None:
                                    vendor_score = max(cpe_asset.item(), vendor_score)

                        scores = np.append(scores, vendor_score)
                        vendor_score = vendor_score * 100
                    case "name":
                        product_name_score = max(v, product_name_score)

                        if "cpe" in self.fields:
                            if field_csaf_cpe_norm_match in df_norm.columns:
                                cpe_asset = df_norm.select([field_csaf_cpe_norm_match]).to_series()

                                if cpe_asset.item() is not None:
                                    product_name_score = max(cpe_asset.item(), product_name_score)

                        scores = np.append(scores, product_name_score)
                        product_name_score = product_name_score * 100
                    case "device_family":
                        scores = np.append(scores, v)
                        product_family_score = v * 100
                    case "version":
                        version_score = max(v, version_score)

                        if "cpe" in self.fields:
                            asset_csaf_cpe_norm_match = f"asset_{csaf_cpe_norm}_match"

                            if asset_csaf_cpe_norm_match in df_norm.columns:
                                cpe_asset = df_norm.select([asset_csaf_cpe_norm_match]).to_series()
                                if cpe_asset.item() is not None: 
                                    version_score = max(cpe_asset.item(), version_score)
                            
                            if field_csaf_cpe_norm_match in df_norm.columns:
                                cpe_version = df_norm.select([field_csaf_cpe_norm_match]).to_series()
                                if cpe_version.item() is not None: 
                                    version_score = max(cpe_version.item(), version_score)
                        if "purl" in self.fields:
                            asset_csaf_purl_norm_match = f"asset_{csaf_purl_norm}_match"
                            version_csaf_purl_norm_match = f"{field}_{csaf_purl_norm}_match"

                            if asset_csaf_purl_norm_match in df_norm.columns:
                                purl_asset = df_norm.select([asset_csaf_purl_norm_match]).to_series()
                                if purl_asset.item() is not None: 
                                    version_score = max(purl_asset.item(), version_score)
                            
                            if version_csaf_purl_norm_match in df_norm.columns:
                                purl_version = df_norm.select([version_csaf_purl_norm_match]).to_series()
                                if purl_version.item() is not None: 
                                    version_score = max(purl_version.item(), version_score)

                        scores = np.append(scores, version_score)
                        version_score = version_score * 100
                    case _:
                        scores = np.append(scores, v)
                        keyword_scores.append(v * 100)

        keyword_score = sum(keyword_scores) / len(keyword_scores) if keyword_scores else 0.0

        weighted_sum = np.nansum(scores * scores_weights)
        weight_sum   = np.nansum(scores_weights[~np.isnan(scores)])
        normalized_score = weighted_sum / weight_sum if weight_sum > 0 else None

        score_percent = normalized_score * 100
        
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
