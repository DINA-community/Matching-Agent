from typing import List, Optional
import copy

from dina.cachedb.model import File, FileList
from .datamodels import (
    ProductInfo,
    ProductIdentificationHelper,
    ProductVersion,
    ProductVersionRange,
    Product,
    CsafDocument,
    CsafProductTree,
    Relationship,
)


async def get_csaf_product_tree(host: str, path: str, document: dict, product_tree: dict) -> Optional[CsafProductTree]:
    """Convert raw CSAF document + product_tree into CsafProductTree."""
    if not document or not product_tree:
        return None

    branches = product_tree.get("branches")
    if not branches:
        return None

    csaf_document = CsafDocument(
        host=host,
        path=path,
        title=document.get("title"),
        version=document.get("csaf_version"),
        lang=document.get("lang"),
        publisher=document.get("publisher", {}).get("name"),
    )

    product_list = [await get_product_info(branch) for branch in branches]

    relationships_list: List[Relationship] = [
        Relationship(
            category=r.get("category"),
            product_reference=r.get("product_reference"),
            relates_to_product_reference=r.get("relates_to_product_reference"),
        )
        for r in (product_tree.get("relationships") or [])
    ]

    return CsafProductTree(
        csaf_document=csaf_document,
        product_list=product_list,
        relationships_list=relationships_list,
    )


async def get_product_identification_helper(data: dict) -> Optional[ProductIdentificationHelper]:
    """Build ProductIdentificationHelper from raw dict."""
    if not data:
        return None

    helper = ProductIdentificationHelper(
        cpe=data.get("cpe"),
        purl=data.get("purl"),
        model_numbers=data.get("model_numbers"),
        skus=data.get("skus"),
        sbom_urls=data.get("sbom_urls"),
        serial_numbers=data.get("serial_numbers"),
    )

    hashes = data.get("hashes")
    
    if hashes:
        files = FileList()

        for entry in hashes:
            file = File(
                name=entry.get("filename"),
                hash_algorithm=entry.get("algorithm"),
                file_hash=entry.get("value"),
            )
            files.files.append(file)
        helper.files = files

    return helper


async def get_product_version(name: str, sub_branch: dict, as_range: bool = False) -> ProductVersion | ProductVersionRange:
    """Create a ProductVersion or ProductVersionRange object."""
    cls = ProductVersionRange if as_range else ProductVersion
    version_obj = cls(name=name)

    branch_product = sub_branch.get("product")
    
    if branch_product:
        version_obj.product = await get_product(branch_product)

    return version_obj


async def get_product(branch_product: dict) -> Product:
    """Convert product dict into Product model."""
    product = Product(
        name=branch_product.get("name"),
        product_id=branch_product.get("product_id"),
    )

    if helper := branch_product.get("product_identification_helper"):
        product.product_identification_helper = await get_product_identification_helper(helper)

    return product


async def get_product_info(sub_branch) -> List[ProductInfo]:
    result: List[ProductInfo] = []

    async def process_branch(current_branch, base_info: ProductInfo):
        info = copy.deepcopy(base_info)
        category = current_branch.get("category")
        name = current_branch.get("name")
        branch_product = current_branch.get("product")
        sub_branches = current_branch.get("branches", [])

        match category:
            case "vendor":
                info.manufacturer = name
            case "product_name":
                info.product_name = name
            case "product_family":
                info.product_family = name
            case "service_pack":
                info.service_pack = name
            case "patch_level":
                info.patch_level = name
            case "host_name":
                info.host_name = name
            case "product_version_range":
                info.product_version_range = await get_product_version(name, current_branch, as_range=True)
            case "product_version":
                info.product_version = await get_product_version(name, current_branch)

        if branch_product:
            info.product = await get_product(branch_product)

        if sub_branches:
            for child in sub_branches:
                await process_branch(child, info)
        else:
            result.append(info)

    await process_branch(sub_branch, ProductInfo())

    return result
