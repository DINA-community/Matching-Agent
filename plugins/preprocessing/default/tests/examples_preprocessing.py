import time
from dina.cachedb.model import CsafProduct, Product, ProductType, File, FileList

FILES = FileList(
    files=[File(name="firmware.bin", file_hash="abc123", hash_algorithm="sha256")]
)

PRODUCT = Product(
    product_type=ProductType.Software,
    name="Example Software",
    version=["1.0.0"],
    cpe="cpe:/a:example:software:1.0.0",
    purl="pkg:generic/example@1.0.0",
    sbom_urls=["https://example.com/sbom.json"],
    serial_numbers=[],
    files=FILES,
    model="X200",
    model_numbers=["X200"],
    part_numbers=["1234"],
    device_family=None,
    hardware_name=None,
    manufacturer_name="ExampleCorp",
)

CSAF_PRODUCT = CsafProduct(
    id=1,
    origin_uri="https://advisories.example.com",
    origin_info={
        "product_name_id": "example-software-1",
        "path": "/api/documents/42",
        "version": "2.0",
        "publisher": "ExampleCorp",
        "lang": "en",
    },
    uri="https://advisories.example.com/api/documents/42",
    last_update=time.time(),
    product=PRODUCT,
)
