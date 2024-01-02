from nicegui import ui
from typing import List, Dict
from signe import effect
from ..utils import common as utils_common
from ..utils.signals import ReadonlyRef
from ..utils.signals import is_ref
from ..utils.signals import ref_computed
from ..utils.signals import _TMaybeRef as TMaybeRef
from ..utils import convert_kws_ref2value
from .base import BindableUi


class AgGridBindableUi(BindableUi[ui.aggrid]):
    def __init__(
        self,
        options: TMaybeRef[Dict],
        *,
        html_columns: TMaybeRef[List[int]] = [],
        theme: TMaybeRef[str] = "balham",
        **org_kws
    ) -> None:
        kws = {
            "options": options,
            "html_columns": html_columns,
            "theme": theme,
        }
        value_kws = convert_kws_ref2value(kws)
        element = ui.aggrid(**value_kws, **org_kws)
        super().__init__(element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)  # type: ignore

    @staticmethod
    def from_pandas(df: TMaybeRef, **org_kws):
        if is_ref(df):

            @ref_computed
            def cp_convert_df():
                return utils_common.convert_dataframe(df.value)

            @ref_computed
            def cp_options():
                column_defs_ = [
                    {"headerName": col, "field": col}
                    for col in cp_convert_df.value.columns
                ]
                row_data_ = cp_convert_df.value.to_dict("records")
                data = {"columnDefs": column_defs_, "rowData": row_data_}
                return data

            return AggridBindableUi(cp_options, **org_kws)

        column_defs = [{"headerName": col, "field": col} for col in df.columns]  # type: ignore
        row_data = df.to_dict("records")  # type: ignore
        options = {"columnDefs": column_defs, "rowData": row_data}
        return AggridBindableUi(options, **org_kws)

    def bind_prop(self, prop: str, ref_ui: ReadonlyRef):
        if prop == "options":
            return self.bind_options(ref_ui)

        return super().bind_prop(prop, ref_ui)

    def bind_options(self, ref_ui: ReadonlyRef[List[Dict]]):
        @effect
        def _():
            ele = self.element
            data = ref_ui.value
            ele._props["options"].update(data)
            ele.update()

        return self

