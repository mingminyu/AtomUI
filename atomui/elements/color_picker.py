from typing import Any, Callable, Optional
from signe import effect
from nicegui import ui
from .base import SingleValueBindableUi
from ..utils.signals import ReadonlyRef, is_ref
from ..utils.signals import _TMaybeRef as TMaybeRef
from ..utils import convert_kws_ref2value


class ColorPickerBindableUi(SingleValueBindableUi[str, ui.color_picker]):
    def __init__(
        self,
        color: TMaybeRef[str] = "",
        *,
        on_pick: Optional[Callable[..., Any]] = None,
        value: TMaybeRef[bool] = False,
    ) -> None:
        kws = {
            "value": value,
            "on_pick": on_pick,
        }
        value_kws = convert_kws_ref2value(kws)

        with ui.card().tight():
            element_menu = ui.color_picker(**value_kws)
            self._element_picker = element_menu.default_slot.children[0]
            self._element_picker.props('format-model="rgba"')

            ui.button(on_click=element_menu.open, icon="colorize")

        super().__init__(color, element_menu)

        for key, value in kws.items():
            if is_ref(value) and key != "color":
                self.bind_prop(key, value)  # type: ignore

        self._ex_setup()

    def _ex_setup(self):
        ele = self._element_picker

        @effect
        def _():
            ele._props["modelValue"] = self.value

        def on_model_value_changed(e):
            self._ref.value = e.args  # type: ignore

        ele.on("update:modelValue", handler=on_model_value_changed)

    def bind_prop(self, prop: str, ref_ui: ReadonlyRef):
        if prop == "value":
            return self.bind_value(ref_ui)

        return super().bind_prop(prop, ref_ui)

    def bind_color(self, ref_ui: ReadonlyRef[str]):
        @effect
        def _():
            self._element_picker._props["modelValue"] = ref_ui.value

        return self

    def bind_value(self, ref_ui: ReadonlyRef[bool]):
        @effect
        def _():
            self._element_picker._props["value"] = ref_ui.value

        return self


class ColorPickerLazyBindableUi(ColorPickerBindableUi):
    def __init__(
        self,
        color: TMaybeRef[str] = "",
        *,
        on_pick: Optional[Callable[..., Any]] = None,
        value: TMaybeRef[bool] = False,
    ) -> None:
        super().__init__(color, on_pick=on_pick, value=value)

    def _ex_setup(self):
        ele = self._element_picker

        # @effect
        # def _():
        #     ele._props["modelValue"] = self.value

        def on_model_value_changed(e):
            self._ref.value = e.args

        ele.on("change", handler=on_model_value_changed)
