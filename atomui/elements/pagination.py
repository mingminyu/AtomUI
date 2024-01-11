from nicegui import ui
from signe import effect
from typing import Any, Callable, Optional, Union
from .base import SingleValueBindableUi, _bind_color
from ..utils.signals import ReadonlyRef, is_ref
from ..utils.signals import _TMaybeRef as TMaybeRef
from ..utils import convert_kws_ref2value


class PaginationBindableUi(SingleValueBindableUi[str, ui.pagination]):
    def __init__(
        self,
        *,
        min: TMaybeRef[int],
        max: TMaybeRef[int],
        direction_links: Optional[TMaybeRef[bool]] = False,
        value: Optional[TMaybeRef[int]] = ...,
        on_change: Optional[Callable[..., Any]] = None,
        input: Optional[TMaybeRef[bool]] = False,
        icon_prev: Optional[TMaybeRef[str]] = None,
        icon_next: Optional[TMaybeRef[str]] = None,
        icon_first: Optional[TMaybeRef[str]] = None,
        icon_last: Optional[TMaybeRef[str]] = None,
        to_fn: Optional[Callable[..., Any]] = None,
        boundary_links: Optional[TMaybeRef[bool]] = False,
        boundary_numbers: Optional[TMaybeRef[bool]] = False,
        ellipses: Optional[TMaybeRef[bool]] = False,
        max_pages: Optional[TMaybeRef[Union[str, int]]] = 0,
        disable: Optional[TMaybeRef[bool]] = False,
        dark: Optional[TMaybeRef[bool]] = False,
        size: Optional[TMaybeRef[str]] = None,
        flat: Optional[TMaybeRef[bool]] = False,
        outline: Optional[TMaybeRef[bool]] = False,
        unelevated: Optional[TMaybeRef[bool]] = False,
        push: Optional[TMaybeRef[bool]] = False,
        color: Optional[TMaybeRef[str]] = None,
        text_color: Optional[TMaybeRef[str]] = None,
        active_design: Optional[TMaybeRef[str]] = None,
        active_color: Optional[TMaybeRef[str]] = "primary",
        active_text_color: Optional[TMaybeRef[str]] = None,
        round: Optional[TMaybeRef[bool]] = False,
        rounded: Optional[TMaybeRef[bool]] = False,
        glossy: Optional[TMaybeRef[bool]] = False,
        gutter: Optional[TMaybeRef[str]] = '2px',
        padding: Optional[TMaybeRef[str]] = None,
        input_class: Optional[TMaybeRef[str]] = None,
        ripple: Optional[TMaybeRef[bool]] = True,
    ):
        kws = {
            "min": min,
            "max": max,
            "direction_links": direction_links,
            "value": value,
            "on_change": on_change,
        }
        value_kws = convert_kws_ref2value(kws)
        element = ui.pagination(**value_kws)
        super().__init__(element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)

        kws_extra = {
            "input": input,
            "icon-prev": icon_prev,
            "icon-next": icon_next,
            "icon-first": icon_first,
            "icon-last": icon_last,
            "to-fn": to_fn,
            "boundary-links": boundary_links,
            "boundary-numbers": boundary_numbers,
            "ellipses": ellipses,
            "max-pages": max_pages,
            "disable": disable,
            "dark": dark,
            "size": size,
            "flat": flat,
            "rounded": rounded,
            "glossy": glossy,
            "gutter": gutter,
            "padding": padding,
            "input-class": input_class,
            "ripple": ripple,
            "outline": outline,
            "unelevated": unelevated,
            "push": push,
            "color": color,
            "text-color": text_color,
            "active-design": active_design,
            "active-color": active_color,
            "active-text-color": active_text_color,
            "round": round,
        }

        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value

    def bind_prop(self, prop: str, ref_ui: ReadonlyRef):
        if prop == "value":
            return self.bind_value(ref_ui)

        elif prop == "color":
            return self.bind_color(ref_ui)

        return super().bind_prop(prop, ref_ui)

    def bind_value(self, ref_ui: ReadonlyRef):
        @effect
        def _():
            self.element.set_value(str(ref_ui.value))
            self.element.update()

        return self

    def bind_color(self, ref_ui: ReadonlyRef):
        return _bind_color(self, ref_ui)

