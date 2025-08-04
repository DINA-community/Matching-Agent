from dataclasses import dataclass
from typing import Optional

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
