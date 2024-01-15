from nicegui import ui
from uuid import uuid4, UUID
from datetime import datetime, date
from typing import List, Optional, Any, Callable, cast, Literal, Union
from nicegui.events import KeyEventArguments, GenericEventArguments, ClickEventArguments
from .footer import FooterBindableUi
from .input import InputBindableUi
from .button import ButtonBindableUi
from .drawer import DrawerBindableUi
from .card import CardBindableUi, CardSectionBindableUi
from .menu import MenuBindableUi, MenuItemBindableUi
from .chip import ChipBindableUi
from .avatar import Avatar
from .badge import BadgeBindableUi
from .header import HeaderBindableUi
from .base import BindableUi
from ..components.router import Router
from ..models.chat import ChatCardModel, ChatInfo
from ..utils.signals import ReadonlyRef, is_ref, effect, ref_computed, to_ref
from ..utils.signals import _TMaybeRef as TMaybeRef
from ..utils.click import FreeClick



def chat_main(chat_id: str):
    ui.label(chat_id)



def chat_greet():
    # 针对 `landscape`(横屏) 和 `portrait`(竖屏) 分别设置
    with ui.column().classes(
        'w-full flex justify-center items-center justify-self-center gap-0 mb-0 '
        'md:pt-[100px] lg:pt-[100px] portrait:pt-[500px]'
    ) as home_greet:
        ui.avatar(
            icon="img:/static/avatar/logo.svg", size="100px", color="white"
            )
        ui.markdown("**How can I help you today?**").classes('text-xl gap-0 mt-0')




class ChatInfoEditCard(CardBindableUi):
    """ChatGPT 风格的编辑卡片，用于侧边栏展示"""
    def __init__(
        self,
        *,
        title: Optional[TMaybeRef[str]] = "default",
        show_input: Optional[TMaybeRef[bool]] = to_ref(False),
        input_clearable: Optional[TMaybeRef[bool]] = to_ref(True),
        chat_id: Optional[Union[str, UUID]] = None,
        router: Router = None,
    ):
        super().__init__(flat=True)
        self.chat_id = chat_id
        self.chat_url = f"/chat/{chat_id}"
        self.__click_callback: Optional[Callable[[], None]] = None
        self.__dblclick_callback: Optional[Callable[[], None]] = None

        def disable_input():
            show_input.set_value(False)
            disable_class = "pointer-events-none bg-grey-6"
            self._input.classes(disable_class)
            input_clearable.value = False

        card_css = "w-40 flex bg-slate-700 h-8 gap-0 py-0 cursor-pointer"
        with self.tight().classes(card_css).props(f"chat_id='{self.chat_id}'"):
            # chat-card 为自定义类名，后面通过 add_body_html 来设置样式
            active_card_css = ref_computed(
                lambda: "chat-card bg-red-2 pl-1"
                if router.curr_path.value == self.chat_url else "chat-card bg-blue-2 pl-1"
            )
            self.card_sec = CardSectionBindableUi(horizontal=True).classes("chat-card w-full h-8 gap-0 py-0 pl-1")
            self.card_sec.bind_bg_color(active_card_css)

            with self.card_sec:
                card_btn_css = "w-48 self-start h-8 text-left text-light bg-grey-6 text-[12px]"
                self._btn = ButtonBindableUi(
                    title, text_color='white', no_caps=True, flat=True, shape='square', align='left',
                ).classes(card_btn_css)
                show_btn = ref_computed(lambda: not show_input.value)
                self._btn.bind_visible(show_btn)

                self._input = InputBindableUi(
                    value=title, dense=True, color="grey-6", flat=True, square=True,
                    bg_color='grey-6', input_class="text-white", clear_icon='close',
                    standout="text-white", clearable=input_clearable
                ).classes('w-48 h-8 text-xs gap-0')
                self._input.bind_visible(show_input)

        self._btn.element.bind_text(self._input, 'value')

        # 焦点离开或按回车，输入框就禁用吧
        self._input.on("blur", disable_input).on(
            "keyup.enter", lambda: self._input.element.run_method("blur")
        )

        fc = FreeClick().apply(self)

        @fc.on_click
        def _():
            router.open(chat_id=self.chat_id)

        @fc.on_dblclick
        def _():
            show_input.value = True
            input_clearable.value = True

            self._input.element.run_method("focus")

    def click_self(self):
        self.element.run_method('click')



