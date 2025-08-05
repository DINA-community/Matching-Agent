from dina.cachedb.database import Device, DeviceType
from dina.cachedb.model import CsafDocument, CsafProduct, CsafProductTree, Manufacturer, Software
from dina.common import logging
from typing import List
from .datamodels import CsafDocument as Document, CsafProductTree as ProductTree

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

def convert_into_database_format(product_tree: ProductTree) -> List[CsafProductTree]:
    if product_tree.csaf_document == None:
        return None
    
    csaf_product_tree_list: List[CsafProductTree] = []

    document: Document = product_tree.csaf_document
    csaf_document = CsafDocument()
    csaf_document.url = document.url
    csaf_document.lang = document.lang
    csaf_document.publisher = document.publisher
    csaf_document.version = document.version

    csaf_product_tree_list.append(csaf_document)
    
    for product_list in product_tree.product_list:
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
                    manufacturer = None
                    
                    if m_name:= product.manufacturer:
                        manufacturer = Manufacturer()
                        manufacturer.name = m_name
                    
                    software = Software()
                    software.name = p.name
                    software.manufacturer = manufacturer
                    software.cpe = cpe
                    software.version = pv.name
                    software.manufacturer = manufacturer

                    csaf_product = CsafProduct()
                    csaf_product.software = software

                    csaf_product_tree = CsafProductTree()
                    csaf_product_tree.csaf_product = csaf_product
                    csaf_product_tree.csaf_document = csaf_document
                    csaf_product_tree_list.append(csaf_product_tree)

                elif part == "h":
                    logger.info("Device")
                    manufacturer = None

                    if m_name:= product.manufacturer:
                        manufacturer = Manufacturer()

                    device_type = DeviceType()
                    device_type.manufacturer = manufacturer
                    device_type.cpe = cpe
                    device_type.hardware_name = p.name # duplicate value 
                    device_type.hardware_version = pv.name
                    device_type.device_family = product.product_family

                    if helper.skus is not None and isinstance(helper.skus, list):
                        device_type.part_number = ", ".join(helper.skus)
                    
                    if helper.model_numbers is not None and isinstance(helper.model_numbers, list):
                        device_type.model_number = ", ".join(helper.model_numbers)
                                            
                    device = Device()
                    device.device_type = device_type
                    device.name =  p.name # duplicate value 

                    if helper.serial_numbers is not None and isinstance(helper.serial_numbers, list):
                        device.serial = ", ".join(helper.serial_numbers)

                    csaf_product = CsafProduct()
                    csaf_product.device = device

                    csaf_product_tree = CsafProductTree()
                    csaf_product_tree.csaf_product = csaf_product
                    csaf_product_tree.csaf_document = csaf_document
                    csaf_product_tree_list.append(csaf_product_tree)

    return csaf_product_tree_list
