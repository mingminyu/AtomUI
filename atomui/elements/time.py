from nicegui import ui
from typing import Any, Callable, Optional
from .base import SingleValueBindableUi
from ..utils.signals import ReadonlyRef, is_ref
from ..utils.signals import _TMaybeRef as TMaybeRef
from ..utils import convert_kws_ref2value


class TimeBindableUi(SingleValueBindableUi[str, ui.time]):
    def __init__(
        self,
        value: Optional[TMaybeRef[str]] = None,
        *,
        mask: str = 'HH:mm',
        on_change: Optional[Callable[..., Any]] = None,
        name: Optional[TMaybeRef[str]] = None,
        landscape: Optional[TMaybeRef[bool]] = False,
        format24h: Optional[TMaybeRef[bool]] = False,
        hour_options: Optional[TMaybeRef[str]] = None,
        minute_options: Optional[TMaybeRef[str]] = None,
        second_options: Optional[TMaybeRef[str]] = None,
        with_seconds: Optional[TMaybeRef[bool]] = False,
        now_btn: Optional[TMaybeRef[bool]] = False,
        calendar: Optional[TMaybeRef[str]] = None,
        default_value: Optional[TMaybeRef[str]] = None,
        readonly: Optional[TMaybeRef[bool]] = False,
        dark: Optional[TMaybeRef[bool]] = False,
        square: Optional[TMaybeRef[bool]] = False,
        flat: Optional[TMaybeRef[bool]] = False,
        bordered: Optional[TMaybeRef[bool]] = False,
        disable: Optional[TMaybeRef[bool]] = False,
        color: Optional[TMaybeRef[str]] = None,
        text_color: Optional[TMaybeRef[str]] = None,
        # options / locale
    ):
        """

        :param value:
        :param mask:
        :param on_change:
        :param name:
        :param landscape:
        :param format24h:
        :param hour_options:
        :param minute_options:
        :param second_options:
        :param with_seconds:
        :param now_btn:
        :param calendar: gregorian/ persian
        :param default_value: (e.g.) 1939/10/01. default is current day

        """
        kws = {
            "value": value,
            "mask": mask,
            "on_change": on_change,
        }
        value_kws = convert_kws_ref2value(kws)
        element = ui.time(**value_kws)
        super().__init__(element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)

        kws_extra = {
            "name": name,
            "landscape": landscape,
            "format24h": format24h,
            "hour_options": hour_options,
            "minute_options": minute_options,
            "second_options": second_options,
            "with_seconds": with_seconds,
            "now_btn": now_btn,
            "calendar": calendar,
            "default_value": default_value,
            "readonly": readonly,
            "dark": dark,
            "square": square,
            "flat": flat,
            "text": text_color,
            "color": color,
            "bordered": bordered,
            "disable": disable,
        }
        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value

    def bind_prop(self, prop: str, ref_ui: ReadonlyRef):
        return super().bind_prop(prop, ref_ui)
