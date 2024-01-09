from nicegui import ui
from nicegui.elements.mixins.color_elements import TextColorElement
from typing import Optional, Union, Callable, Any, cast
from .base import BindableUi, SingleValueBindableUi
from ..utils.signals import ReadonlyRef, is_ref, effect
from ..utils import convert_kws_ref2value
from ..utils.signals import _TMaybeRef as TMaybeRef


class StepBindableUi(SingleValueBindableUi[str, ui.step]):
    def __init__(
        self,
        *,
        name: Optional[TMaybeRef[str]],
        title: Optional[TMaybeRef[str]] = None,
        icon: Optional[TMaybeRef[str]] = None,
        header_nav: Optional[TMaybeRef[bool]] = False,
        caption: Optional[TMaybeRef[str]] = None,
        prefix: Optional[TMaybeRef[str]] = None,
        done_icon: Optional[TMaybeRef[str]] = None,
        done_color: Optional[TMaybeRef[str]] = None,
        active_icon: Optional[TMaybeRef[str]] = None,
        active_color: Optional[TMaybeRef[str]] = None,
        error_icon: Optional[TMaybeRef[str]] = None,
        error_color: Optional[TMaybeRef[str]] = None,
        disable: Optional[TMaybeRef[bool]] = False,
        done: Optional[TMaybeRef[bool]] = False,
        error: Optional[TMaybeRef[bool]] = False,
        color: Optional[TMaybeRef[str]] = None,
    ):
        kws = {
            "name": name,
            "title": title,
            "icon": icon,
        }
        value_kws = convert_kws_ref2value(kws)
        element = ui.step(**value_kws)
        super().__init__(element)

        kws_extra = {
            "header-nav": header_nav,
            "active-icon": active_icon,
            "active-color": active_color,
            "done-icon": done_icon,
            "done-color": done_color,
            "error-icon": error_icon,
            "error-color": error_color,
            "disable": disable,
            "done": done,
            "error": error,
            "color": color,
            "caption": caption,
            "prefix": prefix,
        }
        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value

    def bind_prop(self, prop: str, ref_ui: ReadonlyRef):
        if prop == "name":
            return self.bind_name(ref_ui)

        return super().bind_prop(prop, ref_ui)

    def bind_name(self, ref_ui: ReadonlyRef):
        @effect
        def _():
            ele = cast(TextColorElement, self.element)
            ele._props["name"] = ref_ui.value
            ele.update()

        return self


class StepperBindableUi(BindableUi[ui.stepper]):
    def __init__(
        self,
        *,
        value: TMaybeRef[Union[str, ui.step, StepBindableUi, None]] = None,
        on_value_change: Optional[Callable[..., Any]] = None,
        keep_alive: Optional[TMaybeRef[bool]] = True,
        keep_alive_include: Optional[TMaybeRef[str]] = None,
        keep_alive_exclude: Optional[TMaybeRef[str]] = None,
        keep_alive_max: Optional[TMaybeRef[int]] = None,
        animated: Optional[TMaybeRef[bool]] = False,
        infinite: Optional[TMaybeRef[bool]] = False,
        swipeable: Optional[TMaybeRef[bool]] = False,
        vertical: Optional[TMaybeRef[bool]] = False,
        header_nav: Optional[TMaybeRef[bool]] = False,
        contracted: Optional[TMaybeRef[bool]] = False,
        alternative_labels: Optional[TMaybeRef[bool]] = False,
        active_icon: Optional[TMaybeRef[str]] = None,
        active_color: Optional[TMaybeRef[str]] = None,
        inactive_icon: Optional[TMaybeRef[str]] = None,
        inactive_color: Optional[TMaybeRef[str]] = None,
        done_icon: Optional[TMaybeRef[str]] = None,
        done_color: Optional[TMaybeRef[str]] = None,
        error_icon: Optional[TMaybeRef[str]] = None,
        error_color: Optional[TMaybeRef[str]] = None,
        dark: Optional[TMaybeRef[bool]] = False,
        flat: Optional[TMaybeRef[bool]] = False,
        bordered: Optional[TMaybeRef[bool]] = False,
        header_class: Optional[TMaybeRef[str]] = None,
        transition_prev: Optional[TMaybeRef[str]] = None,
        transition_next: Optional[TMaybeRef[str]] = None,
        transition_duration: Optional[TMaybeRef[int]] = 300,
    ):
        kws = {
            "value": value,
            "on-value-change": on_value_change,
            "keep_alive": keep_alive,
        }
        value_kws = convert_kws_ref2value(kws)
        element = ui.stepper(**value_kws)
        super().__init__(element)

        kws_extra = {
            "keep-alive-include": keep_alive_include,
            "keep-alive-exclude": keep_alive_exclude,
            "keep-alive-max": keep_alive_max,
            "animated": animated,
            "infinite": infinite,
            "swipeable": swipeable,
            "vertical": vertical,
            "header-nav": header_nav,
            "contracted": contracted,
            "alternative-labels": alternative_labels,
            "active-icon": active_icon,
            "active-color": active_color,
            "inactive-icon": inactive_icon,
            "inactive-color": inactive_color,
            "done-icon": done_icon,
            "done-color": done_color,
            "error-icon": error_icon,
            "error-color": error_color,
            "dark": dark,
            "flat": flat,
            "bordered": bordered,
            "header-class": header_class,
            "transition_prev": transition_prev,
            "transition_next": transition_next,
            "transition_duration": transition_duration,
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

    def bind_value(self, ref_ui: ReadonlyRef[bool]):
        @effect
        def _():
            self.element.on_value_change(ref_ui.value)

        return self


class StepperNavigation(ui.stepper_navigation):
    ...
