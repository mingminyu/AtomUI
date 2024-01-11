from nicegui import ui
from typing import Optional, Callable, Any

from .base import SingleValueBindableUi
from ..utils.signals import ReadonlyRef, is_ref
from ..utils.signals import _TMaybeRef as TMaybeRef
from ..utils import convert_kws_ref2value


class KnobBindableUi(SingleValueBindableUi[str, ui.knob]):
    def __init__(
        self,
        value: Optional[TMaybeRef[float]] = 0.0,
        *,
        min_: Optional[TMaybeRef[float]] = 0.0,
        max_: Optional[TMaybeRef[float]] = 1.0,
        step: Optional[TMaybeRef[float]] = 0.01,
        color: Optional[TMaybeRef[str]] = 'primary',
        center_color: Optional[TMaybeRef[str]] = None,
        track_color: Optional[TMaybeRef[str]] = None,
        size: Optional[TMaybeRef[str]] = None,
        show_value: Optional[TMaybeRef[bool]] = False,
        on_change: Optional[Callable[..., Any]] = None,
        name: Optional[TMaybeRef[str]] = None,
        reverse: Optional[TMaybeRef[bool]] = None,
        disable: Optional[TMaybeRef[bool]] = None,
        readonly: Optional[TMaybeRef[bool]] = None,
        instant_feedback: Optional[TMaybeRef[bool]] = False,
        angle: Optional[TMaybeRef[int]] = 0,
        inner_min: Optional[TMaybeRef[float]] = None,
        inner_max: Optional[TMaybeRef[float]] = None,
        font_size: Optional[TMaybeRef[str]] = "0.25em",
        thickness: Optional[TMaybeRef[float]] = 0.2,
        # other params: tabindex
    ):
        kws = {
            "value": value,
            "min": min_,
            "max": max_,
            "step": step,
            "color": color,
            "center-color": center_color,
            "track-color": track_color,
            "size": size,
            "show-value": show_value,
            "on-change": on_change,
        }
        value_kws = convert_kws_ref2value(kws)
        element = ui.knob(**value_kws)
        super().__init__(element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)

        kws_extra = {
            "name": name,
            "reverse": reverse,
            "disable": disable,
            "readonly": readonly,
            "instant-feedback": instant_feedback,
            "angle": angle,
            "inner-min": inner_min,
            "inner-max": inner_max,
            "font-size": font_size,
            "thickness": thickness
        }
        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value

    def bind_prop(self, prop: str, ref_ui: ReadonlyRef):
        return super().bind_prop(prop, ref_ui)
