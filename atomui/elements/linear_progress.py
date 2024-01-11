from nicegui import ui
from typing import Optional

from .base import SingleValueBindableUi
from ..utils.signals import ReadonlyRef, is_ref, effect
from ..utils.signals import _TMaybeRef as TMaybeRef
from ..utils import convert_kws_ref2value


class LineProgressBindableUi(SingleValueBindableUi[str, ui.linear_progress]):
    def __init__(
        self,
        value: Optional[TMaybeRef[float]] = 0.0,
        *,
        size: Optional[TMaybeRef[str]] = 'xl',
        show_value: Optional[TMaybeRef[bool]] = True,
        color: Optional[TMaybeRef[str]] = 'primary',
        buffer: Optional[TMaybeRef[float]] = None,
        reverse: Optional[TMaybeRef[bool]] = False,
        indeterminate: Optional[TMaybeRef[bool]] = False,
        query: Optional[TMaybeRef[bool]] = False,
        instant_feedback: Optional[TMaybeRef[bool]] = False,
        stripe: Optional[TMaybeRef[bool]] = False,
        track_color: Optional[TMaybeRef[str]] = None,
        dark: Optional[TMaybeRef[str]] = None,
        rounded: Optional[TMaybeRef[bool]] = False,
        animation_speed: Optional[TMaybeRef[int]] = 2100,
    ):
        """Literal values of parameters

        :param buffer: 0.0 < x < 1.0
        :param size: (e.g.) 16px/ 2rem/ xs/ md
        :param color: (e.g.) primary/ teal-10
        :param track_color: (e.g.) primary/ teal-10
        """
        kws = {
            "value": value,
            "size": size,
            "show_value": show_value,
            "color": color,
        }
        value_kws = convert_kws_ref2value(kws)
        element = ui.linear_progress(**value_kws)
        super().__init__(element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)

        kws_extra = {
            "indeterminate": indeterminate,
            "track_color": track_color,
            "rounded": rounded,
            "animation_speed": animation_speed,
            "reverse": reverse,
            "instant_feedback": instant_feedback,
            "buffer": buffer,
            "query": query,
            "stripe": stripe,
            "dark": dark
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
