
from typing import List

from .datamodels import ProductInfo, FileHash, Hash, ProductIdentificationHelper, ProductVersion, ProductVersionRange, Product, CsafDocument, CsafProductTree, Relationship
import copy

async def get_csaf_product_tree(url, document, product_tree) -> CsafProductTree:
    if document is None or product_tree is None:
        return None
    
    branches = product_tree.get("branches")

    if branches is None: 
        return None
        
    csaf_document = CsafDocument()
    product_list: List[List[ProductInfo]] = []
    
    if url:
        csaf_document.url = url
    
    if document and (title:= document["title"]):
        csaf_document.title = title
    
    if document and (version:= document["csaf_version"]):
        csaf_document.version = version

    if document and (lang:= document["lang"]):
        csaf_document.lang = lang

    if document and (publisher:= document["publisher"]) and (p_name:= publisher["name"]):
        csaf_document.publisher = p_name

    if branches is not None:
        for branch in branches:
            product: List[ProductInfo] = await get_product_info(branch)
            product_list.append(product)

    relationships = product_tree.get("relationships")

    relationships_list = []

    if relationships is not None:
        for r in relationships:
            relationship = Relationship()
            relationship.category = r.get("category")
            relationship.product_reference = r.get("product_reference")
            relationship.relates_to_product_reference = r.get("relates_to_product_reference")
            relationships_list.append(relationship)
        
    return CsafProductTree(csaf_document=csaf_document, product_list=product_list, relationships_list=relationships_list)

async def get_file_hash(file_hashes_value) -> FileHash:
    file_hash = FileHash()
    algorithm = file_hashes_value.get("algorithm")
    value = file_hashes_value.get("value")
    
    if algorithm is not None:
        file_hash.algorithm = algorithm

    if value is not None: 
        file_hash.value = value

    return file_hash

async def get_product_identification_helper(product_identification_helper_value) -> ProductIdentificationHelper:
    if product_identification_helper_value is None: 
        return None
    
    product_identification_helper = ProductIdentificationHelper()
    hashes_value = product_identification_helper_value.get("hashes")
    cpe = product_identification_helper_value.get("cpe")
    purl = product_identification_helper_value.get("purl")
    model_numbers = product_identification_helper_value.get("model_numbers")
    skus = product_identification_helper_value.get("skus")
    sbom_urls = product_identification_helper_value.get("sbom_urls")
    serial_numbers = product_identification_helper_value.get("serial_numbers")

    if hashes_value is not None:
        hashes = Hash()
        filename = hashes_value.get("filename")
        file_hashes_value = hashes_value.get("file_hashes")

        if filename is not None:
            hashes.file_name = filename

        if file_hashes_value is not None:
            hashes.file_hash = await get_file_hash(file_hashes_value)
        
        product_identification_helper.hashes = hashes

    if cpe is not None:
        product_identification_helper.cpe = cpe
    
    if purl is not None:
        product_identification_helper.purl = purl
    
    if model_numbers is not None: 
        product_identification_helper.model_numbers = model_numbers
    
    if skus is not None: 
        product_identification_helper.skus = skus
    
    if sbom_urls is not None: 
        product_identification_helper.sbom_urls = sbom_urls

    if serial_numbers is not None: 
        product_identification_helper.serial_numbers = serial_numbers
    
    return product_identification_helper

async def get_product_version(name: str, sub_branch) -> ProductVersion:
    product_version = ProductVersion()
    product_version.name = name
    branch_product = sub_branch.get("product")

    if branch_product is not None:
        product_version.product = await get_product(branch_product)
    
    return product_version

async def get_product_version_range(name: str, sub_branch) -> ProductVersionRange:
    product_version_range = ProductVersionRange()
    product_version_range.name = name
    branch_product = sub_branch.get("product")

    if branch_product is not None:
        product_version_range.product = await get_product(branch_product)
    
    return product_version_range

async def get_product(branch_product) -> Product:
    product_name = branch_product.get("name")
    product_id = branch_product.get("product_id")
    product_identification_helper = branch_product.get("product_identification_helper")
    product = Product()

    if product_name is not None:
        product.name = product_name
    
    if product_id is not None:
        product.product_id = product_id
    
    if product_identification_helper is not None:
        product.product_identification_helper = await get_product_identification_helper(product_identification_helper)

    return product
    
async def get_product_info(sub_branch) -> List[ProductInfo]:
    result: List[ProductInfo] = []

    async def process_branch(current_branch, base_info: ProductInfo):
        info = copy.deepcopy(base_info)
        category = current_branch.get("category")
        name = current_branch.get("name")
        branch_product = current_branch.get("product")
        sub_branches = current_branch.get("branches", [])

        if category == "vendor":
            info.manufacturer = name
        elif category == "product_name":
            info.product_name = name
        elif category == "product_family":
            info.product_family = name
        elif category == "service_pack":
            info.service_pack = name
        elif category == "patch_level":
            info.patch_level = name
        elif category == "host_name":
            info.host_name = name
        elif category == "product_version_range":
            info.product_version_range = await get_product_version_range(name, current_branch)
        elif category == "product_version":
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
