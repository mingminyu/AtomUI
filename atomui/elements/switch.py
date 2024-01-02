from typing import Any, Callable, Optional, TypeVar, cast
from signe import effect
from nicegui import ui
from nicegui.elements.mixins.value_element import ValueElement
from .base import SingleValueBindableUi
from ..utils.signals import ReadonlyRef, is_ref
from ..utils.signals import _TMaybeRef as TMaybeRef
from ..utils import convert_kws_ref2value

T = TypeVar("T")


"""对应到 ex4nicegui/nicegui 的 switch 组件"""


class SwitchBindableUi(SingleValueBindableUi[bool, ui.switch]):
    @staticmethod
    def _setup_(binder: "SwitchBindableUi"):
        def on_value_changed(e):
            ele._send_update_on_value_change = ele.LOOPBACK
            cur_value = ele._event_args_to_value(e)
            ele.set_value(cur_value)
            ele._send_update_on_value_change = True
            binder._ref.value = cur_value

        ele = cast(ValueElement, binder.element)

        @effect
        def _():
            ele.value = binder.value

        ele.on("update:modelValue", on_value_changed, [None], throttle=0)  # type: ignore

    def __init__(
        self,
        text: TMaybeRef[str] = "",
        *,
        value: TMaybeRef[bool] = False,
        on_change: Optional[Callable[..., Any]] = None,
        indeterminate_value: TMaybeRef[Any] = None,
        toggle_order: TMaybeRef[str] = None,
        toggle_indeterminate: TMaybeRef[bool] = False,
        keep_color: TMaybeRef[bool] = False,
        icon: TMaybeRef[str] = None,
        checked_icon: TMaybeRef[str] = None,
        unchecked_icon: TMaybeRef[str] = None,
        indeterminate_icon: TMaybeRef[str] = None,
        label: TMaybeRef[str] = None,
        left_label: TMaybeRef[bool] = None,
        val: TMaybeRef[Any] = None,
        true_value: TMaybeRef[Any] = None,
        false_value: TMaybeRef[Any] = None,
        disable: TMaybeRef[bool] = None,
        size: TMaybeRef[str] = None,
        color: TMaybeRef[str] = "primary",
        dark: TMaybeRef[bool] = False,
        dense: TMaybeRef[bool] = False,
        icon_color: TMaybeRef[str] = None,
        readonly: TMaybeRef[bool] = False,
    ) -> None:
        kws = {"text": text, "value": value, "on_change": on_change}
        value_kws = convert_kws_ref2value(kws)
        element = ui.switch(**value_kws)
        super().__init__(value, element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)  # type: ignore

        kws_extra = {
            "color": color,
            "checked-icon":  checked_icon,
            "disable": disable,
            "dark": dark,
            "dense": dense,
            "false-value": false_value,
            "icon": icon,
            "icon-color": icon_color,
            "indeterminate-value": indeterminate_value,
            "indeterminate-icon": indeterminate_icon,
            "keep-color": keep_color,
            "label": label,
            "left-label": left_label,
            "readonly": readonly,
            "size": size,
            "toggle-order": toggle_order,
            "toggle-indeterminate": toggle_indeterminate,
            "true-value": true_value,
            "val": val,
            "unchecked-icon": unchecked_icon,
        }

        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value

        SwitchBindableUi._setup_(self)

    def bind_prop(self, prop: str, ref_ui: ReadonlyRef):
        if prop == "value":
            return self.bind_value(ref_ui)

        return super().bind_prop(prop, ref_ui)

    def bind_value(self, ref_ui: ReadonlyRef[bool]):
        @effect
        def _():
            self.element.on_value_change(ref_ui.value)

        return self
