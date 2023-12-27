# coding: utf8
from typing import Any, Callable, Optional, Union
from nicegui.elements.mixins.disableable_element import DisableableElement
from nicegui.elements.mixins.value_element import ValueElement


class Space(DisableableElement):
    def __init__(self) -> None:
        super().__init__(tag='q-space')