class ChatInfoCard(BindableUi[ui.row]):
    def __init__(
        self,
        *,
        title: Optional[TMaybeRef[str]] = "default",
        show_input: Optional[TMaybeRef[bool]] = to_ref(False),
        input_clearable: Optional[TMaybeRef[bool]] = to_ref(True),
        chat_id: Optional[Union[str, UUID]] = None,
        router: Router = None,
    ):
        element = ui.row()
        super().__init__(element)
        self.chat_id = chat_id

        with self:
            self.chat_edit_card = ChatInfoEditCard(
                title=title, show_input=show_input, input_clearable=input_clearable,
                chat_id=chat_id, router=router
            )
            self._card_options = ButtonBindableUi(
                color="white", size='sm', icon='more_horiz',
                no_caps=True, flat=True, shape='square'
            ).classes('w-8 self-start h-8 rounded-r bg-grey-6')
            with self._card_options:
                with MenuBindableUi(dense=True, flat=True).classes('text-xs gap-0 items-center self-center'):
                    MenuItemBindableUi('Rename', dense=True, flat=True).classes('self-center text-center p-2.5')
                    MenuItemBindableUi('Delete', dense=True, flat=True).classes('self-center text-center p-2.5')


class ChatSidebar(DrawerBindableUi):
    def __init__(
        self,
        *,
        router: Router,
        chat_infos: List[ChatInfo] = None,
    ):
        super().__init__(
            side="left", value=True, top_corner=True, bottom_corner=True, fixed=True,
            bordered=True, elevated=True, overlay=False, show_if_above=False, width="256"
        )
        self._router = router

        with self.classes('bg-slate-700'):
            with ui.row().classes('w-full items-center justify-center'):
                ButtonBindableUi(
                    text="New Chat", icon="img:/static/avatar/logo.svg",
                    icon_right="edit", color="slate-700", shape="square",
                    align="between", no_caps=True, flat=True, dense=True,
                    on_click=lambda: router.open("/")
                ).classes('flex-grow w-full text-white rounded-lg w-56')

            date_tag_css = 'text-xs text-slate-400'
            container_d0 = ui.row().classes('w-full self-center flex justify-between')
            container_d1 = ui.row().classes('w-full self-center flex justify-between')
            container_d30 = ui.row().classes('w-full self-center flex justify-between')

            with container_d0:
                ui.label('Today').classes(f'w-full {date_tag_css} mt-10')

            with container_d1:
                ui.label('Yesterday').classes(date_tag_css)

            with container_d30:
                ui.label('Previous 30 Days').classes(date_tag_css)

            for chat_info in chat_infos:
                if (date.today() - chat_info.date).days == 0:
                    with container_d0:
                        ChatInfoCard(title=chat_info.title, chat_id=chat_info.cid, router=router)

                elif (date.today() - chat_info.date).days == 1:
                    with container_d1:
                        ChatInfoCard(title=chat_info.title, chat_id=chat_info.cid, router=router)

                elif (date.today() - chat_info.date).days > 1:
                    with container_d30:
                        ChatInfoCard(title=chat_info.title, chat_id=chat_info.cid, router=router)


