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
                                "product_id": "4711",
                                "product_identification_helper": {
                                    "cpe": "cpe:/o:siemens:sentron_7kt_pac1260:-"
                                },
                            },
                        }
                    ],
                }
            ]
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
                                "product_id": "5822",
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
                                "product_id": "9348",
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
