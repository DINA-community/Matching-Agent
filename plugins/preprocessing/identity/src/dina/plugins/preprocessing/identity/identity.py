from typing import List, Union

from dina.cachedb.model import Asset, CsafDocument
from dina.manager.plugin_base.preprocessor import PreprocessorPlugin


class Identity(PreprocessorPlugin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    async def preprocess(
        self, data: List[Union[Asset, CsafDocument]]
    ) -> List[Union[Asset, CsafDocument]]:
        return data
