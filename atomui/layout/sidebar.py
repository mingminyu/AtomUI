from nicegui import ui
from atomui import webui
from atomui import ref_computed, to_ref
from atomui.components.router import Router
from atomui.mock.chat_conversation import chat_conversations_example
from atomui.models.chat import ChatCard


def chat_main(chat_id: str):
    webui.label(f'uid: {chat_id}')



def chat_sidebar_card(chat_card: ChatCard, router: Router):
    webui.chat_edit_card(
        chat_card.title, show_input=to_ref(False),
        chat_id=chat_card.cid, curr_chat_id=router.curr_path,
        on_click=lambda: router.open(f'/c/{chat_card.cid}', chat_main)
    )


def chat_sidebar(router: Router) -> webui.drawer:
    with (webui.drawer(
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
    ).classes('bg-slate-700') as left_drawer):
        with ui.row().classes('items-center justify-center'):
            webui.button(
                "New Chat", icon="img:/static/avatar/logo.svg",
                icon_right="edit", color="slate-700", shape="square", align="between",
                no_caps=True, flat=True, dense=True, href='/'
            ).classes('flex-grow w-full text-white rounded-lg').style('width: 220px')

        # ui.label('Test').classes('text-xs text-slate-400 mt-10')
        # webui.chat_edit_card("Hello world 0", show_input=to_ref(False),
        #                      on_click=lambda: (print(123)), on_dblclick=lambda: (print(234)))
        #
        # webui.chat_edit_card("Hello world 1", show_input=to_ref(True),
        #                      on_click=lambda: (print(123)), on_dblclick=lambda: (print(234)))

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

        # chat_sidebar_card(chat_card=ChatCard(**chat_conversation_example[1]), router=router)

        ui.label('Previous 30 Days').classes('text-xs text-slate-400')
        for chat_conversation in chat_conversations_example:
            chat_card = ChatCard(**chat_conversation)

            if chat_card.chat_date_flag == 3:
                chat_sidebar_card(chat_card, router)

        # chat_sidebar_card(chat_card=ChatCard(**chat_conversation_example[2]), router=router)
        # webui.chat_edit_card(
        #     "Hello world 001", show_input=to_ref(False),
        #     sess_id="c1", curr_sess_id=router.curr_path,
        #     on_click=lambda: router.open('/c/c1'))

    return left_drawer
