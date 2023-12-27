# coding: utf8
from typing import Any, Callable, Optional, TypeVar, cast, Union, Literal
from signe import effect
from nicegui import ui
from .base import SingleValueBindableUi
from ..utils.signals import ReadonlyRef, is_ref
from ..utils.signals import _TMaybeRef as TMaybeRef
from ..utils import convert_kws_ref2value
from .button import ButtonBindableUi


# TODO: 当前实现存在BUG，在点击Tab移除时，依旧会显示对应的TabPanel的内容


class TabBindableUi(SingleValueBindableUi[bool, ui.tab]):
    def __init__(
            self,
            name: TMaybeRef[str],
            label: Optional[TMaybeRef[TMaybeRef[str]]] = None,
            icon: Optional[TMaybeRef[str]] = None,
            alert: Optional[Union[TMaybeRef[bool], TMaybeRef[str]]] = None,
            alert_icon: Optional[TMaybeRef[str]] = None,
            no_caps: Optional[TMaybeRef[bool]] = False,
            disable: Optional[TMaybeRef[bool]] = False,
            content_class: Optional[TMaybeRef[str]] = None,
            ripple: Optional[TMaybeRef[bool]] = False,
            removable: Optional[TMaybeRef[bool]] = False,
            remove_mode: Optional[Literal['delete', 'hide']] = 'hide',
            on_remove: Optional[Callable[..., Any]] = None
    ):
        kws = {
            "name": name,
            "label": label,
            "icon": icon
        }
        element = ui.tab(**kws)
        super().__init__(name, element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)  # type: ignore

        kws_extra = {
            "alert": alert,
            "alert-icon": alert_icon,
            "no-caps": no_caps,
            "disable": disable,
            "content-class": content_class,
            "ripple": ripple
        }

        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value

        if removable:
            with self.element:
                ButtonBindableUi(
                    icon="close", flat=True, shape="round", size="6px",
                    on_click=on_remove
                )


class TabPanelBindableUi(SingleValueBindableUi[bool, ui.tab_panel]):
    def __init__(
            self,
            name: TMaybeRef[str],
            *,
            disable: Optional[TMaybeRef[bool]] = False,
            dark: Optional[TMaybeRef[bool]] = False
    ):
        kws = {
            "name": name,
        }
        value_kws = convert_kws_ref2value(kws)
        element = ui.tab_panel(**value_kws)
        super().__init__(name, element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)  # type: ignore

        kws_extra = {
            "disable": disable,
            "dark": dark,
        }

        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value


class TabsBindableUi(SingleValueBindableUi[bool, ui.tabs]):
    def __init__(
        self,
        *,
        value: TMaybeRef[Union[TabBindableUi, TabPanelBindableUi, ui.tab, ui.tab_panel, TMaybeRef[str]]] = None,
        on_change: Optional[Callable[..., Any]] = None,
        vertical: Optional[TMaybeRef[bool]] = False,
        outside_arrows: Optional[TMaybeRef[bool]] = False,
        mobile_arrows: Optional[TMaybeRef[bool]] = False,
        align: Optional[TMaybeRef[Literal['left', 'center', 'right', 'justify']]] = 'center',
        left_icon: Optional[TMaybeRef[str]] = False,
        right_icon: Optional[TMaybeRef[str]] = False,
        active_color: Optional[TMaybeRef[str]] = None,
        active_bg_color: Optional[TMaybeRef[str]] = None,
        indicator_color: Optional[TMaybeRef[str]] = None,
        content_class: Optional[TMaybeRef[str]] = None,
        active_class: Optional[TMaybeRef[str]] = None,
        dense: Optional[TMaybeRef[bool]] = False,
    ):
        kws = {
            "value": value,
            "on_change": on_change,
        }
        value_kws = convert_kws_ref2value(kws)
        element = ui.tabs(**value_kws)
        super().__init__(value, element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)  # type: ignore

        kws_extra = {
            "vertical": vertical,
            "outside-arrows": outside_arrows,
            "mobile-arrows": mobile_arrows,
            "align": align,
            "dense": dense,
            "left-icon": left_icon,
            "right-icon": right_icon,
            "active-color": active_color,
            "active-bg-color": active_bg_color,
            "indicator-color": indicator_color,
            "content-class": content_class,
            "active-class": active_class,
        }

        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value

    def bind_prop(self, prop: TMaybeRef[str], ref_ui: ReadonlyRef):
        return super().bind_prop(prop, ref_ui)

    def bind_enabled(self, ref_ui: ReadonlyRef[TMaybeRef[bool]]):
        @effect
        def _():
            self.element.on_enabled_change(ref_ui.value)

        return self

    def bind_disable(self, ref_ui: ReadonlyRef[TMaybeRef[bool]]):
        @effect
        def _():
            self.element.on_enabled_change(not ref_ui.value)

        return self

    def bind_value(self, ref_ui: ReadonlyRef):
        @effect
        def _():
            ele = self.element
            ele._props["value"] = ref_ui.value
            ele.update()

        return self


class TabPanelsBindableUi(SingleValueBindableUi[bool, ui.tab_panels]):
    def __init__(
        self,
        tabs: Union[ui.tabs, TabsBindableUi],
        *,
        value: TMaybeRef[Union[ui.tab, ui.tab_panel, TabBindableUi, TabPanelBindableUi, str, None]] = None,
        on_change: Optional[Callable[..., Any]] = None,
        animated: Optional[TMaybeRef[bool]] = True,
        keep_alive: Optional[TMaybeRef[bool]] = True,
        keep_alive_exclude: Optional[TMaybeRef[str]] = None,
        keep_alive_max: Optional[TMaybeRef[int]] = None,
        infinite: Optional[TMaybeRef[bool]] = False,
        swipeable: Optional[TMaybeRef[bool]] = False,
        vertical: Optional[TMaybeRef[bool]] = False,
        transition_prev: Optional[TMaybeRef[str]] = None,
        transition_next: Optional[TMaybeRef[str]] = None,
        transition_duration: Optional[TMaybeRef[str]] = None,
    ):
        kws = {
            "tabs": tabs,
            "value": value,
            "animated": animated,
            "keep_alive": keep_alive,
            "on_change": on_change,
        }
        value_kws = convert_kws_ref2value(kws)
        element = ui.tab_panels(**value_kws)
        super().__init__(value, element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)  # type: ignore

        kws_extra = {
            "keep-alive-exclude": keep_alive_exclude,
            "keep-alive-max": keep_alive_max,
            "infinite": infinite,
            "swipeable": swipeable,
            "vertical": vertical,
            "transition-prev": transition_prev,
            "transition-next": transition_next,
            "transition-duration": transition_duration,
        }

        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value

    def bind_prop(self, prop: TMaybeRef[str], ref_ui: ReadonlyRef):
        if prop == "tabs":
            return self.bind_tabs(ref_ui)

        return super().bind_prop(prop, ref_ui)

    def bind_enabled(self, ref_ui: ReadonlyRef[TMaybeRef[bool]]):
        @effect
        def _():
            self.element.on_enabled_change(ref_ui.value)

        return self

    def bind_disable(self, ref_ui: ReadonlyRef[TMaybeRef[bool]]):
        @effect
        def _():
            self.element.on_enabled_change(not ref_ui.value)

        return self

    def bind_tabs(self, ref_ui: ReadonlyRef):
        @effect
        def _():
            ele = self.element
            ele._props["tabs"] = ref_ui.value
            ele.update()

        return self
