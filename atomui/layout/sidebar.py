from nicegui import ui
from atomui import webui
from atomui import to_ref
from atomui.components.router import Router
from atomui.mock.chat_conversation import chat_conversations_example
from atomui.models.chat import ChatCard
from atomui.layout.body import chat_messages_card


chat_cards = [ChatCard(**chat_conversation) for chat_conversation in chat_conversations_example]


def chat_main(chat_id: str):
    chat_card = [
        chat_card_ for chat_card_ in chat_cards if chat_card_.cid == chat_id.split('/')[-1]
    ]
    chat_messages_card(chat_card[0].conversation)


def chat_sidebar_card(chat_card: ChatCard, router: Router):
    return webui.chat_edit_card(
        chat_card.title, show_input=to_ref(False),
        chat_id=chat_card.cid, curr_chat_id=router.curr_path,
        on_click=lambda: router.open(f'/c/{chat_card.cid}', chat_main)
    )


def chat_sidebar(router: Router) -> webui.drawer:
    with webui.drawer(
            side="left",
            value=True,
            top_corner=True,
            bottom_corner=True,
            fixed=True,
            bordered=True,
            elevated=True,
            overlay=False,
            show_if_above=False,
            width="260",
    ).classes('bg-slate-700') as left_drawer:
        with ui.row().classes('items-center justify-center'):
            webui.button(
                "New Chat", icon="img:/static/avatar/logo.svg",
                icon_right="edit", color="slate-700", shape="square", align="between",
                no_caps=True, flat=True, dense=True, href='/'
            ).classes('flex-grow w-full text-white rounded-lg').style('width: 220px')

        ui.label('Today').classes('text-xs text-slate-400 mt-10')
        for chat_conversation in chat_conversations_example:
            chat_card = ChatCard(**chat_conversation)

            if chat_card.chat_date_flag == 1:
                chat_sidebar_card(chat_card, router)

        # chat_sidebar_card(chat_card=ChatCard(**chat_conversation_example[0]), router=router)

        ui.label('Yesterday').classes('text-xs text-slate-400')
        for chat_conversation in chat_conversations_example:
            chat_card = ChatCard(**chat_conversation)

            if chat_card.chat_date_flag == 2:
                chat_sidebar_card(chat_card, router)

        ui.label('Previous 30 Days').classes('text-xs text-slate-400')
        for chat_conversation in chat_conversations_example:
            chat_card = ChatCard(**chat_conversation)

            if chat_card.chat_date_flag == 3:
                chat_sidebar_card(chat_card, router)

    return left_drawer
