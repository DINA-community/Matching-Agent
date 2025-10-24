from typing import List, Union

from dina.cachedb.model import Asset, CsafProduct
from dina.synchronizer.plugin_base.preprocessor import PreprocessorPlugin


class DefaultPreprocessor(PreprocessorPlugin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    async def preprocess(
        self, data: List[Union[Asset, CsafProduct]]
    ) -> List[Union[Asset, CsafProduct]]:
        # TODO: Implement preprocessing
        return data
