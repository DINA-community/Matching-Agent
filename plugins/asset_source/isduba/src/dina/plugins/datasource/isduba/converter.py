import time
from dina.cachedb.database import Device, DeviceType
from dina.cachedb.model import CsafDocument, CsafProduct, CsafProductTree, File, Hash, Manufacturer, Software
from dina.common import logging
from typing import List, Optional, Tuple
from .datamodels import CsafDocument as Document, CsafProductTree as ProductTree, ProductIdentificationHelper, ProductInfo

logger = logging.get_logger(__name__)

async def convert_into_database_format(product_tree: ProductTree) -> List[CsafProductTree]:
    if product_tree.csaf_document == None:
        return None
    
    starttime = time.time()
    
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
            cpe, helper, product_version, products = get_product_values(product)

            if cpe == "a" or cpe == "o":
                logger.info("Software")
                manufacturer = None
                
                if m_name:= product.manufacturer:
                    manufacturer = Manufacturer()
                    manufacturer.name = m_name
                    manufacturer.last_seen = starttime

                # TODO: add Hashes and Files 
                # hash = Hash()
                # hash.algorithm = None
                # hash.value = None

                # file = File()
                # file.hash = hash
                # file.filename = None
                
                software = Software()
                software.name = list_to_str(products)
                software.cpe = cpe
                software.version = product_version
                software.manufacturer = manufacturer
                software.last_seen = starttime

                csaf_product = CsafProduct()
                csaf_product.software = software

                csaf_product_tree = CsafProductTree()
                csaf_product_tree.csaf_product = csaf_product
                csaf_product_tree.csaf_document = csaf_document
                csaf_product_tree_list.append(csaf_product_tree)

            elif cpe == "h":
                logger.info("Device")
                manufacturer = None

                if m_name:= product.manufacturer:
                    manufacturer = Manufacturer()
                    manufacturer.name = m_name
                    manufacturer.last_seen = starttime

                device_type = DeviceType()
                device_type.manufacturer = manufacturer
                device_type.cpe = cpe
                device_type.hardware_name = list_to_str(products) # duplicate value 
                device_type.hardware_version = product_version
                device_type.device_family = product.product_family
                device_type.last_seen = starttime

                if helper.skus is not None and isinstance(helper.skus, list):
                    device_type.part_numbers = helper.skus
                
                if helper.model_numbers is not None and isinstance(helper.model_numbers, list):
                    device_type.model_numbers = helper.model_numbers
                                        
                device = Device()
                device.device_type = device_type
                device.name =  list_to_str(products) # duplicate value
                device.last_seen = starttime

                if helper.serial_numbers is not None and isinstance(helper.serial_numbers, list):
                    device.serial_numbers = helper.serial_numbers

                csaf_product = CsafProduct()
                csaf_product.device = device

                csaf_product_tree = CsafProductTree()
                csaf_product_tree.csaf_product = csaf_product
                csaf_product_tree.csaf_document = csaf_document
                csaf_product_tree_list.append(csaf_product_tree)

            elif cpe != None: 
                logger.info("Undefined Type")

    return csaf_product_tree_list

def get_product_values(product: ProductInfo) -> Tuple[Optional[str], Optional[ProductIdentificationHelper], List, List]:
    cpe = None
    helper = None
    product_version = []
    products = []
       
    if ((pv := product.product_version) and
        (p := pv.product)):
        if pv.name not in product_version:
            product_version.append(pv.name)
        
        if p.name not in products:
            products.append(p.name)
        
        if (h := p.product_identification_helper):
            helper = h

            if (cpe := h.cpe):
                cpe = extract_cpe_part(cpe)
    
    if ((pv := product.product_version_range) and
        (p := pv.product)):
        if pv.name and pv.name not in product_version:
            product_version.append(pv.name)
        
        if p.name not in products:
            products.append(p.name)
        
        if (h := p.product_identification_helper):
            helper = h

            if (cpe := h.cpe):
                cpe = extract_cpe_part(cpe)
    
    if ((p := product.product)):
        products.append(p.name)
        
        if (h := p.product_identification_helper):
            helper = h

            if (cpe := h.cpe):
                cpe = extract_cpe_part(cpe)

    return (cpe, helper, product_version, products)

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

def list_to_str(list_val: List) -> Optional[str]:
    if list_val is not None and isinstance(list_val, list):
        return ", ".join(list_val)
    
    return None