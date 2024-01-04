from nicegui import ui
from signe import effect
from typing import Optional, Literal

from ..utils.signals import ReadonlyRef, is_ref
from ..utils.signals import _TMaybeRef as TMaybeRef
from ..utils import convert_kws_ref2value
from .base import SingleValueBindableUi, _bind_color


class BadgeBindableUi(SingleValueBindableUi[str, ui.badge]):
    def __init__(
            self,
            text: Optional[TMaybeRef[str]] = '',
            *,
            color: Optional[TMaybeRef[str]] = "primary",
            text_color: Optional[TMaybeRef[str]] = None,
            outline: Optional[TMaybeRef[bool]] = False,
            floating: Optional[TMaybeRef[bool]] = False,
            multi_line: Optional[TMaybeRef[bool]] = False,
            transparent: Optional[TMaybeRef[bool]] = False,
            rounded: Optional[TMaybeRef[bool]] = False,
            align: Optional[Literal['top', 'middle', 'bottom']] = None,
    ) -> None:
        kws = {
            "text": text,
            "color": color,
            "text_color": text_color,
            "outline": outline,
        }
        value_kws = convert_kws_ref2value(kws)
        element = ui.badge(**value_kws)
        super().__init__(text, element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)

        kws_extra = {
            "align": align,
            "rounded": rounded,
            "transparent": transparent,
            "multi-line": multi_line,
            "floating": floating,
        }

        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value

    def bind_prop(self, prop: str, ref_ui: ReadonlyRef):
        if prop == "text":
            return self.bind_text(ref_ui)

        if prop == "color":
            return self.bind_color(ref_ui)

        return super().bind_prop(prop, ref_ui)

    def bind_color(self, ref_ui: ReadonlyRef):
        return _bind_color(self, ref_ui)

    def bind_text(self, ref_ui: ReadonlyRef):
        @effect
        def _():
            ele = self.element
            ele._props["label"] = ref_ui.value
            ele.update()

        return self

    def bind_enabled(self, ref_ui: ReadonlyRef[bool]):
        @effect
        def _():
            self.element.on_enabled_change(ref_ui.value)

        return self

    def bind_disable(self, ref_ui: ReadonlyRef[bool]):
        @effect
        def _():
            self.element.on_enabled_change(not ref_ui.value)

        return self
