from typing import Optional
from nicegui import ui

from .base import BindableUi
from ..utils.signals import _TMaybeRef as TMaybeRef
from ..utils import convert_kws_ref2value


class RowBindableUi(BindableUi[ui.row]):
    def __init__(
        self,
        wrap: Optional[TMaybeRef[bool]] = True
    ) -> None:
        kws = {"wrap": wrap}
        value_kws = convert_kws_ref2value(kws)
        element = ui.row(**value_kws)
        super().__init__(element)
