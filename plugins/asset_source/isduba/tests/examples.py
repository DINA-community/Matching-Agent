from dina.plugins.datasource.isduba.datamodels import (
    CsafProductTree,
    Product,
    ProductIdentificationHelper,
    ProductInfo,
    ProductVersion,
    Relationship,
    CsafDocument,
)

DOCS_META = [
    {
        "id": 1,
        "publisher": "Siemens ProductCERT",
        "title": "SSA-187636: Multiple Vulnerabilities in SENTRON 7KT PAC1260 Data Manager",
        "tracking_id": "SSA-187636",
        "version": "1",
    },
    {
        "id": 2,
        "publisher": "CISA",
        "title": "Dover Fueling Solutions ProGauge MAGLINK LX CONSOLE",
        "tracking_id": "ICSA-24-268-04",
        "version": "1",
    },
    {
        "id": 3,
        "publisher": "Siemens ProductCERT",
        "title": "SSA-454789: Deserialization Vulnerability in TeleControl Server Basic V3.1",
        "tracking_id": "SSA-454789",
        "version": "1",
    },
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
