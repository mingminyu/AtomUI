from typing import Any, Callable, List, Optional
from typing import TypeVar, cast, Dict, Union
from signe import effect
from nicegui import ui
from nicegui.elements.mixins.value_element import ValueElement

from .base import SingleValueBindableUi
from ..utils.signals import ReadonlyRef, is_ref
from ..utils.signals import _TMaybeRef as TMaybeRef
from ..utils import convert_kws_ref2value

T = TypeVar("T")


"""对应 ex4nicegui/nicegui 的 radio 组件"""


class RadioBindableUi(SingleValueBindableUi[bool, ui.radio]):
    @staticmethod
    def _setup_(binder: "RadioBindableUi"):
        def on_value_changed(e):
            binder._ref.value = binder.element.options[e.args]

        @effect
        def _():
            binder.element.value = binder.value

        binder.element.on("update:modelValue", handler=on_value_changed)

    def __init__(
        self,
        options: Union[TMaybeRef[List], TMaybeRef[Dict]],
        *,
        value: TMaybeRef[Any] = None,
        on_change: Optional[Callable[..., Any]] = None,
        keep_color: TMaybeRef[bool] = None,
        left_label: TMaybeRef[bool] = None,
        disable: TMaybeRef[bool] = None,
        size: TMaybeRef[str] = None,
        color: TMaybeRef[str] = "primary",
        dark: TMaybeRef[bool] = False,
        dense: TMaybeRef[bool] = False,
        readonly: TMaybeRef[bool] = False,
        inline: TMaybeRef[bool] = False,
        type_: TMaybeRef[str] = None,
    ) -> None:
        kws = {"options": options, "value": value, "on_change": on_change}
        value_kws = convert_kws_ref2value(kws)
        element = ui.radio(**value_kws)
        super().__init__(value, element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)

        kws_extra = {
            "color": color,
            "disable": disable,
            "dark": dark,
            "dense": dense,
            "keep-color": keep_color,
            "left-label": left_label,
            "readonly": readonly,
            "size": size,
            "inline": inline,
            "type": type_
        }

        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value

        RadioBindableUi._setup_(self)

    def bind_prop(self, prop: str, ref_ui: ReadonlyRef):
        if prop == "value":
            return self.bind_value(ref_ui)

        if prop == "options":
            return self.bind_options(ref_ui)

        return super().bind_prop(prop, ref_ui)

    def bind_options(self, ref_ui: ReadonlyRef):
        @effect
        def _():
            self.element.options = ref_ui.value
            self.element.update()

        return self

    def bind_value(self, ref_ui: ReadonlyRef):
        @effect
        def _():
            cast(ValueElement, self.element).set_value(ref_ui.value)

        return self
