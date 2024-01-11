from nicegui import ui
from typing import Optional, List, Callable, Any, Dict

from .base import SingleValueBindableUi
from ..utils.signals import ReadonlyRef, is_ref
from ..utils.signals import _TMaybeRef as TMaybeRef
from ..utils import convert_kws_ref2value


class TreeBindableUi(SingleValueBindableUi[str, ui.tree]):
    def __init__(
        self,
        nodes: List[Dict],
        *,
        node_key: Optional[TMaybeRef[str]] = 'id',
        label_key: Optional[TMaybeRef[str]] = 'label',
        children_key: Optional[TMaybeRef[str]] = 'children',
        on_select: Optional[Callable[..., Any]] = None,
        on_expand: Optional[Callable[..., Any]] = None,
        on_tick: Optional[Callable[..., Any]] = None,
        tick_strategy: Optional[TMaybeRef[str]] = None,
        no_selection_unset: Optional[TMaybeRef[bool]] = False,
        default_expand_all: Optional[TMaybeRef[bool]] = False,
        accordion: Optional[TMaybeRef[bool]] = False,
        no_transition: Optional[TMaybeRef[bool]] = False,
        icon: Optional[TMaybeRef[str]] = None,
        no_nodes_label: Optional[TMaybeRef[str]] = None,
        no_result_label: Optional[TMaybeRef[str]] = None,
        filter_: Optional[TMaybeRef[str]] = None,
        ticked: Optional[TMaybeRef[bool]] = False,
        expanded: Optional[TMaybeRef[str]] = None,
        selected: Optional[TMaybeRef[Any]] = None,
        no_connectors: Optional[TMaybeRef[bool]] = False,
        color: Optional[TMaybeRef[str]] = None,
        control_color: Optional[TMaybeRef[str]] = None,
        text_color: Optional[TMaybeRef[str]] = None,
        selected_color: Optional[TMaybeRef[str]] = None,
        dense: Optional[TMaybeRef[bool]] = False,
        dark: Optional[TMaybeRef[bool]] = False,
        duration: Optional[TMaybeRef[int]] = 300,
    ):
        """Literal value of parameters

        :param tick_strategy: leaf/ leaf-filtered/ strict
        """
        kws = {
            "nodes": nodes,
            "node_key": node_key,
            "label_key": label_key,
            "children_key": children_key,
            "on_select": on_select,
            "on_expand": on_expand,
            "on_tick": on_tick,
            "tick_strategy": tick_strategy
        }
        value_kws = convert_kws_ref2value(kws)
        element = ui.tree(**value_kws)
        super().__init__(element)

        for key, value in kws.items():
            if is_ref(value):
                self.bind_prop(key, value)

        kws_extra = {
            "no-selection-unset": no_selection_unset,
            "default-expand-all": default_expand_all,
            "accordion": accordion,
            "no-transition": no_transition,
            "icon": icon,
            "no-nodes-label": no_nodes_label,
            "no-result-label": no_result_label,
            "filter": filter_,
            "ticked": ticked,
            "expanded": expanded,
            "selected": selected,
            "no-connectors": no_connectors,
            "color": color,
            "control-color": control_color,
            "text-color": text_color,
            "selected-color": selected_color,
            "dense": dense,
            "dark": dark,
            "duration": duration,
        }
        for key, value in kws_extra.items():
            if is_ref(value):
                self.bind_prop(key, value)
            elif value:
                self.element._props[key] = value

    def bind_prop(self, prop: str, ref_ui: ReadonlyRef):
        return super().bind_prop(prop, ref_ui)