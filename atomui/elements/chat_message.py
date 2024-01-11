from nicegui import ui
from typing import Optional, List, Union

from .base import SingleValueBindableUi
from ..utils.signals import ReadonlyRef, is_ref
from ..utils.signals import _TMaybeRef as TMaybeRef
from ..utils import convert_kws_ref2value


class ChatMessageBindableUi(SingleValueBindableUi[str, ui.chat_message]):
    def __init__(
        self,
        text: TMaybeRef[Union[str, List[str]]] = ...,
        *,
        name: Optional[TMaybeRef[str]] = None,
        label: Optional[TMaybeRef[str]] = None,
        stamp: Optional[TMaybeRef[str]] = None,
        avatar: Optional[TMaybeRef[str]] = None,
        sent: Optional[TMaybeRef[bool]] = False,
        text_html: Optional[TMaybeRef[bool]] = False,
        bg_color: Optional[TMaybeRef[str]] = None,
        text_color: Optional[TMaybeRef[str]] = None,
        size: Optional[TMaybeRef[str]] = None,
        label_html: Optional[TMaybeRef[bool]] = False,
        name_html: Optional[TMaybeRef[bool]] = False,
        stamp_html: Optional[TMaybeRef[bool]] = False,
    ):
        """Literal values of parameters

        :param bg_color: (e.g.) primary/ teal-10
        :param text_color: (e.g.) primary/ teal-10
        :param size: (e.g.) 4/ 6/ 12
        """
        kws = {
            "text": text,
            "name": name,
            "label": label,
            "stamp": stamp,
            "avatar": avatar,
            "sent": sent,
            "text_html": text_html
        }
        value_kws = convert_kws_ref2value(kws)
        element = ui.chat_message(**value_kws)
        super().__init__(element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)

        kws_extra = {
            "bg-color": bg_color,
            "text-color": text_color,
            "size": size,
            "label-html": label_html,
            "name-html": name_html,
            "stamp-html": stamp_html,
        }
        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value

    def bind_prop(self, prop: str, ref_ui: ReadonlyRef):
        return super().bind_prop(prop, ref_ui)
