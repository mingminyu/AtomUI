# coding: utf8
import asyncio
from typing import Any, Callable, Optional, Literal, Union
from ..utils.signals import ReadonlyRef, is_ref
from ..utils.signals import _TMaybeRef as TMaybeRef
from signe import effect
from .base import SingleValueBindableUi, _bind_color
from ..utils import convert_kws_ref2value

from nicegui.events import ClickEventArguments, handle_event
from nicegui.elements.mixins.color_elements import BackgroundColorElement
from nicegui.elements.mixins.disableable_element import DisableableElement
from nicegui.elements.mixins.text_element import TextElement

# user add for this chip element


class Chip(TextElement, DisableableElement, BackgroundColorElement):

    def __init__(
            self,
            text: str = '',
            *,
            on_click: Optional[Callable[..., Any]] = None,
            on_remove: Optional[Callable[..., Any]] = None,
            color: Optional[str] = 'primary',
            icon: Optional[str] = None,
    ) -> None:
        """Chip

        This element is based on Quasar's `QBtn <https://quasar.dev/vue-components/chip>`_ component.
        """
        super().__init__(tag='q-chip', text=text, background_color=color)

        if icon:
            self._props['icon'] = icon

        if on_click:
            self.on('click', lambda _: handle_event(on_click, ClickEventArguments(sender=self, client=self.client)), [])

        if on_remove:
            self.on('remove', lambda _: self.set_visibility(False))

    def _text_to_model_text(self, text: str) -> None:
        self._props['label'] = text

    async def clicked(self) -> None:
        """Wait until the button is clicked."""
        event = asyncio.Event()
        self.on('click', event.set, [])
        await self.client.connected()
        await event.wait()


class ChipBindableUi(SingleValueBindableUi[str, Chip]):
    def __init__(
        self,
        text: TMaybeRef[str] = "",
        *,
        on_click: Optional[Callable[..., Any]] = None,
        on_remove: Optional[Callable[..., Any]] = None,
        color: Optional[TMaybeRef[str]] = "primary",
        icon: Optional[TMaybeRef[str]] = None,
        class_: Optional[TMaybeRef[str]] = None,
        clickable: Optional[TMaybeRef[bool]] = True,
        dense: Optional[TMaybeRef[bool]] = False,
        disable: Optional[TMaybeRef[bool]] = False,
        icon_right: Optional[TMaybeRef[str]] = None,
        outline: Optional[TMaybeRef[bool]] = False,
        removable: Optional[TMaybeRef[bool]] = False,
        square: Optional[TMaybeRef[bool]] = False,
        size: Optional[TMaybeRef[str]] = None,
        selected: Optional[TMaybeRef[bool]] = False,
        text_color: Optional[TMaybeRef[str]] = None,
        title: Optional[TMaybeRef[str]] = None,
    ):
        kws = {
            "text": text,
            "color": color,
            "icon": icon,
            "on_click": on_click,
            "on_remove": on_remove,
        }
        value_kws = convert_kws_ref2value(kws)
        element = Chip(**value_kws)
        super().__init__(text, element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)  # type: ignore

        kws_extra = {
            "class": class_,
            "clickable": clickable,
            "disable": disable,
            "dense": dense,
            "outline": outline,
            "icon-right": icon_right,
            "removable": removable,
            "size": size,
            "square": square,
            "selected": selected,
            "title": title,
            "text-color": text_color,
        }

        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value

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
