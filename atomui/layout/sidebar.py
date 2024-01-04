from nicegui import ui
from atomui import webui


def chat_sidebar() -> webui.drawer:
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
                "New Chat", icon="img:static/images/site_logo.svg",
                icon_right="edit", color="slate-700", shape="square", align="between",
                no_caps=True, flat=True, dense=True
            ).classes('flex-grow w-full text-white').style(
                'width: 220px; border-radius: 0.5rem')

        ui.label('Today').classes('text-xs text-slate-400 mt-10')

        with webui.card(bordered=False, flat=True).tight().classes('w-full bg-slate-700 h-8 gap-0 p-0'):
            with webui.card_section(horizontal=True).classes('flex w-full bg-slate-700 h-8'):
                webui.label(' ').classes('bg-red-200 h-8 w-1')
                webui.button(
                    'Test Chat', color='gray-500', text_color='white', size='sm',
                    no_caps=True, flat=True, shape='square', align='left'
                ).classes('w-48 self-start h-8 text-left')
                with webui.button(
                    color='gray-500', size='sm', icon='more_horiz',
                    no_caps=True, flat=True, shape='square'
                ).classes('w-8 self-start h-8 rounded-r'):
                    with webui.menu().classes(
                        'text-xs gap-0 items-center self-center'
                    ).props('dense flat') as chat_sess_menu:
                        ui.menu_item('Rename').classes('self-center text-center p-2.5').props('dense flat')
                        ui.menu_item('Delete').classes('self-center text-center p-2.5').props('dense flat')

        with webui.card(bordered=False, flat=True).tight().classes('w-full justify-around bg-slate-700 h-8 gap-0 p-0'):
            with webui.card_section(horizontal=True).classes('flex w-full bg-slate-700 h-8'):
                webui.label(' ').classes('bg-green-200 h-8 w-1')
                webui.button(
                    'Test Chat', color='gray-500', text_color='white', size='sm',
                    no_caps=True, flat=True, shape='square', align='left'
                ).classes('w-48 self-start h-8 text-left')
                with webui.button(
                        color='gray-500', size='sm', icon='more_horiz',
                        no_caps=True, flat=True, shape='square'
                ).classes('w-8 self-start h-8 rounded-r'):
                    with webui.menu().classes(
                            'text-xs gap-0 items-center self-center'
                    ).props('dense flat') as chat_sess_menu:
                        ui.menu_item('Rename').classes('self-center text-center p-2.5').props('dense flat')
                        ui.menu_item('Delete').classes('self-center text-center p-2.5').props('dense flat')

        # 双击会引起单击事件

        ui.label('Yesterday').classes('text-xs text-slate-400')
        ui.label('Previous 30 Days').classes('text-xs text-slate-400')

    return left_drawer

