from typing import List, Union
import logging

from dina.cachedb.model import Manufacturer, DeviceType

# from dina.netbox_api.net_box_rest_api_client.models import manufacturer
from dina.synchronizer.plugin_base.preprocessor import PreprocessorPlugin

logger = logging.getLogger(__name__)


class NetboxPreprocessor(PreprocessorPlugin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    async def preprocess(self, data) -> List[Union[Manufacturer]]:
        result = []
        for x in data[0]:
            logger.info(f"DATA: {x}")
            if x.__class__.__name__ == "Manufacturer":
                result.append(Manufacturer(nb_id=x.id, name=x.name))
            if x.__class__.__name__ == "DeviceType":
                if x.custom_fields.additional_properties['model_number'] == None:
                    model_number = ""
                else:
                    model_number=x.custom_fields.additional_properties['model_number']
                result.append(DeviceType(nb_id=x.id,model=x.model,model_number=model_number,part_number=x.part_number, hardware_name=x.custom_fields.additional_properties['hardware_name'],hardware_version=x.custom_fields.additional_properties['hardware_version'],device_family=x.custom_fields.additional_properties['device_family'],cpe=x.custom_fields.additional_properties['cpe'],nb_manu_id=x.manufacturer.id))
        return result

