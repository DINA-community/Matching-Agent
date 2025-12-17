import json
from typing import List, Union

from dina.cachedb.model import Asset, CsafProduct
from dina.synchronizer.plugin_base.preprocessor import PreprocessorPlugin
from dina.plugins.preprocessing.default.normalizer import Normalizer


class DefaultPreprocessor(PreprocessorPlugin):
    def __init__(self, config=None, **kwargs):
        super().__init__(config=config, **kwargs)

    async def preprocess(
        self, data: List[Union[Asset, CsafProduct]]
    ) -> List[Union[Asset, CsafProduct]]:
        for d in data:
            if product := d.product:
                normalizer = Normalizer(self.config)
                if self.freetext_fields and self.freetext_fields.keys():
                    for col in self.freetext_fields.keys():
                        value = getattr(product, col)
                        if value:
                            new_value = normalizer.parse_freetext(value)
                            setattr(product, col, new_value)

                if self.ordered_fields and self.ordered_fields.keys():
                    for col in self.ordered_fields.keys():
                        value = getattr(product, col)
                        if value:
                            new_value = normalizer.parse_version(value)

                            if col == "model" and isinstance(new_value, (dict, list)):
                                new_value = json.dumps(new_value)

                            setattr(product, col, new_value)

                if self.other_fields and self.other_fields.keys():
                    for col in self.other_fields.keys():
                        parsers = {
                            "cpe": normalizer.parse_cpe,
                            "purl": normalizer.parse_purl,
                            "files": normalizer.parse_files,
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
