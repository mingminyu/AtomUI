from nicegui import ui
from typing import Any, Callable, Optional
from .base import SingleValueBindableUi
from ..utils.signals import ReadonlyRef, is_ref
from ..utils.signals import _TMaybeRef as TMaybeRef
from ..utils import convert_kws_ref2value


class EditorBindableUi(SingleValueBindableUi[str, ui.editor]):
    def __init__(
        self,
        placeholder: Optional[TMaybeRef[str]] = None,
        value: Optional[TMaybeRef[str]] = '',
        on_change: Optional[Callable[..., Any]] = None,
        fullscreen: Optional[TMaybeRef[bool]] = False,
        no_route_fullscreen_exit: Optional[TMaybeRef[bool]] = False,
        paragraph_tag: Optional[TMaybeRef[str]] = None,
        readonly: Optional[TMaybeRef[bool]] = False,
        disable: Optional[TMaybeRef[bool]] = False,
        square: Optional[TMaybeRef[bool]] = False,
        flat: Optional[TMaybeRef[bool]] = False,
        dense: Optional[TMaybeRef[bool]] = False,
        dark: Optional[TMaybeRef[bool]] = False,
        min_height: Optional[TMaybeRef[str]] = "10rem",
        max_height: Optional[TMaybeRef[str]] = "10rem",
        height: Optional[TMaybeRef[str]] = "10rem",
        toolbar_outline: Optional[TMaybeRef[bool]] = False,
        toolbar_push: Optional[TMaybeRef[bool]] = False,
        toolbar_rounded: Optional[TMaybeRef[bool]] = False,
        content_style: Optional[TMaybeRef[str]] = None,
        content_class: Optional[TMaybeRef[str]] = None,
        fonts: Optional[TMaybeRef[str]] = None,
        toolbar: Optional[TMaybeRef[str]] = None,
        toolbar_color: Optional[TMaybeRef[str]] = None,
        toolbar_text_color: Optional[TMaybeRef[str]] = None,
        toolbar_toggle_color: Optional[TMaybeRef[str]] = None,
        toolbar_bg: Optional[TMaybeRef[str]] = None,
        definitions = None
    ):
        """

        :param paragraph_tag: div/ p
        :param height: (e.g.) 100px / 50vh
        :param min_height: (e.g.) 15rem / 50vh
        :param max_height: (e.g.) 1000px / 90vh
        :param content_class: (e.g.) my-special-class/ {"my-special-class": <condition>}
        :param fonts: (e.g.) not use frequent
        :param toolbar: (e.g.) left,center,right,justify
        :param toolbar_bg: (e.g.) secondary/ blue-3; default is grey-3
        """
        kws = {
            "placeholder": placeholder,
            "value": value,
            "on_change": on_change
        }
        value_kws = convert_kws_ref2value(kws)
        element = ui.editor(**value_kws)
        super().__init__(element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)

        kws_extra = {
            "fullscreen": fullscreen,
            "toolbar": toolbar,
            "toolbar_text_color": toolbar_text_color,
            "toolbar_bg": toolbar_bg,
            "toolbar_outline": toolbar_outline,
            "toolbar_push": toolbar_push,
            "toolbar_rounded": toolbar_rounded,
            "no_route_fullscreen_exit": no_route_fullscreen_exit,
            "paragraph_tag": paragraph_tag,
            "readonly": readonly,
            "disable": disable,
            "square": square,
            "flat": flat,
            "dense": dense,
            "dark": dark,
            "min_height": min_height,
            "max_height": max_height,
            "height": height,
            "content_style": content_style,
            "content_class": content_class,
            "fonts": fonts,
            "definitions": definitions,
        }
        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value

    def bind_prop(self, prop: str, ref_ui: ReadonlyRef):
        return super().bind_prop(prop, ref_ui)
