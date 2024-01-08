from typing import Any, Callable, List, Optional, Dict, Union
from typing_extensions import Literal
from nicegui import ui
from signe import effect
from ..utils.signals import ReadonlyRef, is_ref
from ..utils.signals import _TMaybeRef as TMaybeRef
from .base import SingleValueBindableUi
from ..utils import convert_kws_ref2value
from atomui import webui


class InputBindableUi(SingleValueBindableUi[str, ui.input]):
    def __init__(
            self,
            label: Optional[TMaybeRef[str]] = None,
            *,
            placeholder: Optional[TMaybeRef[str]] = None,
            value: TMaybeRef[str] = "",
            password: TMaybeRef[bool] = False,
            password_toggle_button: TMaybeRef[bool] = False,
            on_change: Optional[Callable[..., Any]] = None,
            autocomplete: Optional[TMaybeRef[List[str]]] = None,
            validation: Dict[str, Callable[..., bool]] = None,
            color: Optional[TMaybeRef[str]] = None,
            label_color: Optional[TMaybeRef[str]] = None,
            bg_color: Optional[TMaybeRef[str]] = None,
            filled: Optional[TMaybeRef[bool]] = False,
            hint: Optional[TMaybeRef[str]] = None,
            outlined: Optional[TMaybeRef[bool]] = False,
            flat: Optional[TMaybeRef[bool]] = False,
            dense: Optional[TMaybeRef[bool]] = False,
            standout: Union[TMaybeRef[bool], TMaybeRef[str]] = False,
            borderless: Optional[TMaybeRef[bool]] = False,
            rounded: Optional[TMaybeRef[bool]] = False,
            square: Optional[TMaybeRef[bool]] = False,
            stack_label: Optional[TMaybeRef[bool]] = False,
            bottom_slots: Optional[TMaybeRef[bool]] = False,
            counter: Optional[TMaybeRef[bool]] = False,
            max_length: Optional[TMaybeRef[str]] = None,
            readonly: Optional[TMaybeRef[bool]] = False,
            disable: Optional[TMaybeRef[bool]] = False,
            dark: Optional[TMaybeRef[bool]] = False,
            input_class: Optional[TMaybeRef[str]] = None,
            input_style: Optional[TMaybeRef[str]] = None,
            clearable: Optional[TMaybeRef[bool]] = False,
            clear_icon: Optional[TMaybeRef[str]] = None,
            input_type: Optional[TMaybeRef[str]] = None,
            prefix: Optional[TMaybeRef[str]] = None,
            suffix: Optional[TMaybeRef[str]] = None,
            shadow_text: Optional[TMaybeRef[str]] = None,
            autogrow: Optional[TMaybeRef[bool]] = False,
            autofocus: Optional[TMaybeRef[bool]] = False,
            debounce: Optional[TMaybeRef[str]] = None,
            loading: Optional[TMaybeRef[bool]] = False,
            mask: Optional[TMaybeRef[str]] = None,
            fill_mask: Optional[Union[TMaybeRef[bool], TMaybeRef[str]]] = False,
            reverse_fill_mask: Optional[TMaybeRef[bool]] = False,
            unmasked_value: Optional[TMaybeRef[bool]] = False,
            label_slot: Optional[TMaybeRef[bool]] = False,
            hide_hint: Optional[TMaybeRef[bool]] = False,
            hide_bottom_space: Optional[TMaybeRef[bool]] = False,
            item_aligned: Optional[TMaybeRef[bool]] = False,
            rules: Optional[TMaybeRef[List]] = None,
            reactive_rules: Optional[TMaybeRef[str]] = False,
            lazy_rules: Optional[TMaybeRef[Union[str, bool]]] = False,
            for_: Optional[TMaybeRef[str]] = None,
            error_message: Optional[TMaybeRef[str]] = None,
            no_error_icon: Optional[TMaybeRef[bool]] = False,
            left_icon: Optional[TMaybeRef[str]] = None,
            right_icon: Optional[TMaybeRef[str]] = None,
            left_icon_kwargs: Optional[TMaybeRef[Dict]] = None,
            right_icon_kwargs: Optional[TMaybeRef[Dict]] = None,
    ) -> None:
        if validation is None:
            validation = {}

        if left_icon_kwargs is None:
            left_icon_kwargs = {}

        if right_icon_kwargs is None:
            right_icon_kwargs = {}

        kws = {
            "label": label,
            "placeholder": placeholder,
            "value": value,
            "password": password,
            "password_toggle_button": password_toggle_button,
            "autocomplete": autocomplete,
            "validation": validation,
            "on_change": on_change,
        }

        value_kws = convert_kws_ref2value(kws)
        element = ui.input(**value_kws)
        super().__init__(value, element)

        for key, value in kws.items():
            if is_ref(value) and key != "value":
                self.bind_prop(key, value)  # type: ignore

        kws_extra = {
            "autogrow": autogrow,
            "autofocus": autofocus,
            "bg-color": bg_color,
            "bottom-slots": bottom_slots,
            "borderless": borderless,
            "color": color,
            "counter": counter,
            "clearable": clearable,
            "clear-icon": clear_icon,
            "debounce": debounce,
            "dense": dense,
            "disable": disable,
            "dark": dark,
            "error-message": error_message,
            "filled": filled,
            "flat": flat,
            "fill-mask": fill_mask,
            "for": for_,
            "hint": hint,
            "hide-hint": hide_hint,
            "hide-bottom-space": hide_bottom_space,
            "input-class": input_class,
            "input-style": input_style,
            "item_aligned": item_aligned,
            "label-color": label_color,
            "label-slot": label_slot,
            "lazy-rules": lazy_rules,
            "loading": loading,
            "maxlength": max_length,
            "mask": mask,
            "no-error-icon": no_error_icon,
            "type": input_type,
            "outlined": outlined,
            "prefix": prefix,
            "rules": rules,
            "reactive-rules": reactive_rules,
            "readonly": readonly,
            "reverse-fill-mask": reverse_fill_mask,
            "suffix": suffix,
            "standout": standout,
            "stack-label": stack_label,
            "shadow-text": shadow_text,
            "unmasked-value": unmasked_value,
            "square": square,
            "rounded": rounded
        }

        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value

        if left_icon:
            left_icon = (
                "img:" + left_icon
                if left_icon.startswith("http") or left_icon.startswith("static")
                else left_icon
            )

            left_icon_slot_type = left_icon_kwargs.get("slot_type", "prepend")
            left_icon_type = left_icon_kwargs.get("type", "icon")
            left_icon_color = left_icon_kwargs.get("color", "white")
            # left_icon_round = left_icon_kwargs.get("round", False)
            left_icon_flat = left_icon_kwargs.get("flat", False)
            left_icon_dense = left_icon_kwargs.get("dense", False)
            left_icon_size = left_icon_kwargs.get("size")

            with self.element.add_slot(left_icon_slot_type):
                if left_icon_type == "avatar":
                    ui.avatar(left_icon, color=left_icon_color, size=left_icon_size)
                elif left_icon_type == "button":
                    webui.button(
                        icon=left_icon,
                        color=left_icon_color,
                        size=left_icon_size,
                        flat=left_icon_flat,
                        dense=left_icon_dense
                               )
                else:
                    ui.icon(left_icon)

        if right_icon:
            right_icon = (
                "img:" + right_icon
                if right_icon.startswith("http") or right_icon.startswith("static")
                else right_icon
            )

            right_icon_slot_type = right_icon_kwargs.get("slot_type", "prepend")
            right_icon_type = right_icon_kwargs.get("type", "icon")
            right_icon_color = right_icon_kwargs.get("color", "white")
            # right_icon_round = right_icon_kwargs.get("round", False)
            right_icon_flat = right_icon_kwargs.get("flat", False)
            right_icon_dense = right_icon_kwargs.get("dense", False)
            right_icon_size = right_icon_kwargs.get("size")

            with self.element.add_slot(right_icon_slot_type):
                if right_icon_type == "avatar":
                    ui.avatar(right_icon, color=right_icon_color, size=right_icon_size)
                elif right_icon_type == "button":
                    webui.button(
                        icon=right_icon,
                        color=right_icon_color,
                        size=right_icon_size,
                        flat=right_icon_flat,
                        dense=right_icon_dense
                               )
                else:
                    ui.icon(right_icon)

        self._ex_setup()

    def _ex_setup(self):
        ele = self.element

        @effect
        def _():
            ele.value = self.value

        def on_model_value_changed(e):
            self._ref.value = e.args or ""  # type: ignore

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


class LazyInputBindableUi(InputBindableUi):
    def __init__(
        self,
        label: Optional[TMaybeRef[str]] = None,
        *,
        placeholder: Optional[TMaybeRef[str]] = None,
        value: TMaybeRef[str] = "",
        password: TMaybeRef[bool] = False,
        password_toggle_button: TMaybeRef[bool] = False,
        on_change: Optional[Callable[..., Any]] = None,
        autocomplete: Optional[TMaybeRef[List[str]]] = None,
        validation: Dict[str, Callable[..., bool]] = {},
    ) -> None:
        super().__init__(
            label,
            placeholder=placeholder,
            value=value,
            password=password,
            password_toggle_button=password_toggle_button,
            on_change=on_change,
            autocomplete=autocomplete,
            validation=validation,
        )

    def _ex_setup(self):
        ele = self.element

        @effect
        def _():
            ele.value = self.value

        def on_value_changed():
            self._ref.value = ele.value or ""

        ele.on("blur", on_value_changed)
        ele.on("keyup.enter", on_value_changed)
