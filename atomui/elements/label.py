from signe import effect
from nicegui import ui
from .base import SingleValueBindableUi
from ..utils.signals import ReadonlyRef, is_ref
from ..utils.signals import _TMaybeRef as TMaybeRef
from ..utils import convert_kws_ref2value


class LabelBindableUi(SingleValueBindableUi[str, ui.label]):
    @staticmethod
    def _setup_(binder: "LabelBindableUi"):
        def on_value_changed(e):
            binder._ref.value = e.args["label"]

        @effect
        def _():
            binder.element.text = binder.value

        binder.element.on("update:modelValue", handler=on_value_changed)

    def __init__(
        self,
        text: TMaybeRef[str] = "",
    ) -> None:
        kws = {
            "text": text,
        }
        value_kws = convert_kws_ref2value(kws)
        element = ui.label(**value_kws)
        super().__init__(text, element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)

        LabelBindableUi._setup_(self)

    def bind_prop(self, prop: str, ref_ui: ReadonlyRef):
        if prop == "text":
            return self.bind_text(ref_ui)

        if prop == "color":
            return self.bind_color(ref_ui)

        return super().bind_prop(prop, ref_ui)

    def bind_color(self, ref_ui: ReadonlyRef):
        @effect
        def _():
            self.element._style["color"] = ref_ui.value
            self.element.update()

    def bind_text(self, ref_ui: ReadonlyRef):
        @effect
        def _():
            self.element.set_text(str(ref_ui.value))
            self.element.update()

        return self
