from typing import List, Union

from dina.cachedb.model import Asset, CsafDocument
from dina.synchronizer.plugin_base.preprocessor import PreprocessorPlugin


class IdentityPreprocessor(PreprocessorPlugin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    async def preprocess(
        self, data: List[Union[Asset, CsafDocument]]
    ) -> List[Union[Asset, CsafDocument]]:
        return data
