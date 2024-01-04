from nicegui import ui
from typing import Optional, Literal
from ..utils.signals import ReadonlyRef, is_ref
from ..utils.signals import _TMaybeRef as TMaybeRef
from .base import BindableUi


class CardBindableUi(BindableUi[ui.card]):
    def __init__(
            self,
            dark: Optional[TMaybeRef[bool]] = False,
            square: Optional[TMaybeRef[bool]] = False,
            flat: Optional[TMaybeRef[bool]] = False,
            bordered: Optional[TMaybeRef[bool]] = False
    ):
        element = ui.card()
        super().__init__(element)

        kws_extra = {
            "dark": dark,
            "square": square,
            "flat": flat,
            "bordered": bordered,
        }

        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value

    def tight(self):
        """Removes padding and gaps between nested elements."""
        self.element._classes.clear()
        self.element._style.clear()
        return self

    def bind_prop(self, prop: str, ref_ui: ReadonlyRef):
        return super().bind_prop(prop, ref_ui)


class CardSectionBindableUi(BindableUi[ui.card_section]):
    def __init__(
        self,
        horizontal: Optional[TMaybeRef[bool]] = False
    ) -> None:
        element = ui.card_section()
        super().__init__(element)

        kws_extra = {
            "horizontal": horizontal,
        }

        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value

    def bind_prop(self, prop: str, ref_ui: ReadonlyRef):
        return super().bind_prop(prop, ref_ui)


_CARD_ACTIONS_ALIGNMENT = Literal['left', 'center', 'right', 'between', 'around', 'evenly', 'stretch']


class CardActionsBindableUi(BindableUi[ui.card_actions]):
    def __init__(
        self,
        align: Optional[TMaybeRef[_CARD_ACTIONS_ALIGNMENT]] = None,
        vertical: Optional[TMaybeRef[bool]] = False
    ) -> None:
        element = ui.card_actions()
        super().__init__(element)

        kws_extra = {
            "align": align,
            "vertical": vertical,
        }

        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value

    def bind_prop(self, prop: str, ref_ui: ReadonlyRef):
        return super().bind_prop(prop, ref_ui)
