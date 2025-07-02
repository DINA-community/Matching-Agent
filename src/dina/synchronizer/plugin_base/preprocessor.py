from abc import ABC, abstractmethod
from typing import Union, List

from dina.cachedb.model import CsafDocument, Asset


class PreprocessorPlugin(ABC):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @abstractmethod
    async def preprocess(
        self, data: List[Union[Asset, CsafDocument]]
    ) -> List[Union[Asset, CsafDocument]]:
        """
        Asynchronously preprocess a given list of `data` items. This function takes each element
        in the provided list, processes it, and then returns a new list of processed items.

        :param data: A list of either `Asset` or `CsafDocument` objects that need to be preprocessed.
                      Each object in the list will go through preprocessing based on its type.
        :return: A list of preprocessed items of the same types (`Asset` or `CsafDocument`).
        """
        ...
