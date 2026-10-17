import json
from pathlib import Path

from dina.plugins.datasource.isduba.datamodels import (
    CsafProductTree,
    Product,
    ProductIdentificationHelper,
    ProductInfo,
    ProductVersion,
    Relationship,
    CsafDocument,
)

# Load CSAF documents uploaded by dev/isduba-set-sources.py to ISDuBA
# sorted by file name
CSAF_FILES = sorted(
    (Path(__file__).parents[4] / "dev/test-cases/csaf_files").rglob("*.json")
)
ISDUBA_DOCUMENTS = {
    document_id: json.loads(path.read_text(encoding="utf-8"))
    for document_id, path in enumerate(CSAF_FILES, start=1)
}


def highest_criticality(document: dict) -> float:
    """Highest CVSS base score of a document
    ISDuBA orders documents by descending `critical` field"""
    return max(
        (
            score[version]["baseScore"]
            for vulnerability in document.get("vulnerabilities", [])
            for score in vulnerability.get("scores", [])
            for version in ("cvss_v3", "cvss_v2")
            if version in score
        ),
        default=0,
    )


# GET /api/documents?orders=-critical
DOCS_META = [
    {
        "id": document_id,
        "publisher": document["document"]["publisher"]["name"],
        "title": document["document"]["title"],
        "tracking_id": document["document"]["tracking"]["id"],
        "version": document["document"]["tracking"]["version"],
    }
    for document_id, document in sorted(
        ISDUBA_DOCUMENTS.items(), key=lambda item: -highest_criticality(item[1])
    )
]

DOCUMENTS_FULL = [
    {
        "document": {
            "category": "csaf_base",
            "csaf_version": "2.0",
            "title": "Multiple Vulnerabilities in SENTRON 7KT PAC1260 Data Manager",
            "tracking": {"id": "SSA-187636"},
            "publisher": {"name": "Siemens ProductCERT"},
        },
        "product_tree": {
            "branches": [
                {
                    "category": "vendor",
                    "name": "Siemens",
                    "branches": [
                        {
                            "category": "product_name",
                            "name": "SENTRON 7KT PAC1260",
                            "product": {
                                "name": "SENTRON 7KT PAC1260",
                                "product_id": "fake-product-id-1",
                                "product_identification_helper": {
                                    "cpe": "cpe:/o:siemens:sentron_7kt_pac1260:-"
                                },
                            },
                        }
                    ],
                },
                {
                    "category": "vendor",
                    "name": "Siemens",
                    "branches": [
                        {
                            "category": "product_name",
                            "name": "TeleControl Server Basic V3.1",
                            "product": {
                                "name": "TeleControl Server Basic V3.1",
                                "product_id": "fake-product-id-11",
                                "product_identification_helper": {
                                    "cpe": "cpe:/o:siemens:telecontrol_server_basic:3.1"
                                },
                            },
                        }
                    ],
                },
            ],
            "relationships": [
                {
                    "category": "fake-category",
                    "full_product_name": {
                        "name": "SENTRON 7KT PAC1260",
                        "product_id": "fake-product-id-1",
                    },
                    "product_reference": "fake-product-id-1",
                    "relates_to_product_reference": "fake-product-id-11",
                }
            ],
        },
        "vulnerabilities": [
            {"cve": "CVE-2024-0001", "title": "Improper Input Validation"},
        ],
    },
    {
        "document": {
            "category": "csaf_base",
            "csaf_version": "2.0",
            "title": "Dover Fueling Solutions ProGauge MAGLINK LX CONSOLE Advisory",
            "tracking": {"id": "ICSA-24-268-04"},
            "publisher": {"name": "CISA"},
        },
        "product_tree": {
            "branches": [
                {
                    "category": "vendor",
                    "name": "Dover Fueling Solutions",
                    "branches": [
                        {
                            "category": "product_name",
                            "name": "ProGauge MAGLINK LX CONSOLE",
                            "product": {
                                "name": "ProGauge MAGLINK LX CONSOLE",
                                "product_id": "fake-product-id-2",
                                "product_identification_helper": {
                                    "cpe": "cpe:/o:dover:progauge_maglink_lx_console:-"
                                },
                            },
                        }
                    ],
                }
            ]
        },
        "vulnerabilities": [
            {"cve": "CVE-2024-1234", "title": "Authentication Bypass"},
        ],
    },
    {
        "document": {
            "category": "csaf_base",
            "csaf_version": "2.0",
            "title": "Deserialization Vulnerability in TeleControl Server Basic V3.1",
            "tracking": {"id": "SSA-454789"},
            "publisher": {"name": "Siemens ProductCERT"},
        },
        "product_tree": {
            "branches": [
                {
                    "category": "vendor",
                    "name": "Siemens",
                    "branches": [
                        {
                            "category": "product_name",
                            "name": "TeleControl Server Basic V3.1",
                            "product": {
                                "name": "TeleControl Server Basic V3.1",
                                "product_id": "fake-product-id-3",
                                "product_identification_helper": {
                                    "cpe": "cpe:/o:siemens:telecontrol_server_basic:3.1"
                                },
                            },
                        }
                    ],
                }
            ]
        },
        "vulnerabilities": [
            {"cve": "CVE-2024-5678", "title": "Unsafe Deserialization"},
        ],
    },
]

PRODUCT_HELPER = ProductIdentificationHelper(
    cpe="cpe:/a:vendor:product:1.2.3",
    purl="pkg:generic/vendor@1.2.3",
    model_numbers=["1234", "5678"],
    skus=["SKU-123"],
    sbom_urls=["https://example.com/sbom.json"],
    serial_numbers=["SN-98765"],
)

PRODUCT = Product(
    name="Example Product",
    product_id="P-001",
    product_identification_helper=PRODUCT_HELPER,
)

PRODUCT_VERSION = ProductVersion(
    name="1.2.3",
    product=PRODUCT,
)

PRODUCT_INFO = ProductInfo(
    manufacturer="ExampleCorp",
    product_name="Example Product",
    product_family="Example Family",
    service_pack="SP1",
    patch_level="PL2",
    host_name="example-host",
    product_version=PRODUCT_VERSION,
)

CSAF_DOCUMENT = CsafDocument(
    host="https://example.com",
    path="/api/documents/123",
    title="Example Security Advisory",
    version="2.0",
    lang="en",
    publisher="ExampleCERT",
)

RELATIONSHIPS = [
    Relationship(
        category="default_component_of",
        product_reference="P-001",
        relates_to_product_reference="P-002",
    ),
    Relationship(
        category="installed_on",
        product_reference="P-002",
        relates_to_product_reference="P-003",
    ),
]

CSAF_PRODUCT_TREE = CsafProductTree(
    csaf_document=CSAF_DOCUMENT,
    product_list=[[PRODUCT_INFO]],
    relationships_list=RELATIONSHIPS,
)
