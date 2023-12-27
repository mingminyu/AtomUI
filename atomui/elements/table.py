# coding: utf8
from typing import Any, Callable, List, Optional, Dict, cast, Union
from typing_extensions import Literal
from ..utils import common as utils_common
from signe import effect
from nicegui import ui
from .base import BindableUi
from ..utils.signals import ReadonlyRef, is_ref, ref_computed
from ..utils.signals import to_ref
from ..utils.signals import _TMaybeRef as TMaybeRef
from ..utils import convert_kws_ref2value


class TableBindableUi(BindableUi[ui.table]):
    def __init__(
        self,
        columns: TMaybeRef[List[Dict]],
        rows: TMaybeRef[List[Dict]],
        row_key: TMaybeRef[str] = "id",
        title: Optional[TMaybeRef[str]] = None,
        selection: Optional[TMaybeRef[Literal["single", "multiple"]]] = None,
        pagination: Optional[TMaybeRef[int]] = 15,
        on_select: Optional[Callable[..., Any]] = None,
        fullscreen: Optional[TMaybeRef[bool]] = False,
        no_route_fullscreen_exit: Optional[TMaybeRef[bool]] = False,
        virtual_scroll_target: Optional[Union[TMaybeRef[str], ui.element]] = None,
        virtual_scroll_sticky_size_start: Optional[Union[TMaybeRef[str], TMaybeRef[int]]] = None,
        virtual_scroll_sticky_size_end: Optional[Union[TMaybeRef[str], TMaybeRef[int]]] = None,
        grid: Optional[TMaybeRef[bool]] = False,
        grid_header: Optional[TMaybeRef[bool]] = False,
        loading: Optional[TMaybeRef[bool]] = False,
        visible_columns: Optional[TMaybeRef[List]] = None,
        table_colspan: Optional[Union[TMaybeRef[str], TMaybeRef[int]]] = None,
        icon_first_page: Optional[TMaybeRef[str]] = None,
        icon_prev_page: Optional[TMaybeRef[str]] = None,
        icon_next_page: Optional[TMaybeRef[str]] = None,
        icon_last_page: Optional[TMaybeRef[str]] = None,
        hide_header: Optional[TMaybeRef[bool]] = False,
        hide_bottom: Optional[TMaybeRef[bool]] = False,
        hide_selected_banner: Optional[TMaybeRef[bool]] = False,
        hide_no_data: Optional[TMaybeRef[bool]] = False,
        hide_pagination: Optional[TMaybeRef[bool]] = False,
        separator: Optional[TMaybeRef[Literal['horizontal', 'vertical', 'cell', 'None']]] = "horizontal",
        wrap_cells: Optional[TMaybeRef[bool]] = False,
        no_data_label: Optional[TMaybeRef[str]] = None,
        no_results_label: Optional[TMaybeRef[str]] = None,
        loading_label: Optional[TMaybeRef[str]] = None,
        expanded: Optional[TMaybeRef[List]] = None,
        filter_: Optional[TMaybeRef[str]] = None,
        rows_per_page_label: Optional[TMaybeRef[str]] = None,
        rows_per_page_options: Optional[TMaybeRef[List]] = None,
        selected: Optional[TMaybeRef[List]] = None,
        binary_state_sort: Optional[TMaybeRef[bool]] = False,
        column_sort_order: Optional[TMaybeRef[str]] = None,
        color: Optional[TMaybeRef[str]] = None,
        dense: Optional[TMaybeRef[bool]] = False,
        dark: Optional[TMaybeRef[bool]] = False,
        flat: Optional[TMaybeRef[bool]] = False,
        bordered: Optional[TMaybeRef[bool]] = False,
        square: Optional[TMaybeRef[bool]] = False,
        table_style: Optional[Union[TMaybeRef[str], TMaybeRef[List]]] = None,
        table_header_style: Optional[Union[TMaybeRef[str], TMaybeRef[List]]] = None,
        table_class: Optional[Union[TMaybeRef[str], TMaybeRef[List]]] = None,
        table_header_class: Optional[Union[TMaybeRef[str], TMaybeRef[List]]] = None,
        card_container_class: Optional[Union[TMaybeRef[str], TMaybeRef[List]]] = None,
        card_style: Optional[Union[TMaybeRef[str], TMaybeRef[List]]] = None,
        card_class: Optional[Union[TMaybeRef[str], TMaybeRef[List]]] = None,
        title_class: Optional[Union[TMaybeRef[str], TMaybeRef[List]]] = None,
        virtual_scroll: Optional[TMaybeRef[bool]] = False,
        virtual_scroll_slice_size: Optional[Union[TMaybeRef[int], TMaybeRef[int]]] = False,
        virtual_scroll_slice_ratio_before: Optional[Union[TMaybeRef[int], TMaybeRef[int]]] = False,
        virtual_scroll_slice_ratio_after: Optional[Union[TMaybeRef[int], TMaybeRef[int]]] = False,
        virtual_scroll_item_size: Optional[Union[TMaybeRef[int], TMaybeRef[int]]] = False,
        # pagination_label: Optional[Callable[..., Any]] = None,
        # filter_method: Optional[Callable[..., Any]] = None,
        # selected_rows_label: Optional[Callable[..., Any]] = None,
        # sort_method: Optional[Callable[..., Any]] = None,
    ) -> None:
        kws = {
            "columns": columns,
            "rows": rows,
            "row_key": row_key,
            "title": title,
            "selection": selection,
            "pagination": pagination,
            "on_select": on_select,
        }
        value_kws = convert_kws_ref2value(kws)
        element = ui.table(**value_kws)
        super().__init__(element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)  # type: ignore

        self._arg_selection = selection
        self._arg_row_key = row_key
        self._selection_ref: Optional[ReadonlyRef[List[Any]]] = None

        kws_extra = {
            "fullscreen": fullscreen,
            "no-route-fullscreen-exit": no_route_fullscreen_exit,
            "virtual-scroll-target": virtual_scroll_target,
            "virtual_scroll_sticky_size_start": virtual_scroll_sticky_size_start,
            "virtual_scroll_sticky_size_end": virtual_scroll_sticky_size_end,
            "grid": grid,
            "grid-header": grid_header,
            "loading": loading,
            "visible-columns": visible_columns,
            "table-colspan": table_colspan,
            "icon-first-page": icon_first_page,
            "icon-prev-page": icon_prev_page,
            "icon-next-page": icon_next_page,
            "icon-last-page": icon_last_page,
            "hide-header": hide_header,
            "hide-bottom": hide_bottom,
            "hide-selected-banner": hide_selected_banner,
            "hide-no-data": hide_no_data,
            "hide-pagination": hide_pagination,
            "separator": separator,
            "wrap-cells": wrap_cells,
            "no-data-label": no_data_label,
            "no-results-label": no_results_label,
            "loading-label": loading_label,
            "expanded": expanded,
            "filter": filter_,
            "rows-per-page-label": rows_per_page_label,
            "rows-per-page-options": rows_per_page_options,
            "selected": selected,
            "binary-state-sort": binary_state_sort,
            "column-sort-order": column_sort_order,
            "color": color,
            "dense": dense,
            "dark": dark,
            "flat": flat,
            "bordered": bordered,
            "square": square,
            "table-style": table_style,
            "table-header-style": table_header_style,
            "table-class": table_class,
            "table-header-class": table_header_class,
            "card-container-class": card_container_class,
            "card-style": card_style,
            "card-class": card_class,
            "title-class": title_class,
            "virtual-scroll": virtual_scroll,
            "virtual-scroll-slice-size": virtual_scroll_slice_size,
            "virtual-scroll-slice-ratio-before": virtual_scroll_slice_ratio_before,
            "virtual-scroll-slice-ratio-after": virtual_scroll_slice_ratio_after,
            "virtual-scroll-item-size": virtual_scroll_item_size,
        }

        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value


    @property
    def selection_ref(self):
        if self._selection_ref is None:
            self._selection_ref = to_ref([])

            def on_select(_):
                self._selection_ref.value = self.element.selected  # type: ignore

            self.element.on("selection", on_select)

        return cast(ReadonlyRef[List[Any]], self._selection_ref)

    @staticmethod
    def from_pandas(
        df: TMaybeRef,
        *,
        columns_define_fn: Optional[Callable[[str], Dict]] = None,
        row_key="id",
        title: Optional[TMaybeRef[str]] = None,
        selection: Optional[TMaybeRef[Literal["single", "multiple"]]] = None,
        pagination: Optional[TMaybeRef[int]] = 15,
        on_select: Optional[Callable[..., Any]] = None,
    ):
        columns_define_fn = columns_define_fn or (lambda x: {})
        other_kws = {
            "row_key": row_key,
            "title": title,
            "selection": selection,
            "pagination": pagination,
            "on_select": on_select,
        }

        if is_ref(df):

            @ref_computed
            def cp_convert_df():
                return utils_common.convert_dataframe(df.value)

            @ref_computed
            def cp_rows():
                return cp_convert_df.value.to_dict("records")

            @ref_computed
            def cp_cols():
                return [
                    {
                        **{
                            "name": col,
                            "label": col,
                            "field": col,
                        },
                        **columns_define_fn(col),
                    }
                    for col in cp_convert_df.value.columns
                ]

            return TableBindableUi(cp_cols, cp_rows, **other_kws)

        df = utils_common.convert_dataframe(df)
        rows = df.to_dict("records")

        cols = [
            {
                **{
                    "name": col,
                    "label": col,
                    "field": col,
                },
                **columns_define_fn(col),
            }
            for col in df.columns
        ]
        return TableBindableUi(cols, rows, **other_kws)

    def bind_prop(self, prop: str, ref_ui: ReadonlyRef):
        if prop == "dataframe":
            return self.bind_dataframe(ref_ui)

        if prop == "rows":
            return self.bind_rows(ref_ui)

        if prop == "columns":
            return self.bind_columns(ref_ui)

        return super().bind_prop(prop, ref_ui)

    def bind_dataframe(self, ref_df: ReadonlyRef):
        @ref_computed
        def cp_converted_df():
            df = ref_df.value
            return utils_common.convert_dataframe(df)

        @ref_computed
        def cp_rows():
            return cp_converted_df.value.to_dict("records")

        @ref_computed
        def cp_cols():
            return [
                {
                    "name": col,
                    "label": col,
                    "field": col,
                }
                for col in cp_converted_df.value.columns
            ]

        self.bind_rows(cp_rows).bind_columns(cp_cols)

        return self

    def bind_rows(self, ref_ui: ReadonlyRef[List[Dict]]):
        @effect
        def _():
            ele = self.element
            ele._props["rows"] = ref_ui.value
            ele.update()

        return self

    def bind_columns(self, ref_ui: ReadonlyRef[List[Dict]]):
        @effect
        def _():
            ele = self.element
            ele._props["columns"] = ref_ui.value
            ele.update()

        return self
