import json
from typing import List, Union

from dina.cachedb.model import Asset, CsafProduct
from dina.synchronizer.plugin_base.preprocessor import PreprocessorPlugin
from dina.plugins.preprocessing.default.normalizer import (
    parse_cpe,
    parse_files,
    parse_freetext,
    parse_purl,
    parse_version,
)


class DefaultPreprocessor(PreprocessorPlugin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    async def preprocess(
        self, data: List[Union[Asset, CsafProduct]]
    ) -> List[Union[Asset, CsafProduct]]:
        # TODO: add fields to separate file
        freetext_fields = {
            "name": 0.20,
            "hardware_name": 0.17,
            "manufacturer_name": 0.08,
            "device_family": 0.01,
        }

        ordered_fields = {
            "version": 0.10,
            "model": 0.03,
            "model_numbers": 0.03,
            "part_numbers": 0.03,
            "serial_numbers": 0.03,
        }

        other_fields = {
            "cpe": 0.15,
            "purl": 0.13,
            "product_type": 0.02,
            "sbom_urls": 0.01,
        }

        for d in data:
            if product := d.product:
                if freetext_fields and freetext_fields.keys():
                    for col in freetext_fields.keys():
                        value = getattr(product, col)
                        if value:
                            new_value = parse_freetext(value)
                            setattr(product, col, new_value)

                if ordered_fields and ordered_fields.keys():
                    for col in ordered_fields.keys():
                        value = getattr(product, col)
                        if value:
                            new_value = parse_version(value)

                            if col == "model" and isinstance(new_value, (dict, list)):
                                new_value = json.dumps(new_value)

                            setattr(product, col, new_value)

                if other_fields and other_fields.keys():
                    for col in other_fields.keys():
                        parsers = {
                            "cpe": parse_cpe,
                            "purl": parse_purl,
                            "files": parse_files,
                        }

                        if col in parsers:
                            parser = parsers[col]
                            value = getattr(product, col)
                            if value:
                                new_value = parser(value)
                                if isinstance(new_value, (dict, list)):
                                    new_value = json.dumps(new_value)

                                setattr(product, col, new_value)

        return data
