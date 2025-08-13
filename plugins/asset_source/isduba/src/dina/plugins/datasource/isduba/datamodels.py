from dataclasses import dataclass
from typing import List, Optional


@dataclass
class FileHash:
    algorithm: Optional[str] = None
    value: Optional[str] = None


@dataclass
class Hash:
    file_hashes: Optional[FileHash] = None
    file_name: Optional[str] = None


@dataclass
class ProductIdentificationHelper:
    hashes: Optional[Hash] = None
    cpe: Optional[str] = None
    purl: Optional[str] = None
    model_numbers: Optional[List[str]] = None
    skus: Optional[List[str]] = None
    sbom_urls: Optional[List[str]] = None
    serial_numbers: Optional[List[str]] = None


@dataclass
class Product:
    name: Optional[str] = None
    product_id: Optional[str] = None
    product_identification_helper: Optional[ProductIdentificationHelper] = None


@dataclass
class ProductVersion:
    name: Optional[str] = None
    product: Optional[Product] = None


@dataclass
class ProductVersionRange:
    name: Optional[str] = None
    product: Optional[Product] = None


@dataclass
class ProductInfo:
    manufacturer: Optional[str] = None
    product_name: Optional[str] = None
    product_family: Optional[str] = None
    service_pack: Optional[str] = None
    patch_level: Optional[str] = None
    host_name: Optional[str] = None
    product_version_range: Optional[ProductVersionRange] = None
    product_version: Optional[ProductVersion] = None
    product: Optional[Product] = None


@dataclass
class CsafDocument:
    url: Optional[str] = None
    title: Optional[str] = None
    version: Optional[str] = None
    lang: Optional[str] = None
    publisher: Optional[str] = None


@dataclass
class CsafProductTree:
    csaf_document: Optional[CsafDocument] = None
    product_list: Optional[List[List[ProductInfo]]] = None
