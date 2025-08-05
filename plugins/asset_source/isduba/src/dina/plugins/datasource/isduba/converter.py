from dina.common import logging
from typing import List
from .datamodels import ProductInfo, CsafDocument, CsafProductTree

logger = logging.get_logger(__name__)

def extract_cpe_part(cpe: str) -> str:
    if not cpe or not isinstance(cpe, str):
        return None

    parts = cpe.split(":")

    if len(parts) < 3:
        return None

    if parts[1].startswith("/"):
        return parts[1].lstrip("/")

    if len(parts) > 2 and parts[0] == "cpe":
        return parts[2]
    
    return None

def convert_into_database_format(csaf_product_tree: CsafProductTree):
    document: CsafDocument = csaf_product_tree.csaf_document
    product_list_infos: List[List[ProductInfo]] = csaf_product_tree.product_list

    for product_list in product_list_infos:
        for product in product_list:
            if ((pv := product.product_version) and
                (p := pv.product) and
                (helper := p.product_identification_helper) and
                (cpe := helper.cpe)):
                part = extract_cpe_part(cpe)

                if part == "a" or part == "o":
                    logger.info("Software")
                    # software = Software()
                    # manufacturer_id = None

                    # if m_name:= product.manufacturer:
                    #     manufacturer = Manufacturer()
                    
                    # software.name = p.name
                    # software.manufacturer = manufacturer_id
                    # software.cpe = cpe
                    # software.version = pv.name
                elif part == "h":
                    logger.info("Device")
                    # if m_name:= product.manufacturer:
                    #     manufacturer = Manufacturer()
                    #     device_type = Device_Type()
                    #     device = Device()
                    break
                print(part)
