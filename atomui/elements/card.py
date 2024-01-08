from nicegui import ui
from typing import Optional, Literal, Callable, Any
from .base import BindableUi
from ..utils.signals import ReadonlyRef, is_ref, effect, ref_computed, to_ref
from ..utils.signals import _TMaybeRef as TMaybeRef
from ..utils.click import FreeClick
from .button import ButtonBindableUi
from .input import InputBindableUi
from .menu import MenuBindableUi, MenuItemBindableUi


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
        horizontal: Optional[TMaybeRef[bool]] = False,
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

    def bind_bg_color(self, ref_ui: ReadonlyRef):
        @effect
        def _():
            self.element.classes(replace=ref_ui.value)
            self.element.update()

        return self


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


class ChatEditCard(CardBindableUi):
    """ChatGPT 风格的编辑卡片，用于侧边栏展示"""
    def __init__(
        self,
        title: Optional[TMaybeRef[str]] = "default",
        on_click: Optional[Callable[..., Any]] = None,
        on_dblclick: Optional[Callable[..., Any]] = None,
        show_input: Optional[TMaybeRef[bool]] = to_ref(False),
        chat_id: Optional[str] = None,
        curr_chat_id: Optional[TMaybeRef[str]] = None,
    ):
        super().__init__(flat=True)
        self.sess_id = chat_id
        self.__click_callback: Optional[Callable[[], None]] = None
        self.__dblclick_callback: Optional[Callable[[], None]] = None

        with self.tight().classes('w-full justify-around bg-slate-700 h-8 gap-0 py-0 cursor-pointer'):
            # chat-card 为自定义类名
            active_card_css = ref_computed(
                lambda: "chat-card bg-red-2 pl-1"
                if curr_chat_id.value == f"/c/{chat_id}" else "chat-card bg-blue-2 pl-1"
            )
            self.card_sec = CardSectionBindableUi(horizontal=True).classes("chat-card w-full h-8 gap-0 py-0 pl-1")
            self.card_sec.bind_bg_color(active_card_css)

            with self.card_sec:
                self._btn = ButtonBindableUi(
                    title, text_color='white', no_caps=True, flat=True, shape='square', align='left',
                ).classes('w-48 self-start h-8 text-left text-light bg-grey-6 text-[12px]').props('square')
                show_btn = ref_computed(lambda: not show_input.value)
                self._btn.bind_visible(show_btn)

                self._input = InputBindableUi(
                    value=title, dense=True, color="grey-6", flat=True, square=True,
                    bg_color='grey-6', input_class="text-white", clear_icon='close',
                    standout="text-white", clearable=True
                ).classes('w-48 h-8 text-xs gap-0')
                self._input.bind_visible(show_input)

                self._card_options = ButtonBindableUi(
                    color="white", size='sm', icon='more_horiz', no_caps=True, flat=True, shape='square'
                ).classes('w-8 self-start h-8 rounded-r bg-grey-6')
                with self._card_options:
                    with MenuBindableUi(dense=True, flat=True).classes('text-xs gap-0 items-center self-center'):
                        MenuItemBindableUi('Rename', dense=True, flat=True).classes('self-center text-center p-2.5')
                        MenuItemBindableUi('Delete', dense=True, flat=True).classes('self-center text-center p-2.5')

                self._btn.element.bind_text(self._input, 'value')


            disable_class = "pointer-events-none bg-grey-6"

            def disable_input():
                self._input.classes(disable_class)

            # 焦点离开或按回车，输入框就禁用吧
            self._input.on("blur", disable_input).on(
                "keyup.enter", lambda: (show_input.set_value(False), self._input.element.run_method("blur"))
            )

        fc = FreeClick().apply(self)

        @fc.on_click
        def _():
            if on_click:
                on_click()

        @fc.on_dblclick
        def _():
            show_input.value = True
            if on_dblclick:
                on_dblclick()

            self._input.element.run_method("focus")
    @property
    def title(self):
        return self._input.value

