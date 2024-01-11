from nicegui import ui
from signe import effect
from typing import Any, Callable, Optional, Dict

from .base import SingleValueBindableUi
from ..utils.signals import ReadonlyRef, is_ref
from ..utils.signals import _TMaybeRef as TMaybeRef
from ..utils import convert_kws_ref2value


class TextareaBindableUi(SingleValueBindableUi[str, ui.textarea]):
    def __init__(
        self,
        label: Optional[TMaybeRef[str]] = None,
        *,
        placeholder: Optional[TMaybeRef[str]] = None,
        value: TMaybeRef[str] = "",
        on_change: Optional[Callable[..., Any]] = None,
        validation: Dict[str, Callable[..., bool]] = {},
    ) -> None:
        kws = {
            "label": label,
            "placeholder": placeholder,
            "value": value,
            "validation": validation,
            "on_change": on_change,
        }
        value_kws = convert_kws_ref2value(kws)
        element = ui.textarea(**value_kws)
        super().__init__(value, element)

        for key, value in kws.items():
            if is_ref(value) and key != "value":
                self.bind_prop(key, value)

        self._ex_setup()

    def _ex_setup(self):
        ele = self.element

        @effect
        def _():
            ele.value = self.value

        def on_model_value_changed(e):
            self._ref.value = e.args  # type: ignore

        ele.on("update:modelValue", handler=on_model_value_changed)

    def bind_prop(self, prop: str, ref_ui: ReadonlyRef):
        if prop == "value":
            return self.bind_value(ref_ui)

        return super().bind_prop(prop, ref_ui)

    def bind_value(self, ref_ui: ReadonlyRef[bool]):
        @effect
        def _():
            self.element.on_value_change(ref_ui.value)

        return self


class LazyTextareaBindableUi(TextareaBindableUi):
    def __init__(
        self,
        label: Optional[TMaybeRef[str]] = None,
        *,
        placeholder: Optional[TMaybeRef[str]] = None,
        value: TMaybeRef[str] = "",
        on_change: Optional[Callable[..., Any]] = None,
        validation: Dict[str, Callable[..., bool]] = {},
    ) -> None:
        super().__init__(
            label,
            placeholder=placeholder,
            value=value,
            on_change=on_change,
            validation=validation,
        )

    def _ex_setup(self):
        ele = self.element

        @effect
        def _():
            ele.value = self.value

        def on_value_changed():
            self._ref.value = ele.value

        ele.on("blur", on_value_changed)
        ele.on("keyup.enter", on_value_changed)
