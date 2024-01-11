from nicegui import ui
from typing import Optional, Union
from signe import effect
from .base import SingleValueBindableUi, _bind_color
from ..utils.signals import ReadonlyRef, is_ref
from ..utils.signals import _TMaybeRef as TMaybeRef
from ..utils import convert_kws_ref2value



class SeparatorBindableUi(SingleValueBindableUi[str, ui.separator]):

    def __init__(
        self,
        *,
        spaced: Optional[TMaybeRef[Union[bool, str]]] = None,
        inset: Optional[TMaybeRef[Union[bool, str]]] = None,
        vertical: Optional[TMaybeRef[bool]] = None,
        dark: Optional[TMaybeRef[bool]] = False,
        size: Optional[TMaybeRef[str]] = None,
        color: Optional[TMaybeRef[str]] = None,
    ):
        element = ui.separator()
        super().__init__(element)

        kws_extra = {
            "spaced": spaced,
            "inset": inset,
            "vertical": vertical,
            "dark": dark,
            "size": size,
            "color": color,
        }
        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value


    def bind_prop(self, prop: str, ref_ui: ReadonlyRef):
        if prop == "color":
            return self.bind_color(ref_ui)

        return super().bind_prop(prop, ref_ui)

    def bind_color(self, ref_ui: ReadonlyRef):
        return _bind_color(self, ref_ui)
