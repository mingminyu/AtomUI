from nicegui import ui
from .base import BindableUi


class ColumnBindableUi(BindableUi[ui.column]):
    def __init__(
        self,
    ) -> None:
        element = ui.column()
        super().__init__(element)
