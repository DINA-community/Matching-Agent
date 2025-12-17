from dataclasses import dataclass, field
from typing import List, Optional

from dina.cachedb.model import FileList


@dataclass
class ProductIdentificationHelper:
    files: Optional[FileList] = None
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
    host: Optional[str] = None
    path: Optional[str] = None
    title: Optional[str] = None
    version: Optional[str] = None
    lang: Optional[str] = None
    publisher: Optional[str] = None


@dataclass
class Relationship:
    category: None | str = None
    product_reference: None | str = None
    relates_to_product_reference: None | str = None


@dataclass
class CsafProductTree:
    csaf_document: Optional[CsafDocument] = None
    product_list: List[List[ProductInfo]] = field(default_factory=list)
    relationships_list: List[Relationship] = field(default_factory=list)
