import time
from dina.cachedb.database import Device, DeviceType
from dina.cachedb.model import (
    CsafDocument,
    CsafProduct,
    CsafProductTree,
    # File,
    # Hash,
    Manufacturer,
    Software,
    Product,
    CsafProductRelationship
)
from dina.common import logging
from typing import List, Optional, Tuple, Union
from .datamodels import (
    CsafDocument as Document,
    CsafProductTree as ProductTree,
    ProductIdentificationHelper,
    ProductInfo,
)

logger = logging.get_logger(__name__)


async def convert_into_database_format(product_tree: ProductTree) -> List[Union[CsafProductTree, CsafProductRelationship]]:
    if product_tree.csaf_document is None:
        return None

    starttime = time.time()

    csaf_full_product_list: List[Union[CsafProductTree, CsafProductRelationship]] = []

    document: Document = product_tree.csaf_document
    csaf_document = CsafDocument()
    csaf_document.url = document.url
    csaf_document.lang = document.lang
    csaf_document.publisher = document.publisher
    csaf_document.version = document.version

    csaf_product_list: List[CsafProduct] = []
    
    for product_list in product_tree.product_list:
        for product in product_list:
            product_name_id, cpe, helper, product_version, products = await get_product_values(product)

            if (cpe == "a" or cpe == "o") or (helper and helper.purl and helper.purl.startswith("pkg:")):
                logger.info("Software")
                manufacturer = None

                if m_name := product.manufacturer:
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
                csaf_product.product_name_id = product_name_id
                csaf_product.software = software
                csaf_product_list.append(csaf_product)

                csaf_product_tree = CsafProductTree()
                csaf_product_tree.csaf_product = csaf_product
                csaf_product_tree.csaf_document = csaf_document
                csaf_full_product_list.append(csaf_product_tree)

            elif (
                cpe == "h"
                or (helper and helper.serial_numbers)
                or (helper and helper.model_numbers)
                or (helper and helper.skus)
            ):
                logger.info("Device")
                manufacturer = None

                if m_name := product.manufacturer:
                    manufacturer = Manufacturer()
                    manufacturer.name = m_name
                    manufacturer.last_seen = starttime

                device_type = DeviceType()
                device_type.manufacturer = manufacturer
                device_type.cpe = cpe
                device_type.hardware_name = list_to_str(products)  # duplicate value
                device_type.hardware_version = product_version
                device_type.device_family = product.product_family
                device_type.last_seen = starttime

                if helper and helper.skus is not None and isinstance(helper.skus, list):
                    device_type.part_numbers = helper.skus

                if helper and helper.model_numbers is not None and isinstance(
                    helper.model_numbers, list
                ):
                    device_type.model_numbers = helper.model_numbers

                device = Device()
                device.device_type = device_type
                device.name = list_to_str(products)  # duplicate value
                device.last_seen = starttime

                if helper and helper.serial_numbers is not None and isinstance(
                    helper.serial_numbers, list
                ):
                    device.serial_numbers = helper.serial_numbers

                csaf_product = CsafProduct()
                csaf_product.product_name_id = product_name_id
                csaf_product.device = device
                csaf_product_list.append(csaf_product)

                csaf_product_tree = CsafProductTree()
                csaf_product_tree.csaf_product = csaf_product
                csaf_product_tree.csaf_document = csaf_document
                csaf_full_product_list.append(csaf_product_tree)
            elif cpe is None:
                logger.info("Undefined Type")

                manufacturer = None

                if m_name := product.manufacturer:
                    manufacturer = Manufacturer()
                    manufacturer.name = m_name
                    manufacturer.last_seen = starttime

                prod = Product()
                prod.name = list_to_str(products)
                prod.cpe = cpe
                prod.version = product_version
                prod.manufacturer = manufacturer
                prod.last_seen = starttime

                device_type = DeviceType()
                device_type.manufacturer = manufacturer
                device_type.cpe = cpe
                device_type.hardware_name = list_to_str(products)  # duplicate value
                device_type.hardware_version = product_version
                device_type.device_family = product.product_family
                device_type.last_seen = starttime

                if helper and helper.skus is not None and isinstance(helper.skus, list):
                    device_type.part_numbers = helper.skus

                if helper and helper.model_numbers is not None and isinstance(
                    helper.model_numbers, list
                ):
                    device_type.model_numbers = helper.model_numbers

                prod.device_type = device_type
                prod.name = list_to_str(products)  # duplicate value
                prod.last_seen = starttime

                if helper and helper.serial_numbers is not None and isinstance(
                    helper.serial_numbers, list
                ):
                    prod.serial_numbers = helper.serial_numbers

                csaf_product = CsafProduct()
                csaf_product.product_name_id = product_name_id
                csaf_product.product = prod
                csaf_product_list.append(csaf_product)

                csaf_product_tree = CsafProductTree()
                csaf_product_tree.csaf_product = csaf_product
                csaf_product_tree.csaf_document = csaf_document
                csaf_full_product_list.append(csaf_product_tree)
    
    for relationship in product_tree.relationships_list:
        product_reference: Optional[CsafProduct] = None
        relates_to_product_reference: Optional[CsafProduct] = None

        for csaf_product in csaf_product_list:
            if csaf_product.product_name_id == relationship.product_reference:
                product_reference = csaf_product
            
            if csaf_product.product_name_id == relationship.relates_to_product_reference:
                relates_to_product_reference = csaf_product

            if product_reference != None and relates_to_product_reference != None: 
                relationship_value = CsafProductRelationship()
                relationship_value.category = relationship.category
                relationship_value.csaf_product_source = product_reference
                relationship_value.csaf_product_target = relates_to_product_reference
                csaf_full_product_list.append(relationship_value)
                break

    return csaf_full_product_list

async def get_product_values(product: ProductInfo) -> Tuple[Optional[str], Optional[str], Optional[ProductIdentificationHelper], List, List]:
    cpe = None
    helper = None
    product_name_id = None
    product_version = []
    products = []
       
    if product and (pv := product.product_version):
        if pv.name not in product_version:
            product_version.append(pv.name)

        if p := pv.product:
            product_name_id = p.product_id

            if p.name not in products:
                products.append(p.name)
            
            if h := p.product_identification_helper:
                helper = h

                if (cpe := h.cpe):
                    cpe = extract_cpe_part(cpe)
    
    if product and (pv := product.product_version_range):
        if pv.name and pv.name not in product_version:
            product_version.append(pv.name)

        if p := pv.product:
            product_name_id = p.product_id

            if p.name not in products:
                products.append(p.name)
            
            if h := p.product_identification_helper:
                helper = h

                if cpe := h.cpe:
                    cpe = extract_cpe_part(cpe)

    if product and (p := product.product):
        products.append(p.name)
        product_name_id = p.product_id

        if h := p.product_identification_helper:
            helper = h

            if cpe := h.cpe:
                cpe = extract_cpe_part(cpe)

    return (product_name_id, cpe, helper, product_version, products)

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
