from nicegui import ui
from atomui import webui
from atomui import ref_computed, to_ref
from atomui.components.router import Router
from atomui.mock.chat_conversation import chat_conversations_example
from atomui.models.chat import ChatCard


def var_index(uid: str):
    webui.label(f'uid: {uid}')


def chat_sidebar_card_deprecated(
    *,
    chat_card: ChatCard,
    router: Router,
):
    """Deprecated: 显示侧边栏历史聊天卡片信息"""
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