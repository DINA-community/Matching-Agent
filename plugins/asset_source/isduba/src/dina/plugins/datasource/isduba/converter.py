from dina.common import logging
from typing import List
from .datamodels import ProductInfo, CsafDocument, CsafProductTree as ProductTree

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

def convert_into_database_format(product_tree: ProductTree):
    document: CsafDocument = product_tree.csaf_document
    product_list_infos: List[List[ProductInfo]] = product_tree.product_list

    document_id = None 

    for product_list in product_list_infos:
        for product in product_list:

            # Additional fields like `purl`, `model_numbers`, `skus`, and `serial_numbers` can be added for extended product identification. 
            # TODO: product.product_version_range
            if ((pv := product.product_version) and
                (p := pv.product) and
                (helper := p.product_identification_helper) and
                (cpe := helper.cpe)):
                part = extract_cpe_part(cpe)

                if part == "a" or part == "o":
                    logger.info("Software")
                    # manufacturer_id = None

                    # if m_name:= product.manufacturer:
                    #     manufacturer = Manufacturer()
                    
                    # software = Software()
                    # software.name = p.name
                    # software.manufacturer = manufacturer_id
                    # software.cpe = cpe
                    # software.version = pv.name

                    # software_id = None
                    # csaf_product = CsafProduct()
                    # csaf_product.software_id = software_id

                    # csaf_product_id = None
                    # csaf_product_tree = CsafProductTree()
                    # csaf_product_tree.csaf_product_id = csaf_product_id
                    # csaf_product_tree.csaf_document_id = document_id

                elif part == "h":
                    logger.info("Device")
                    # manufacturer_id = None

                    # if m_name:= product.manufacturer:
                    #     manufacturer = Manufacturer()
                    
                    # device_type = Device_Type()
                    # device_type.manufacturer = manufacturer_id
                    # device_type.cpe = cpe
                    # device_type.hardware_name = p.name # duplicate value 
                    # device_type.hardware_version = pv.name
                    # device_type.device_family = product.product_family

                    # if helper.skus is not None and isinstance(helper.skus, list):
                    #     device_type.part_number = ", ".join(helper.skus)
                    
                    # if helper.model_numbers is not None and isinstance(helper.model_numbers, list):
                    #     device_type.model_number = ", ".join(helper.model_numbers)
                        
                    # device_type_id = None
                    
                    # device = Device()
                    # device.device_type = device_type_id
                    # device.name =  p.name # duplicate value 

                    # if helper.serial_numbers is not None and isinstance(helper.serial_numbers, list):
                    #     device.serial = ", ".join(helper.serial_numbers)
                print(part)
