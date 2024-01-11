from nicegui import ui
from typing import Optional, Callable, Any

from .base import SingleValueBindableUi
from ..utils.signals import ReadonlyRef, is_ref
from ..utils.signals import _TMaybeRef as TMaybeRef
from ..utils import convert_kws_ref2value


class ScrollAreaBindable(SingleValueBindableUi[str, ui.scroll_area]):
    def __init__(
        self,
        *,
        on_scroll: Optional[Callable[..., Any]] = None,
        visible: Optional[TMaybeRef[bool]] = True,
        delay: Optional[TMaybeRef[int]] = 1000,
        dark: Optional[TMaybeRef[bool]] = False,
        bar_style: Optional[TMaybeRef[str]] = None,
        vertical_bar_style: Optional[TMaybeRef[str]] = None,
        horizontal_bar_style: Optional[TMaybeRef[str]] = None,
        thumb_style: Optional[TMaybeRef[str]] = None,
        vertical_thumb_style: Optional[TMaybeRef[str]] = None,
        horizontal_thumb_style: Optional[TMaybeRef[str]] = None,
        content_style: Optional[TMaybeRef[str]] = None,
        content_active_style: Optional[TMaybeRef[str]] = None,

    ):
        kws = {"on_scroll": on_scroll}
        value_kws = convert_kws_ref2value(kws)
        element = ui.scroll_area(**value_kws)
        super().__init__(element)

        kws_extra = {
            "visible": visible,
            "delay": delay,
            "dark": dark,
            "bar_style": bar_style,
            "vertical_bar_style": vertical_bar_style,
            "horizontal_bar_style": horizontal_bar_style,
            "thumb_style": thumb_style,
            "vertical_thumb_style": vertical_thumb_style,
            "horizontal_thumb_style": horizontal_thumb_style,
            "content_style": content_style,
            "content_active_style": content_active_style,
        }
        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value

    def bind_prop(self, prop: str, ref_ui: ReadonlyRef):
        return super().bind_prop(prop, ref_ui)