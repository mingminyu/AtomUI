from nicegui import ui
from typing import List
from atomui.utils.signals import ReadonlyRef
from atomui import webui
from atomui.utils.parser import MarkdownParser
from atomui.models.chat import ChatMessage

md_parser = MarkdownParser()


def chat_greet(show_ref: ReadonlyRef):
    # 针对 `landscape`(横屏) 和 `portrait`(竖屏) 分别设置
    with ui.column().classes(
        'items-center self-center gap-0 mb-0 md:pt-[10%] landscape:pt-[5%] portrait:pt-[60%]'
    ) as home_greet:
        ui.avatar(
            icon="img:/static/avatar/logo.svg", size="100px", color="white"
            )
        ui.markdown("**How can I help you today?**").classes('text-xl gap-0 mt-0')
    home_greet.bind_visibility_from(show_ref, 'value')


def chat_message_card(chat_message: ChatMessage):
    """展示聊天对话信息"""
    if chat_message.role == "user":
        avatar = "img:/static/avatar/default.png"
    else:
        avatar = "img:/static/avatar/logo.svg"

    with ui.row(wrap=True).classes(
        'w-full items-center self-center w-[900px] max-w-8xl landscape:mx-60 portrait:mx-40 gap-0'
    ):
        with webui.card(bordered=False).classes('w-full min-w-3xl max-w-4xl my-1 no-shadow'):
            with webui.card_section(horizontal=True):
                webui.avatar(avatar, color=None).props('dense flat')

                with ui.column().classes('self-center pr-8'):
                    for message_token in md_parser.split_code_block_content(chat_message.value):
                        if message_token.type != 'fence':
                            ui.markdown(message_token.content).classes('w-full')
                        else:
                            ui.code(message_token.content).classes('w-full bg-gray-200')


def chat_messages_card(chat_messages: List[ChatMessage]):
    """展示整个对话信息"""
    for chat_message in chat_messages:
        chat_message_card(chat_message)
