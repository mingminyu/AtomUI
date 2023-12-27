# coding: utf8
from typing import Optional, Callable, Union
from nicegui import ui
from .base import SingleValueBindableUi
from ..utils.signals import effect, is_ref
from ..utils.signals import _TMaybeRef as TMaybeRef
from ..utils import convert_kws_ref2value


class ExpansionBindableUi(SingleValueBindableUi[bool, ui.expansion]):
    def __init__(
        self,
        text: Optional[TMaybeRef[str]] = None,
        *,
        icon: Optional[TMaybeRef[str]] = None,
        value: TMaybeRef[bool] = False,
        on_value_change: Optional[Callable[..., None]] = None,
        # user add
        caption: Optional[TMaybeRef[str]] = None,
        caption_lines: Optional[TMaybeRef[Union[int, str]]] = None,
        content_insert_level: Optional[TMaybeRef[str]] = None,
        disable: Optional[TMaybeRef[bool]] = False,
        dense: Optional[TMaybeRef[bool]] = True,
        dense_toggle: Optional[TMaybeRef[bool]] = True,
        duration: Optional[TMaybeRef[str]] = None,
        default_opened: Optional[TMaybeRef[bool]] = False,
        expand_icon: Optional[TMaybeRef[str]] = None,
        expanded_icon: Optional[TMaybeRef[str]] = None,
        expand_icon_class: Optional[TMaybeRef[str]] = None,
        expand_separator: Optional[TMaybeRef[bool]] = False,
        expand_icon_toggle: Optional[TMaybeRef[bool]] = False,
        flat: Optional[TMaybeRef[bool]] = False,
        group: Optional[TMaybeRef[str]] = None,
        header_class: Optional[TMaybeRef[str]] = None,
        header_style: Optional[TMaybeRef[str]] = None,
        header_insert_level: Optional[TMaybeRef[str]] = None,
        hide_expand_icon: Optional[TMaybeRef[bool]] = False,
        label: Optional[TMaybeRef[str]] = None,
        label_lines: Optional[TMaybeRef[Union[int, str]]] = None,
        popup: Optional[TMaybeRef[bool]] = False,
        switch_toggle_side: Optional[TMaybeRef[bool]] = False,
    ) -> None:
        kws = {
            "text": text,
            "icon": icon,
            "value": value,
            "on_value_change": on_value_change,
        }
        value_kws = convert_kws_ref2value(kws)
        element = ui.expansion(**value_kws)
        super().__init__(value, element)

        for key, value in kws.items():
            if is_ref(value) and key != "value":
                self.bind_prop(key, value)  # type: ignore

        kws_extra = {
            "caption": caption,
            "content-insert-level": content_insert_level,
            "caption-lines": caption_lines,
            "disable": disable,
            "dense": dense,
            "dense-toggle": dense_toggle,
            "default-opened": default_opened,
            "duration": duration,
            "expand-separator": expand_separator,
            "expand-icon": expand_icon,
            "expanded-icon": expanded_icon,
            "expand-icon-class": expand_icon_class,
            "expand-icon-toggle": expand_icon_toggle,
            "flat": flat,
            "group": group,
            "header-insert-level": header_insert_level,
            "header-class": header_class,
            "hide-expand-icon": hide_expand_icon,
            "header-style": header_style,
            "label": label,
            "label-lines": label_lines,
            "switch-toggle-side": switch_toggle_side,
            "popup": popup,
        }
        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value

        self._ex_setup()

    def _ex_setup(self):
        ele = self.element

        @effect
        def _():
            ele.value = self.value

        def on_model_value_changed(e):
            self._ref.value = e.args

        ele.on("update:modelValue", handler=on_model_value_changed)
