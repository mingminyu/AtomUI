from typing import Dict
from ..utils.signals import to_value


def convert_kws_ref2value(kws: Dict):
    return {key: to_value(value) for key, value in kws.items()}
