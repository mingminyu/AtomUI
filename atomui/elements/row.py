from nicegui import ui
from .base import BindableUi


class RowBindableUi(BindableUi[ui.row]):
    def __init__(
        self,
    ) -> None:
        element = ui.row()
        super().__init__(element)
