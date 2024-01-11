import time
import asyncio
from nicegui import ui, run, context
from typing import List
from atomui.utils.signals import ReadonlyRef, to_ref
from atomui import webui
from atomui.utils.parser import MarkdownParser
from atomui.models.chat import ChatMessage

md_parser = MarkdownParser()


def chat_greet(show_ref: ReadonlyRef):
    # 针对 `landscape`(横屏) 和 `portrait`(竖屏) 分别设置
    with ui.column().classes(
        'w-full flex justify-center items-center justify-self-center gap-0 mb-0 '
        'md:pt-[100px] lg:pt-[100px] portrait:pt-[500px]'
    ) as home_greet:
        ui.avatar(
            icon="img:/static/avatar/logo.svg", size="100px", color="white"
            )
        ui.markdown("**How can I help you today?**").classes('text-xl gap-0 mt-0')
    home_greet.bind_visibility_from(show_ref, 'value')


def build_task_loading(
    message: str,
    chat_message: ChatMessage = None,
):
    with ui.row().classes('w-full self-center'):
        if not chat_message.think:
            for message_token in md_parser.split_code_block_content(chat_message.content):
                if message_token.type != 'fence':
                    ui.markdown(message_token.content).classes('w-full self-center')
                else:
                    ui.code(message_token.content).classes('w-full self-center bg-gray-200')
        else:
            ui.spinner(color="positive").classes('self-center')

        if message != "":
            ui.label(message).classes('text-md')


def chat_message_card(chat_message: ChatMessage):
    """
    展示聊天对话信息
    当前可以实现 Thinking 的 spinner 效果，但是交互信息会先出来
    """
    if chat_message.role == "user":
        avatar = "img:/static/avatar/default.png"
    else:
        avatar = "img:/static/avatar/logo.svg"

    with ui.row(wrap=True).classes('w-full flex justify-center self-center'):
        with webui.card(bordered=False).classes('w-full items-center self-center max-w-4xl my-0 py-0 px-2 no-shadow'):
            with webui.card_section(horizontal=True).classes('w-full gap-0 pr-2'):
                webui.avatar(avatar, color=None).props('dense flat gap-0')

                task_loading = ui.refreshable(build_task_loading)

                with ui.column().classes('self-center pr-8'):
                    if chat_message.think:
                        task_loading("Thinking ...", chat_message)
                    else:
                        task_loading("", chat_message)

                    task_bound = asyncio.create_task(run.io_bound(time.sleep, 2))
                    # curr_client = context.get_client()

                    def when_task_done(task):
                        chat_message.think = False
                        task_loading.refresh("", chat_message)

                    task_bound.add_done_callback(when_task_done)


def chat_messages_card(chat_messages: List[ChatMessage]):
    """展示整个对话信息"""
    for chat_message in chat_messages:
        chat_message_card(chat_message)
