# coding: utf8
from nicegui import ui
from .base import BindableUi


class CardBindableUi(BindableUi[ui.card]):
    def __init__(self) -> None:
        element = ui.card()
        super().__init__(element)

    def tight(self):
        """Removes padding and gaps between nested elements."""
        self.element._classes.clear()
        self.element._style.clear()
        return self


class CardSectionBindableUi(BindableUi[ui.card_section]):
    def __init__(
        self,
    ) -> None:
        element = ui.card_section()
        super().__init__(element)


class CardActionsBindableUi(BindableUi[ui.card_actions]):
    def __init__(
        self,
    ) -> None:
        element = ui.card_actions()
        super().__init__(element)
