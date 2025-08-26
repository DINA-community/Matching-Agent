import time
from dina.cachedb.model import (
    CsafProduct,
    ProductType,
    Product
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

async def convert_into_database_format(
    product_tree: ProductTree,
) -> List[Union[CsafProduct]]:
    if product_tree.csaf_document is None:
        return None

    last_update = time.time()

    csaf_full_product_list: List[Union[CsafProduct]] = []

    document: Document = product_tree.csaf_document

    for product_list in product_tree.product_list:
        for product in product_list:
            (
                product_name_id,
                cpe,
                helper,
                product_version,
                products,
            ) = await get_product_values(product)

            product_type = ProductType.Undefined

            if (cpe == "a" or cpe == "o" 
                or (helper and helper.purl and helper.purl.startswith("pkg:"))
                ):
                product_type = ProductType.Software
            elif (
                cpe == "h"
                or (helper and helper.serial_numbers)
                or (helper and helper.model_numbers)
                or (helper and helper.skus)
                ):
                product_type = ProductType.Device

            model_product = Product()
            model_product.product_type = product_type
            model_product.name = list_to_str(products)
            model_product.version = product_version
            model_product.cpe = cpe

            if helper and helper.purl:
                model_product.purl = helper.purl

            if helper and helper.sbom_urls:
                model_product.sbom_urls = helper.sbom_urls

            if helper and helper.serial_numbers:
                model_product.serial_numbers = helper.serial_numbers

            if helper and helper.files:
                model_product.files = helper.files 

            # model_product.model = 

            if helper and helper.model_numbers:
                model_product.model_numbers = helper.model_numbers

            if helper and helper.skus:
                model_product.part_numbers = helper.skus
            
            if product_family := product.product_family:
                model_product.device_family = product_family

            if m_name := product.manufacturer:
                model_product.manufacturer_name = m_name

            csaf_product = CsafProduct()
            csaf_product.product = model_product
            csaf_product.last_update = last_update

            if document and document.host:
                csaf_product.origin_uri = document.host

            csaf_product.origin_info = {}

            if document and document.path:
                csaf_product.origin_info["path"] = document.path
            
            if document and document.version:
                csaf_product.origin_info["version"] = document.version

            if document and document.publisher:
                csaf_product.origin_info["publisher"] = document.publisher
            
            if document and document.lang:
                csaf_product.origin_info["lang"] = document.lang

            csaf_full_product_list.append(csaf_product)

    # for relationship in product_tree.relationships_list:
    #     product_reference: Optional[CsafProduct] = None
    #     relates_to_product_reference: Optional[CsafProduct] = None

    #     for csaf_product in csaf_product_list:
    #         if csaf_product.product_name == relationship.product_reference:
    #             product_reference = csaf_product

    #         if (
    #             csaf_product.product_name
    #             == relationship.relates_to_product_reference
    #         ):
    #             relates_to_product_reference = csaf_product

    #         if (
    #             product_reference is not None
    #             and relates_to_product_reference is not None
    #         ):
    #             relationship_value = CsafProductRelationship()
    #             relationship_value.category = relationship.category
    #             relationship_value.csaf_product_source = product_reference
    #             relationship_value.csaf_product_target = relates_to_product_reference
    #             csaf_full_product_list.append(relationship_value)
    #             break

    return csaf_full_product_list


async def get_product_values(
    product: ProductInfo,
) -> Tuple[
    Optional[str], Optional[str], Optional[ProductIdentificationHelper], List, List
]:
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

                if cpe := h.cpe:
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
