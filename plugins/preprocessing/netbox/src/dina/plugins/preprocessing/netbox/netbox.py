from typing import List, Union
import logging

from dina.cachedb.model import Manufacturer
#from dina.netbox_api.net_box_rest_api_client.models import manufacturer
from dina.synchronizer.plugin_base.preprocessor import PreprocessorPlugin

logger = logging.getLogger(__name__)


class NetboxPreprocessor(PreprocessorPlugin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    async def preprocess(
        self, data
    ) -> List[Union[Manufacturer]]:
        result = []
        for x in data[0]:
            logger.info(f"DATA: {x}")
            if x.__class__.__name__ == "Manufacturer":
                result.append(Manufacturer(nb_id=x.id, name=x.name))
        logger.info(f"RESULT: {result}")
        return result
