
from typing import List

from .datamodels import ProductInfo, FileHash, Hash, ProductIdentificationHelper, ProductVersion, ProductVersionRange, Product, CsafDocument, CsafProductTree
import copy

def get_product_info_list(document, branches) -> CsafProductTree:
    csaf_document = CsafDocument()
    product_list: List[List[ProductInfo]] = []

    if document and (title:= document["title"]):
        csaf_document.title = title
    
    if document and (version:= document["csaf_version"]):
        csaf_document.version = version

    if document and (lang:= document["lang"]):
        csaf_document.lang = lang

    if document and (references:= document["references"]) and (first:= references[0]) and (url:= first["url"]):
        csaf_document.url = url

    if document and (publisher:= document["publisher"]) and (p_name:= publisher["name"]):
        csaf_document.publisher = p_name

    if branches != None:
        for branch in branches:
            product: List[ProductInfo] = get_product_info(branch)
            product_list.append(product)
        
    return CsafProductTree(csaf_document=csaf_document, product_list=product_list)

def get_file_hash(file_hashes_value) -> FileHash:
    file_hash = FileHash()
    algorithm = file_hashes_value.get("algorithm")
    value = file_hashes_value.get("value")
    
    if algorithm != None:
        file_hash.algorithm = algorithm

    if value != None: 
        file_hash.value = value

    return file_hash

def get_product_identification_helper(product_identification_helper_value: str) -> ProductIdentificationHelper:
    product_identification_helper = ProductIdentificationHelper()
    hashes_value = product_identification_helper_value.get("hashes")
    cpe = product_identification_helper_value.get("cpe")

    if hashes_value != None:
        hashes = Hash()
        filename = hashes_value.get("filename")
        file_hashes_value = hashes_value.get("file_hashes")

        if filename != None:
            hashes.filename = filename

        if file_hashes_value != None:
            hashes.file_hashes = get_file_hash(file_hashes_value)
        
        product_identification_helper.hashes = hashes
    if cpe != None:
        product_identification_helper.cpe = cpe
    
    return product_identification_helper

def get_product_version(name: str, sub_branch) -> ProductVersion:
    product_version = ProductVersion()
    product_version.name = name
    branch_product = sub_branch.get("product")

    if branch_product != None:
        product_version.product = get_product(branch_product)
    
    return product_version

def get_product_version_range(name: str, sub_branch) -> ProductVersionRange:
    product_version_range = ProductVersionRange()
    product_version_range.name = name
    branch_product = sub_branch.get("product")

    if branch_product != None:
        product_version_range.product = get_product(branch_product)
    
    return product_version_range

def get_product(branch_product) -> Product:
    product_name = branch_product.get("name")
    product_id = branch_product.get("product_id")
    product_identification_helper = branch_product.get("product_identification_helper")
    product = Product()

    if product_name != None:
        product.name = product_name
    
    if product_id != None:
        product.product_id = product_id
    
    if product_identification_helper != None: 
        product.product_identification_helper = get_product_identification_helper(product_identification_helper)

    return product
    
def get_product_info(sub_branch) -> List[ProductInfo]:
    result: List[ProductInfo] = []

    def process_branch(current_branch, base_info: ProductInfo):
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
            info.product_version_range = get_product_version_range(name, current_branch)
        elif category == "product_version":
            info.product_version = get_product_version(name, current_branch)

        if branch_product:
            info.product = get_product(branch_product)

        if sub_branches:
            for child in sub_branches:
                process_branch(child, info)
        else:
            result.append(info)

    process_branch(sub_branch, ProductInfo())

    return result
