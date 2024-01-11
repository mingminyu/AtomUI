from nicegui import ui
from typing import Any, Callable, Optional, Literal
from .base import SingleValueBindableUi
from ..utils.signals import ReadonlyRef, is_ref
from ..utils.signals import _TMaybeRef as TMaybeRef
from ..utils import convert_kws_ref2value

_PAGE_STICKY_POSITIONS = Literal[
    'top-right',
    'top-left',
    'bottom-right',
    'bottom-left',
    'top',
    'right',
    'bottom',
    'left',
]


class PageStickyBindableUi(SingleValueBindableUi[str, ui.page_sticky]):
    def __init__(
        self,
        position: Optional[TMaybeRef[str]] = 'bottom-right',
        x_offset: Optional[TMaybeRef[float]] = 0,
        y_offset: Optional[TMaybeRef[float]] = 0,
        expand: Optional[TMaybeRef[bool]] = False
    ):
        """Literal value of parameters

        :param position: top-right/ top-left/ bottom-right/ bottom-left/ top/ bottom/ left/ right
        """
        kws = {
            "position": position,
            "x_offset": x_offset,
            "y_offset": y_offset
        }
        value_kws = convert_kws_ref2value(kws)
        element = ui.page_sticky(**value_kws)
        super().__init__(element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)

        kws_extra = {
            "expand": expand,
        }
        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value

    def bind_prop(self, prop: str, ref_ui: ReadonlyRef):
        return super().bind_prop(prop, ref_ui)
