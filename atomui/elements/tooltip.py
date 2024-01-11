from nicegui import ui
from signe import effect
from typing import Literal, List, Any, Callable, Optional, Union, TypeVar, cast
from nicegui.elements.mixins.value_element import ValueElement
from .base import SingleValueBindableUi
from ..utils.signals import ReadonlyRef, is_ref
from ..utils.signals import _TMaybeRef as TMaybeRef
from ..utils import convert_kws_ref2value


_ANCHOR_OPTIONS = Literal[
    "top left", "top right", "top middle", "top start",
    "center left", "center right", "center middle", "center start",
    "bottom left", "bottom right", "bottom middle", "bottom start",
]


class TooltipBindableUi(SingleValueBindableUi[str, ui.tooltip]):
    def __init__(
        self,
        *,
        text: Optional[TMaybeRef[str]] = '',
        scroll_target: Optional[TMaybeRef[Union[str, ui.element]]] = None,
        target: Optional[TMaybeRef[Union[str, bool]]] = True,
        no_parent_event: Optional[TMaybeRef[bool]] = False,
        delay: Optional[TMaybeRef[int]] = 0,
        hide_delay: Optional[TMaybeRef[int]] = 0,
        max_height: Optional[TMaybeRef[str]] = None,
        max_width: Optional[TMaybeRef[str]] = None,
        anchor: Optional[TMaybeRef[_ANCHOR_OPTIONS]] = "bottom middle",
        self_: Optional[TMaybeRef[_ANCHOR_OPTIONS]] = "top middle",
        transition_show: Optional[TMaybeRef[str]] = "jump-down",
        transition_hide: Optional[TMaybeRef[str]] = "jump-up",
        transition_duration: Optional[TMaybeRef[Union[str, int]]] = 300,
        offset_x: Optional[TMaybeRef[int]] = None,
        offset_y: Optional[TMaybeRef[int]] = None,
    ):
        kws = {
            "text": text,
        }
        value_kws = convert_kws_ref2value(kws)
        element = ui.tooltip(**value_kws)
        super().__init__(text, element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)

        kws_extra = {
            "scroll-target": scroll_target,
            "target": target,
            "no-parent-event": no_parent_event,
            "delay": delay,
            "hide-delay": hide_delay,
            "max-height": max_height,
            "max-width": max_width,
            "anchor": anchor,
            "self": self_,
            "transition-show": transition_show,
            "transition-hide": transition_hide,
            "transition-duration": transition_duration,
        }

        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value

    def bind_prop(self, prop: str, ref_ui: ReadonlyRef):
        if prop == "text":
            return self.bind_text(ref_ui)

        return super().bind_prop(prop, ref_ui)

    def bind_text(self, ref_ui: ReadonlyRef):
        @effect
        def _():
            self.element.set_text(str(ref_ui.value))
            self.element.update()

        return self
