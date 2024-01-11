from nicegui import ui
from typing import Optional

from .base import SingleValueBindableUi
from ..utils.signals import ReadonlyRef, is_ref, effect
from ..utils.signals import _TMaybeRef as TMaybeRef
from ..utils import convert_kws_ref2value


class CircularProgressBindableUi(SingleValueBindableUi[str, ui.circular_progress]):
    def __init__(
        self,
        value: Optional[TMaybeRef[float]] = 0.0,
        *,
        min: Optional[TMaybeRef[float]] = 0.0,
        max: Optional[TMaybeRef[float]] = 1.0,
        size: Optional[TMaybeRef[str]] = 'xl',
        show_value: Optional[TMaybeRef[bool]] = True,
        color: Optional[TMaybeRef[str]] = 'primary',
        indeterminate: Optional[TMaybeRef[bool]] = False,
        reverse: Optional[TMaybeRef[bool]] = False,
        instant_feedback: Optional[TMaybeRef[bool]] = False,
        angle: Optional[TMaybeRef[int]] = 0,
        center_color: Optional[TMaybeRef[str]] = None,
        track_color: Optional[TMaybeRef[str]] = None,
        font_size: Optional[TMaybeRef[str]] = "0.25em",
        rounded: Optional[TMaybeRef[bool]] = False,
        thickness: Optional[TMaybeRef[float]] = 0.2,
        animation_speed: Optional[TMaybeRef[int]] = 600,
    ):
        """Literal values of parameters

        :param size: (e.g.) 16px/ 2rem/ xs/ md
        :param color: (e.g.) primary/ teal-10
        :param track_color: (e.g.) primary/ teal-10
        :param center_color: (e.g.) primary/ teal-10
        """
        kws = {
            "value": value,
            "min": min,
            "max": max,
            "size": size,
            "show_value": show_value,
            "color": color,
        }
        value_kws = convert_kws_ref2value(kws)
        element = ui.circular_progress(**value_kws)
        super().__init__(element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)

        kws_extra = {
            "indeterminate": indeterminate,
            "center_color": center_color,
            "track_color": track_color,
            "font_size": font_size,
            "rounded": rounded,
            "thickness": thickness,
            "animation_speed": animation_speed,
            "angle": angle,
            "reverse": reverse,
            "instant_feedback": instant_feedback,
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
            self.element.set_value(ref_ui.value)

        return self