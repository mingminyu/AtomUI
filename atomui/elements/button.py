from signe import effect
from nicegui import ui
from typing import Any, Callable, Optional, Literal, Union
from ..utils.signals import ReadonlyRef, is_ref
from ..utils.signals import _TMaybeRef as TMaybeRef
from .base import SingleValueBindableUi, _bind_color
from ..utils import convert_kws_ref2value


_BUTTON_ALIGNMENT = Literal['left', 'right', 'around', 'between', 'evenly']


class ButtonBindableUi(SingleValueBindableUi[str, ui.button]):
    def __init__(
            self,
            text: TMaybeRef[str] = "",
            *,
            on_click: Optional[Callable[..., Any]] = None,
            color: Optional[TMaybeRef[str]] = "primary",
            icon: Optional[TMaybeRef[str]] = None,
            icon_right: Optional[TMaybeRef[str]] = None,
            text_color: Optional[TMaybeRef[str]] = None,
            glossy: Optional[TMaybeRef[bool]] = False,
            flat: Optional[TMaybeRef[bool]] = False,
            dense: Optional[TMaybeRef[bool]] = False,
            stack: Optional[TMaybeRef[bool]] = False,
            outline: Optional[TMaybeRef[bool]] = False,
            shape: Optional[TMaybeRef[Literal['round', 'rounded', 'square']]] = None,
            unelevated: Optional[TMaybeRef[bool]] = False,
            no_caps: Optional[TMaybeRef[bool]] = False,
            no_wrap: Optional[TMaybeRef[bool]] = False,
            push: Optional[TMaybeRef[bool]] = False,
            size: Optional[TMaybeRef[str]] = None,
            align: Optional[TMaybeRef[_BUTTON_ALIGNMENT]] = None,
            stretch: Optional[TMaybeRef[bool]] = False,
            padding: Optional[TMaybeRef[str]] = None,
            loading: Optional[TMaybeRef[bool]] = False,
            percentage: Optional[TMaybeRef[int]] = None,
            dark_percentage: Optional[TMaybeRef[bool]] = False,
            disabled: Optional[TMaybeRef[bool]] = False,
            fab: Optional[TMaybeRef[bool]] = False,
            fab_mini: Optional[TMaybeRef[bool]] = False,
            ripple: Optional[TMaybeRef[bool]] = False,
            loading_icon: Optional[TMaybeRef[str]] = None,
            loading_icon_color: Optional[Union[TMaybeRef[str], str]] = "primary",
            loading_text: Optional[TMaybeRef[str]] = None,
            loading_icon_left: Optional[TMaybeRef[bool]] = False,
            to: Optional[TMaybeRef[str]] = None,
            href: Optional[TMaybeRef[str]] = None,
            new_tab: Optional[TMaybeRef[bool]] = False,
    ) -> None:
        kws = {
            "text": text,
            "color": color,
            "icon": icon,
            "on_click": on_click,
        }
        value_kws = convert_kws_ref2value(kws)
        element = ui.button(**value_kws)
        super().__init__(text, element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)  # type: ignore

        kws_extra = {
            "align": align,
            "dark-percentage": dark_percentage,
            "disabled": disabled,
            "dense": dense,
            "flat": flat,
            "fab": fab,
            "glossy": glossy,
            "fab-mini": fab_mini,
            "icon-right": icon_right,
            "loading": loading,
            "no-caps": no_caps,
            "no-wrap": no_wrap,
            "outline": outline,
            "percentage": percentage,
            "padding": padding,
            "push": push,
            "ripple": ripple,
            "stack": stack,
            "size": size,
            "stretch": stretch,
            "text-color": text_color,
            "unelevated": unelevated,
            "to": to,
            "href": href,
            "new-tab": new_tab
        }

        if shape is not None:
            kws_extra.update({shape: True})

        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value

        if loading_icon_left and loading_icon and loading_text:
            self.element.add_slot('loading', f'''
                <q-spinner-{loading_icon} color="{loading_icon_color}" class="on-left"/>
                {loading_text}
                ''')
        elif loading_icon and loading_text:
            with self.element.add_slot('loading', loading_text):
                ui.spinner(loading_icon, color=loading_icon_color)
        elif loading_icon:
            with self.element.add_slot('loading'):
                ui.spinner(loading_icon, color=loading_icon_color)
        elif loading_text:
            self.element.add_slot('loading', loading_text)

    def bind_prop(self, prop: str, ref_ui: ReadonlyRef):
        if prop == "text":
            return self.bind_text(ref_ui)

        if prop == "icon":
            return self.bind_icon(ref_ui)

        if prop == "color":
            return self.bind_color(ref_ui)

        return super().bind_prop(prop, ref_ui)

    def bind_color(self, ref_ui: ReadonlyRef):
        return _bind_color(self, ref_ui)

    def bind_text(self, ref_ui: ReadonlyRef):
        @effect
        def _():
            ele = self.element
            ele._props["label"] = ref_ui.value
            ele.update()

        return self

    def bind_icon(self, ref_ui: ReadonlyRef):
        @effect
        def _():
            ele = self.element
            ele._props["icon"] = ref_ui.value
            ele.update()

        return self

    def bind_enabled(self, ref_ui: ReadonlyRef[bool]):
        @effect
        def _():
            self.element.on_enabled_change(ref_ui.value)

        return self

    def bind_disable(self, ref_ui: ReadonlyRef[bool]):
        @effect
        def _():
            self.element.on_enabled_change(not ref_ui.value)

        return self
