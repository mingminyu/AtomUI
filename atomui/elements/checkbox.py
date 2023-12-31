from typing import Any, Callable, Optional, TypeVar, cast
from signe import effect
from nicegui import ui
from nicegui.elements.mixins.value_element import ValueElement
from .base import SingleValueBindableUi
from ..utils.signals import ReadonlyRef, is_ref
from ..utils.signals import _TMaybeRef as TMaybeRef
from ..utils import convert_kws_ref2value


T = TypeVar("T")


class CheckboxBindableUi(SingleValueBindableUi[bool, ui.checkbox]):
    @staticmethod
    def _setup_(binder: "CheckboxBindableUi"):
        ele = cast(ValueElement, binder.element)

        def on_value_changed(e):
            binder._ref.value = e.args[0]  # type: ignore

        @effect
        def _():
            ele.value = binder.value

        ele.on("update:modelValue", handler=on_value_changed)

    def __init__(
        self,
        text: TMaybeRef[str] = "",
        *,
        value: TMaybeRef[bool] = False,
        on_change: Optional[Callable[..., Any]] = None,
        indeterminate_value: Optional[Any] = None,
        toggle_order: Optional[TMaybeRef[str]] = "tf",
        checked_icon: Optional[TMaybeRef[str]] = None,
        unchecked_icon: Optional[TMaybeRef[str]] = None,
        indeterminate_icon: Optional[TMaybeRef[str]] = None,
        label: Optional[TMaybeRef[str]] = None,
        left_label: Optional[TMaybeRef[bool]] = None,
        disable: Optional[TMaybeRef[bool]] = False,
        size: Optional[TMaybeRef[str]] = None,
        color: Optional[TMaybeRef[str]] = None,
        dark: Optional[TMaybeRef[str]] = None,
        dense: Optional[TMaybeRef[bool]] = False,
    ) -> None:
        kws = {"text": text, "value": value, "on_change": on_change}
        value_kws = convert_kws_ref2value(kws)
        element = ui.checkbox(**value_kws)
        super().__init__(value, element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)

        kws_extra = {
            "indeterminate-value": indeterminate_value,
            "checked-icon": checked_icon,
            "unchecked-icon": unchecked_icon,
            "indeterminate-icon": indeterminate_icon,
            "label": label,
            "left-label": left_label,
            "disable": disable,
            "size": size,
            "color": color,
            "dark": dark,
            "dense": dense,
            "toggle-order": toggle_order
        }

        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value

        CheckboxBindableUi._setup_(self)

    def bind_prop(self, prop: str, ref_ui: ReadonlyRef):
        if prop == "value":
            return self.bind_value(ref_ui)

        return super().bind_prop(prop, ref_ui)

    def bind_value(self, ref_ui: ReadonlyRef[bool]):
        @effect
        def _():
            self.element.on_value_change(ref_ui.value)

        return self
