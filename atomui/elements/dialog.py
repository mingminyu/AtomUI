from typing import Optional, cast
from signe import effect
from nicegui import ui
from nicegui.elements.mixins.color_elements import TextColorElement
from .base import SingleValueBindableUi, _bind_color
from ..utils import convert_kws_ref2value
from ..utils.signals import ReadonlyRef, is_ref
from ..utils.signals import _TMaybeRef as TMaybeRef


class DialogBindableUi(SingleValueBindableUi[str, ui.dialog]):
    def __init__(
        self,
        *,
        value: Optional[TMaybeRef[bool]] = False,
        persistent: Optional[TMaybeRef[bool]] = False,
        no_esc_dismiss: Optional[TMaybeRef[bool]] = False,
        no_backdrop_dismiss: Optional[TMaybeRef[bool]] = False,
        no_route_dismiss: Optional[TMaybeRef[bool]] = False,
        auto_close: Optional[TMaybeRef[bool]] = False,
        no_refocus: Optional[TMaybeRef[bool]] = False,
        no_focus: Optional[TMaybeRef[bool]] = False,
        no_shake: Optional[TMaybeRef[bool]] = False,
        allow_focus_outside: Optional[TMaybeRef[bool]] = False,
        seamless: Optional[TMaybeRef[bool]] = False,
        maximized: Optional[TMaybeRef[bool]] = False,
        full_width: Optional[TMaybeRef[bool]] = False,
        full_height: Optional[TMaybeRef[bool]] = False,
        position: Optional[TMaybeRef[str]] = None,
        square: Optional[TMaybeRef[bool]] = False,
        transition_show: Optional[TMaybeRef[str]] = None,
        transition_hide: Optional[TMaybeRef[str]] = None,
        transition_duration: Optional[TMaybeRef[str]] = None,
    ):
        kws = {
            "value": value,
        }
        value_kws = convert_kws_ref2value(kws)
        element = ui.icon(**value_kws)
        super().__init__(value, element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)

        kws_extra = {
            "persistent": persistent,
            "no-esc-dismiss": no_esc_dismiss,
            "no-backdrop-dismiss": no_backdrop_dismiss,
            "no-route-dismiss": no_route_dismiss,
            "auto-close": auto_close,
            "no-refocus": no_refocus,
            "no-focus": no_focus,
            "no-shake": no_shake,
            "allow-focus-outside": allow_focus_outside,
            "seamless": seamless,
            "maximized": maximized,
            "full-width": full_width,
            "full-height": full_height,
            "position": position,
            "square": square,
            "transition_show": transition_show,
            "transition_hide": transition_hide,
            "transition_duration": transition_duration,
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
            self.element.on_value_change(ref_ui.value)

        return self