class ChatFooter(FooterBindableUi):
    def __init__(
        self,
        router: Router,
        chat_sidebar: ChatSidebar,
    ):
        """专用于 ChatGPT 的 Footer 组件
        Desc: ChatGPT UI 的核心组件之一就是底部的 footer 元素，它需要根据用户的首次输入时联动侧边栏
            进行卡片的新增。同时在已有对话历史上，便不再采取往侧边栏新增卡片，而是形成一个在当前对话界面
            上新增对话卡片。甚至后面还需添加上传PDF、图片、音频等文件。

        :param chat_sidebar: ChatGPT 的左侧边栏示例，用于控制联动底部输入框进行卡片新增。
        """
        super().__init__()
        self.send_disabled = to_ref(True)
        self._router = router
        self._chat_sidebar = chat_sidebar


        with self.classes('bg-white'), ui.column().classes('w-full max-w-4xl mx-auto my-6'):
            with ui.row().classes('w-full items-end content-end'):
                self.chat_box = InputBindableUi(
                    placeholder="Message AtomGPT", outlined=True,
                    input_class='mx-3', autogrow=True, item_aligned=True,
                    on_change=(
                        lambda e: self.send_disabled.set_value(True)
                        if len(e.value.strip()) == 0 else self.send_disabled.set_value(False)
                    )
                ).classes('flex-grow self-end rounded-lg').on(
                    "keyup.enter", self.__handle_send_event
                ).on('keyup.shift.enter.capture.stop', lambda: None)
                # keyup.shift.enter.capture.stop 表示不再往下触发

                with self.chat_box.add_slot('append'):
                    # 通过设定 `absolute md:bottom-3 md:right-3` 来使图标沉底固定
                    send_btn_css = "self-center absolute md:bottom-3 md:right-3 rounded-lg"
                    ButtonBindableUi(
                        icon='send', shape='rounded', flat=True, size='xm', dense=True,
                        disabled=self.send_disabled,
                        on_click=self.__handle_send_event,
                    ).classes(send_btn_css)

            footer_hit = "AtomGPT can make mistakes. Consider checking important information."
            ui.markdown(footer_hit).classes('text-xs self-center mr-8 m-[-1em] text-grey')

    def __handle_send_event(self):
        """处理输入框中 enter 和发送按钮 click 的事件，避免 shift+enter 同时按下触发"""

        # print(self._router.curr_path.value)

        # new_chat_card = self.__create_new_sidebar_card()
        fake_new_card = self.__create_new_sidebar_card()
        if self._router.curr_path.value == "/":
            new_chat_card = ChatInfoCard(title=fake_new_card.title, chat_id=fake_new_card.cid, router=self._router)
            new_chat_card.element.move(
                self._chat_sidebar.element.default_slot.children[1], target_index=1
            )
            self._router.open(chat_id=new_chat_card.chat_id)
        else:
            from atomui.layout.body import chat_messages_card
            from nicegui import context
            with context.get_client():
                chat_messages_card(fake_new_card.conversation)


        self.chat_box.element.set_value("")

    def __create_new_sidebar_card(self):
        fake_data = {
            "user": "draven",
            "cid": str(uuid4()),
            "title": self.chat_box.value.strip()[:20],
            "date": f"{datetime.now():%Y-%m-%d}",
            "conversation": [
                {
                    "role": "user",
                    "content": self.chat_box.value.strip()
                },
                {
                    "role": "assistant",
                    "content": "Today is 2023-12-20"
                },
            ]
        }

        fake_new_card = ChatCardModel(**fake_data)

        # new_chat_card = ChatCard(title=fake_new_card.title, chat_id=fake_new_card.cid, router=self._router)
        return fake_new_card


class ChatHeader(HeaderBindableUi):
    def __init__(self, chat_sidebar: ChatSidebar):
        super().__init__(elevated=True)
        header_css = "self-center items-center justify-between"
        header_style = "background: white; height: 55px"
        toggle_icon = to_ref("format_indent_decrease")

        def _change_toggle_icon():
            """改变侧滑按钮的图标"""
            if toggle_icon.value == "format_indent_decrease":
                toggle_icon.value = "format_indent_increase"
            else:
                toggle_icon.value = "format_indent_decrease"

            chat_sidebar.toggle()

        with self.classes(header_css).style(header_style):
            ButtonBindableUi(
                icon=toggle_icon, color="primary", flat=True, dense=True,
                on_click=_change_toggle_icon
            ).classes('self-center')

            with ui.row().classes("items-center justify-center self-end bg-white"):
                with ChipBindableUi(color="stone-50").classes('text-white-10'):
                    Avatar(icon="img:/static/avatar/default.png", color='blue-2')
                    ui.label('draven').classes('font-bold')
                    BadgeBindableUi('3', color='red', floating=True).props('dense')

                    with MenuBindableUi(dense=True, flat=True, fit=True).classes('user-setting w-28'):
                        ButtonBindableUi(
                            text="Instructions", icon="library_books", color="zinc-50",
                            flat=True, align='left', dense=True
                        ).classes('w-full self-center font-normal text-xs')
                        ButtonBindableUi(
                            text="Settings", icon="settings", color="zinc-50",
                            flat=True, align='left', dense=True
                        ).classes('w-full self-center font-normal text-xs')
                        ui.separator()
                        ButtonBindableUi(
                            text="Logout", icon="logout", color="zinc-50",
                            flat=True, align='left', dense=True
                        ).classes('w-full self-center font-normal text-xs')
