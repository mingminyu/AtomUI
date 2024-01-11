from nicegui import ui
from typing import Optional

from .base import SingleValueBindableUi
from ..utils.signals import ReadonlyRef, is_ref
from ..utils.signals import _TMaybeRef as TMaybeRef
from ..utils import convert_kws_ref2value


class TimelineBindableUi(SingleValueBindableUi[str, ui.timeline]):
    def __init__(
        self,
        *,
        side: Optional[TMaybeRef[str]] = 'left',
        layout: Optional[TMaybeRef[str]] = 'dense',
        color: Optional[TMaybeRef[str]] = None,
        dark: Optional[TMaybeRef[bool]] = False,
    ):
        """Literal value of parameters

        :param side: left/ right
        :param layout: dense/ comfortable/ loose
        :param color: (e.g.) primary/ teal-10
        """
        kws = {
            "side": side,
            "layout": layout,
            "color": color,
        }
        value_kws = convert_kws_ref2value(kws)
        element = ui.timeline(**value_kws)
        super().__init__(element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)

        kws_extra = {"dark": dark}
        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value

    def bind_prop(self, prop: str, ref_ui: ReadonlyRef):
        return super().bind_prop(prop, ref_ui)


class TimelineEntryBindableUi(SingleValueBindableUi[str, ui.timeline_entry]):
    def __init__(
            self,
            body: Optional[str] = None,
            *,
            side: Optional[TMaybeRef[str]] = 'left',
            heading: Optional[TMaybeRef[bool]] = False,
            tag: Optional[TMaybeRef[str]] = 'h3',
            icon: Optional[TMaybeRef[str]] = None,
            avatar: Optional[TMaybeRef[str]] = None,
            title: Optional[TMaybeRef[str]] = None,
            subtitle: Optional[TMaybeRef[str]] = None,
            color: Optional[TMaybeRef[str]] = None,
    ):
        """Literal value of parameters

        :param side: left/ right
        :param tag: (e.g.) div/ span/ h1
        :param icon: (e.g.) map/ ion-add/ img:https://xxx/log.svg img:path/to/logo.png
        :param color: (e.g.) primary/ teal-10
        """
        kws = {
            "body": body,
            "side": side,
            "heading": heading,
            "tag": tag,
            "icon": icon,
            "avatar": avatar,
            "title": title,
            "subtitle": subtitle,
            "color": color,
        }
        value_kws = convert_kws_ref2value(kws)
        element = ui.timeline_entry(**value_kws)
        super().__init__(element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)

    def bind_prop(self, prop: str, ref_ui: ReadonlyRef):
        return super().bind_prop(prop, ref_ui)
