from nicegui import ui
from nicegui.elements.menu import MenuItem
from signe import effect
from typing import Any, Callable, Optional, List, Union

from ..utils.signals import ReadonlyRef, is_ref
from ..utils.signals import _TMaybeRef as TMaybeRef
from .base import BindableUi, SingleValueBindableUi
from ..utils import convert_kws_ref2value


class MenuBindableUi(BindableUi[ui.menu]):
    def __init__(
            self,
            value: Optional[TMaybeRef[bool]] = False,
            *,
            anchor: Optional[TMaybeRef[str]] = None,
            auto_close: Optional[TMaybeRef[bool]] = False,
            cover: Optional[TMaybeRef[bool]] = False,
            context_menu: Optional[TMaybeRef[bool]] = False,
            dark: Optional[TMaybeRef[bool]] = False,
            fit: Optional[TMaybeRef[bool]] = False,
            max_height: Optional[TMaybeRef[str]] = None,
            max_width: Optional[TMaybeRef[str]] = None,
            no_parent_event: Optional[TMaybeRef[bool]] = False,
            no_route_dismiss: Optional[TMaybeRef[bool]] = False,
            no_focus: Optional[TMaybeRef[bool]] = False,
            no_refocus: Optional[TMaybeRef[bool]] = False,
            offset: Optional[List[int]] = None,
            persistent: Optional[TMaybeRef[bool]] = None,
            square: Optional[TMaybeRef[bool]] = False,
            self_: Optional[TMaybeRef[str]] = None,
            scroll_target: Optional[TMaybeRef[str]] = None,
            target: Optional[TMaybeRef[Union[str, bool]]] = None,
            touch_position: Optional[TMaybeRef[bool]] = None,
            transition_show: Optional[TMaybeRef[str]] = None,
            transition_hide: Optional[TMaybeRef[str]] = None,
            transition_duration: Optional[Union[str, int]] = 300
    ) -> None:
        kws = {"value": value}
        value_kws = convert_kws_ref2value(kws)
        element = ui.menu(**value_kws)
        super().__init__(element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)

        kws_extra = {
            "anchor": anchor,
            "auto-close": auto_close,
            "cover": cover,
            "context-menu": context_menu,
            "dark": dark,
            "fit": fit,
            "max-height": max_height,
            "max-width": max_width,
            "no-parent-event": no_parent_event,
            "no-route-dismiss": no_route_dismiss,
            "no-focus": no_focus,
            "no-refocus": no_refocus,
            "offset": offset,
            "persistent": persistent,
            "square": square,
            "scroll-target": scroll_target,
            "self": self_,
            "target": target,
            "touch-position": touch_position,
            "transition-show": transition_show,
            "transition-hide": transition_hide,
            "transition-duration": transition_duration
        }

        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value

    def bind_prop(self, prop: str, ref_ui: ReadonlyRef):
        return super().bind_prop(prop, ref_ui)

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



class MenuItemBindableUi(BindableUi[ui.menu_item]):
    def __init__(
            self,
            text: str = '',
            on_click: Optional[Callable[..., Any]] = None,
            *,
            auto_close: Optional[TMaybeRef[bool]] = True,
            active: Optional[TMaybeRef[bool]] = False,
            clickable: Optional[TMaybeRef[bool]] = False,
            disable: Optional[TMaybeRef[bool]] = False,
            dark: Optional[TMaybeRef[bool]] = False,
            dense: Optional[TMaybeRef[bool]] = False,
            focused: Optional[TMaybeRef[bool]] = False,
            manual_focus: Optional[TMaybeRef[bool]] = False,
            insert_level: Optional[TMaybeRef[int]] = None
    ):
        kws = {
            "text": text,
            "on_click": on_click,
            "auto_close": auto_close
        }
        value_kws = convert_kws_ref2value(kws)
        element = ui.menu_item(**value_kws)
        super().__init__(element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)

        kws_extra = {
            "active": active,
            "clickable": clickable,
            "disable": disable,
            "dark": dark,
            "dense": dense,
            "focused": focused,
            "manual-focus": manual_focus,
            "insert-level": insert_level
        }

        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value

    def bind_prop(self, prop: str, ref_ui: ReadonlyRef):
        return super().bind_prop(prop, ref_ui)
