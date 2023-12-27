# coding: utf8
from typing_extensions import Literal
from signe import effect
from nicegui import ui
from nicegui.page_layout import Drawer
from .base import SingleValueBindableUi
from ..utils.signals import to_value, is_ref
from ..utils.signals import _TMaybeRef as TMaybeRef
from ..utils import convert_kws_ref2value


_TDrawerSide = Literal["left", "right"]


class DrawerBindableUi(SingleValueBindableUi[bool, Drawer]):
    def __init__(
            self,
            side: _TDrawerSide = "left",
            *,
            value: TMaybeRef[bool] = True,
            fixed: TMaybeRef[bool] = False,
            bordered: TMaybeRef[bool] = True,
            elevated: TMaybeRef[bool] = False,
            top_corner: TMaybeRef[bool] = False,
            bottom_corner: TMaybeRef[bool] = False,
            show_if_above: TMaybeRef[bool] = False,
            overlay: TMaybeRef[bool] = False,
            min_width: TMaybeRef[str] = "60",
            width: TMaybeRef[str] = None,
            mini: TMaybeRef[bool] = False,
            mini_to_overlay: TMaybeRef[bool] = False,
    ) -> None:
        kws = {
            "value": value,
            "fixed": fixed,
            "bordered": bordered,
            "elevated": elevated,
            "top_corner": top_corner,
            "bottom_corner": bottom_corner,
        }
        value_kws = convert_kws_ref2value(kws)

        ele = None
        if to_value(side) == "left":
            ele = ui.left_drawer(**value_kws)
        else:
            ele = ui.right_drawer(**value_kws)

        init_value = ele._props["model-value"] if "model-value" in ele._props else ele._props["show-if-above"]
        super().__init__(init_value, ele)

        kws_extra = {
            "show_if_above": show_if_above,
            "overlay": overlay,
            "width": width,
            "mini": mini,
            "mini_to_overlay": mini_to_overlay,
            "min-width": min_width,
        }

        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value

        @effect
        def _():
            value_ = "true" if self.value else "false"
            ele.props(f":model-value={value_}")

        def on_update(e):
            self._ref.value = e.args

        ele.on("update:modelValue", on_update)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)  # type: ignore

    def toggle(self):
        self.element.toggle()
        return self
