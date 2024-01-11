import asyncio
from nicegui import ui
from signe import effect
from ..utils import convert_kws_ref2value
from ..utils.signals import ReadonlyRef, is_ref
from ..utils.signals import _TMaybeRef as TMaybeRef
from .base import SingleValueBindableUi


class HtmlBindableUi(SingleValueBindableUi[str, ui.html]):
    @staticmethod
    def _setup_(binder: "HtmlBindableUi"):
        first = True

        @effect
        def _():
            nonlocal first

            async def task():
                pass
                await ui.run_javascript(
                    f"getElement({binder.element.id}).innerText= '{binder.value}' ",
                    respond=False,
                )

            if not first:
                asyncio.run(task())
            else:
                first = False

    def __init__(
        self,
        content: TMaybeRef[str] = "",
    ) -> None:
        kws = {
            "content": content,
        }
        value_kws = convert_kws_ref2value(kws)
        element = ui.html(**value_kws)
        super().__init__(content, element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)  # type: ignore

        HtmlBindableUi._setup_(self)

    def bind_prop(self, prop: str, ref_ui: ReadonlyRef):
        if prop == "color":
            return self.bind_color(ref_ui)

        return super().bind_prop(prop, ref_ui)

    def bind_color(self, ref_ui: ReadonlyRef):
        @effect
        def _():
            self.element._style["color"] = ref_ui.value
            ref_ui.value.update()
