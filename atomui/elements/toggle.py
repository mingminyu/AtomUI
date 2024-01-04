from nicegui import ui
from signe import effect
from typing import Any, Callable, Optional, Literal, Union, List, Dict
from ..utils.signals import ReadonlyRef, is_ref
from ..utils.signals import _TMaybeRef as TMaybeRef
from .base import SingleValueBindableUi
from ..utils import convert_kws_ref2value


"""对应 ex4nicegui/nicegui 的 toggle 组件"""


# TODO: 未完成
class ToggleBindableUi(SingleValueBindableUi[str, ui.toggle]):
    def __int__(
            self,
            options: Union[TMaybeRef[List], TMaybeRef[Dict]],
            *,
            value: Optional[TMaybeRef[Any]] = None,
            on_change: Optional[Callable[..., Any]] = None,
            clearable: Optional[TMaybeRef[bool]] = False,
            color: Optional[TMaybeRef[str]] = None,
            disable: Optional[TMaybeRef[bool]] = False,
            dense: Optional[TMaybeRef[bool]] = False,
            flex: Optional[TMaybeRef[bool]] = False,
            flat: Optional[TMaybeRef[bool]] = False,
            glossy: Optional[TMaybeRef[bool]] = False,
            no_caps: Optional[TMaybeRef[bool]] = False,
            no_wrap: Optional[TMaybeRef[bool]] = False,
            outline: Optional[TMaybeRef[bool]] = False,
            push: Optional[TMaybeRef[bool]] = False,
            padding: Optional[TMaybeRef[str]] = None,
            readonly: Optional[TMaybeRef[bool]] = False,
            ripple: Optional[TMaybeRef[bool]] = False,
            spread: Optional[TMaybeRef[bool]] = False,
            size: Optional[TMaybeRef[str]] = None,
            stack: Optional[TMaybeRef[bool]] = False,
            stretch: Optional[TMaybeRef[bool]] = False,
            rounded: Optional[TMaybeRef[bool]] = False,
            text_color: Optional[TMaybeRef[str]] = None,
            toggle_color: Optional[TMaybeRef[str]] = "primary",
            toggle_text_color: Optional[TMaybeRef[str]] = None,
            unelevated: Optional[TMaybeRef[bool]] = False,
    ):
        kws = {
            "options": options,
            "value": value,
            "on_change": on_change,
            "clearable": clearable,
        }
        value_kws = convert_kws_ref2value(kws)
        element = ui.toggle(**value_kws)
        super().__init__(options, element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)

        kws_extra = {
            "color": color,
            "disable": disable,
            "dense": dense,
            "flex": flex,
            "flat": flat,
            "glossy": glossy,
            "no-caps": no_caps,
            "no-wrap": no_wrap,
            "outline": outline,
            "push": push,
            "padding": padding,
            "readonly": readonly,
            "ripple": ripple,
            "spread": spread,
            "size": size,
            "stack": stack,
            "stretch": stretch,
            "rounded": rounded,
            "text-color": text_color,
            "toggle-text-color": toggle_text_color,
            "toggle-color": toggle_color,
        }

        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value

    def bind_prop(self, prop: str, ref_ui: ReadonlyRef):
        return super().bind_prop(prop, ref_ui)
