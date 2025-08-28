import time
from typing import Optional, Tuple

from dina.cachedb.fetcher_view import FetcherView
from dina.cachedb.model import CsafProduct, ProductType, Product
from dina.common import logging

from .datamodels import (
    CsafDocument as Document,
    CsafProductTree as ProductTree,
    ProductIdentificationHelper,
    ProductInfo,
)

logger = logging.get_logger(__name__)


async def convert_into_database_format(
    fetcher_view: FetcherView,
    product_tree: ProductTree,
) -> list[CsafProduct]:
    """Convert CSAF product tree into database model objects."""
    if not product_tree.csaf_document:
        return []

    last_update = time.time()
    document: Document = product_tree.csaf_document
    csaf_products: list[CsafProduct] = []
    product_name_ids: list[str] = []

    for product_list in product_tree.product_list:
        for product in product_list:
            product_name_id, cpe_identifier, helper, product_version, products = (
                await get_product_values(product)
            )

            if product_name_id and "-fixed" in product_name_id:
                continue

            csaf_product = CsafProduct(
                last_update=last_update,
                origin_uri=document.host or None,
                origin_info={
                    "product_name_id": product_name_id,
                    "path": getattr(document, "path", None),
                    "version": getattr(document, "version", None),
                    "publisher": getattr(document, "publisher", None),
                    "lang": getattr(document, "lang", None),
                },
            )

            csaf_product.product = Product(
                product_type=determine_product_type(cpe_identifier, helper),
                name=list_to_str(products),
                version=product_version,
                cpe=helper.cpe if helper and helper.cpe else None,
                purl=helper.purl if helper and helper.purl else None,
                sbom_urls=getattr(helper, "sbom_urls", None),
                serial_numbers=getattr(helper, "serial_numbers", None),
                files=getattr(helper, "files", None),
                model_numbers=getattr(helper, "model_numbers", None),
                part_numbers=getattr(helper, "skus", None),
                device_family=product.product_family or None,
                manufacturer_name=product.manufacturer or None,
            )

            product_name_ids.append(product_name_id)
            csaf_products.append(csaf_product)

    existing_products = {
        (prod.origin_info.get("product_name_id"), prod.origin_info.get("path")): prod
        for prod in await fetcher_view.get_existing(
            CsafProduct,
            CsafProduct.origin_info["product_name_id"].astext.in_(product_name_ids),
        )
    }

    deduped: dict[tuple[Optional[str], Optional[str]], CsafProduct] = {}

    for prod in csaf_products:
        key = (prod.origin_info.get("product_name_id"), prod.origin_info.get("path"))
        if key in deduped:
            _update_product_fields(deduped[key].product, prod.product)
            deduped[key].origin_info.update(prod.origin_info)
            deduped[key].last_update = prod.last_update
        else:
            deduped[key] = prod

    result: list[CsafProduct] = []

    for key, prod in deduped.items():
        if key in existing_products:
            existing = existing_products[key]
            existing.last_update = prod.last_update
            existing.origin_info.update(prod.origin_info)

            if existing.product:
                _update_product_fields(existing.product, prod.product)
            else:
                existing.product = prod.product

            result.append(existing)
        else:
            result.append(prod)

    return result

#TODO: relationship between the products
"""
for relationship in product_tree.relationships_list:
    product_reference: Optional[CsafProduct] = None
    relates_to_product_reference: Optional[CsafProduct] = None

    for csaf_product in csaf_full_product_list:
        if csaf_product.origin_uri["product_name_id"] == relationship.product_reference:
            product_reference = csaf_product

        if (
            csaf_product.origin_uri["product_name_id"]
            == relationship.relates_to_product_reference
        ):
            relates_to_product_reference = csaf_product

        if (
            product_reference is not None
            and relates_to_product_reference is not None
        ):
            relationship_value = CsafProductRelationship()
            relationship_value.category = relationship.category
            relationship_value.csaf_product_source = product_reference
            relationship_value.csaf_product_target = relates_to_product_reference
            csaf_full_product_list.append(relationship_value)
            break
"""

def _update_product_fields(target: Product, source: Product) -> None:
    """Update all relevant fields of a Product without overwriting the object itself."""
    target.product_type = source.product_type
    target.name = source.name
    target.version = source.version
    target.cpe = source.cpe
    target.purl = source.purl
    target.sbom_urls = source.sbom_urls
    target.serial_numbers = source.serial_numbers
    target.files = source.files
    target.model_numbers = source.model_numbers
    target.part_numbers = source.part_numbers
    target.device_family = source.device_family
    target.manufacturer_name = source.manufacturer_name

def determine_product_type(
    cpe_identifier: Optional[str], helper: Optional[ProductIdentificationHelper]
) -> ProductType:
    """Determine product type based on CPE or helper info."""
    if (
        cpe_identifier in {"a", "o"}
        or (helper and helper.purl and helper.purl.startswith("pkg:"))
    ):
        return ProductType.Software
    
    if (
        cpe_identifier == "h"
        or any(
            getattr(helper, field, None)
            for field in ("serial_numbers", "model_numbers", "skus")
        )
    ):
        return ProductType.Device
    
    return ProductType.Undefined


async def get_product_values(
    product: ProductInfo,
) -> Tuple[Optional[str], Optional[str], Optional[ProductIdentificationHelper], list[str], list[str]]:
    """Extract values like product_id, cpe, helper, versions and names from ProductInfo."""
    product_name_id, cpe, helper = None, None, None
    product_version, products = [], []

    if product and product.product_version:
        _extract_from_version(product.product_version, product_version, products)
        product_name_id, helper, cpe = _extract_product_info(product.product_version, helper, cpe)

    if product and product.product_version_range:
        _extract_from_version(product.product_version_range, product_version, products)
        product_name_id, helper, cpe = _extract_product_info(product.product_version_range, helper, cpe)

    if product and product.product:
        products.append(product.product.name)
        product_name_id = product.product.product_id
        helper = product.product.product_identification_helper or helper
        if helper and helper.cpe:
            cpe = extract_cpe_part(helper.cpe)

    return product_name_id, cpe, helper, product_version, products


def _extract_from_version(pv, product_version: list[str], products: list[str]):
    """Helper: add version and product name from a ProductVersion object."""
    if pv.name and pv.name not in product_version:
        product_version.append(pv.name)

    if pv.product and pv.product.name not in products:
        products.append(pv.product.name)


def _extract_product_info(pv, helper, cpe):
    """Helper: extract product_id, helper and cpe from a ProductVersion object."""
    product_name_id = pv.product.product_id if pv.product else None

    if pv.product and pv.product.product_identification_helper:
        helper = pv.product.product_identification_helper
        if helper.cpe:
            cpe = extract_cpe_part(helper.cpe)

    return product_name_id, helper, cpe


def extract_cpe_part(cpe: str) -> Optional[str]:
    """Extract the relevant part from a CPE string."""
    if not cpe or not isinstance(cpe, str):
        return None
    parts = cpe.split(":")

    if len(parts) < 3:
        return None
    
    if parts[1].startswith("/"):
        return parts[1].lstrip("/")
    
    if parts[0] == "cpe":
        return parts[2]
    
    return None


def list_to_str(values: list) -> Optional[str]:
    """Join a list into a comma-separated string."""
    return ", ".join(values) if values else None
