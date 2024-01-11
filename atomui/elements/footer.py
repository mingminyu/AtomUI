from nicegui import ui
from typing import Optional, Union
from signe import effect
from .base import BindableUi, SingleValueBindableUi
from ..utils.signals import ReadonlyRef, is_ref
from ..utils.signals import _TMaybeRef as TMaybeRef
from ..utils import convert_kws_ref2value


class FooterBindableUi(BindableUi[ui.footer]):
    def __init__(
        self,
        *,
        value: Optional[TMaybeRef[bool]] = True,
        fixed: Optional[TMaybeRef[bool]] = True,
        bordered: Optional[TMaybeRef[bool]] = False,
        elevated: Optional[TMaybeRef[bool]] = False,
        wrap: Optional[TMaybeRef[bool]] = True,
        reveal: Optional[TMaybeRef[bool]] = False,
        height_hint: Optional[TMaybeRef[Union[int, str]]] = None,
    ):
        kws = {
            "value": value,
            "fixed": fixed,
            "bordered": bordered,
            "elevated": elevated,
            "wrap": wrap,
        }
        value_kws = convert_kws_ref2value(kws)
        element = ui.footer(**value_kws)
        super().__init__(element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)

        kws_extra = {
            "reveal": reveal,
            "height_hint": height_hint,
        }
        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value

    def bind_prop(self, prop: str, ref_ui: ReadonlyRef):
        if prop == "value":
            return self.bind_value(ref_ui)

        return super().bind_prop(prop, ref_ui)

    def bind_value(self, ref_ui: ReadonlyRef[bool]):
        @effect
        def _():
            self.element.bind_value(ref_ui.value)

        return self
