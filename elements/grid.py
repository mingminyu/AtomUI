# coding: utf8
from typing import Optional
from ..utils import convert_kws_ref2value

from nicegui import ui
from .base import BindableUi
from ..utils.signals import is_ref
from ..utils.signals import _TMaybeRef as TMaybeRef


class GridBindableUi(BindableUi[ui.grid]):
    def __init__(
        self,
        rows: Optional[TMaybeRef[int]] = None,
        columns: Optional[TMaybeRef[int]] = None,
    ) -> None:
        kws = {
            "rows": rows,
            "columns": columns,
        }
        value_kws = convert_kws_ref2value(kws)
        element = ui.grid(**value_kws)

        super().__init__(element)
        for key, value in kws.items():
            if value is not None and is_ref(value):
                self.bind_prop(key, value)