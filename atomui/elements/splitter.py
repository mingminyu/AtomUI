from nicegui import ui
from signe import effect
from typing import Any, Callable, Optional, Tuple, Literal
from .base import BindableUi, _bind_color
from ..utils.signals import ReadonlyRef, is_ref
from ..utils.signals import _TMaybeRef as TMaybeRef
from ..utils import convert_kws_ref2value


class SplitterBindableUi(BindableUi[ui.splitter]):
    def __init__(
        self,
        *,
        horizontal: Optional[TMaybeRef[bool]] = False,
        reverse: Optional[TMaybeRef[bool]] = False,
        limits: Optional[TMaybeRef[Tuple[float, float]]] = (0, 100),
        value: Optional[TMaybeRef[float]] = 50,
        on_change: Optional[Callable[..., Any]] = None,
        unit: Optional[TMaybeRef[str]] = '%',
        emit_immediately: Optional[TMaybeRef[bool]] = False,
        disable: Optional[TMaybeRef[bool]] = False,
        before_class: Optional[TMaybeRef[str]] = None,
        after_class: Optional[TMaybeRef[str]] = None,
        seperator_class: Optional[TMaybeRef[str]] = None,
        seperator_style: Optional[TMaybeRef[str]] = None,
        dark: Optional[TMaybeRef[bool]] = False,
    ):
        kws = {
            "horizontal": horizontal,
            "reverse": reverse,
            "limits": limits,
            "value": value,
            "on_change": on_change
        }
        value_kws = convert_kws_ref2value(kws)
        element = ui.splitter(**value_kws)
        super().__init__(element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)

        kws_extra = {
            "unit": unit,
            "emit-immediately": emit_immediately,
            "disable": disable,
            "before-class": before_class,
            "after-class": after_class,
            "seperator-class": seperator_class,
            "seperator-style": seperator_style,
            "dark": dark,
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

    def bind_value(self, ref_ui: ReadonlyRef):
        @effect
        def _():
            self.element.set_value(str(ref_ui.value))
            self.element.update()

        return self

