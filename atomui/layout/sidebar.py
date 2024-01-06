from nicegui import ui
from atomui import webui
from atomui import ref_computed
from atomui.components.router import Router
from atomui.mock.chat_conversation import chat_conversation_example
from atomui.models.chat import ChatCard


def var_index(uid: str):
    webui.label(f'uid: {uid}')


def chat_sidebar_card(
        *,
        chat_card: ChatCard,
        router: Router,
):
    """显示侧边栏历史聊天卡片信息"""
    chat_id = f"/c/{chat_card.cid}"
    card_bg_color_ref = ref_computed(
        lambda: "bg-red-200 pl-1" if router.curr_path.value == chat_id else "bg-blue-200 pl-1"
    )

    with webui.card(flat=True).tight().classes('w-full justify-around bg-blue-200 h-8 gap-0 p-0') as chat_card_ele:
        with webui.card_section(horizontal=True).classes("w-full h-8 gap-0 pl-1") as card_sec:
            webui.button(
                chat_card.title, color='gray-500', text_color='white', size='sm',
                no_caps=True, flat=True, shape='square', align='left',
                on_click=lambda: router.open(chat_id, var_index),
            ).classes('w-48 self-start h-8 text-left')

            with webui.button(
                color='gray-500', size='sm', icon='more_horiz', no_caps=True, flat=True, shape='square'
            ).classes('w-8 self-start h-8 rounded-r'):
                with webui.menu(dense=True, flat=True).classes('text-xs gap-0 items-center self-center'):
                    webui.menu_item('Rename', dense=True, flat=True).classes('self-center text-center p-2.5')
                    webui.menu_item('Delete', dense=True, flat=True).classes('self-center text-center p-2.5')

        card_sec.bind_bg_color(card_bg_color_ref)

    return chat_card_ele


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
            ).classes('flex-grow w-full text-white').style(
                'width: 220px; border-radius: 0.5rem')

        ui.label('Today').classes('text-xs text-slate-400 mt-10')
        chat_sidebar_card(chat_card=ChatCard(**chat_conversation_example[0]), router=router)

        ui.label('Yesterday').classes('text-xs text-slate-400')
        chat_sidebar_card(chat_card=ChatCard(**chat_conversation_example[1]), router=router)

        ui.label('Previous 30 Days').classes('text-xs text-slate-400')
        chat_sidebar_card(chat_card=ChatCard(**chat_conversation_example[2]), router=router)

    return left_drawer
