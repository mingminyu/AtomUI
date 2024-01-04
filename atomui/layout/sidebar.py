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

        with webui.card(bordered=True, flat=True).tight().classes('flex w-full bg-slate-700 h-12'):
            with webui.card_section(horizontal=True).classes('flex w-full bg-slate-700 h-12'):
                # ui.label(' ').classes('bg-blue-200 h-12 w-1')
                # with ui.row(wrap=False).classes('w-full self-center items-center gap-1 mt-0'):
                ui.label(' ').classes('bg-red-200 h-12 w-1')
                webui.button(
                    'Test Chat', color='gray-500', text_color='white', size='sm',
                    no_caps=True, flat=True, shape='square'
                ).classes('w-80 self-end h-12')
                    # ui.label('2023-01-01').classes('text-xs borderless self-end')

                # with ui.column(wrap=False).classes('flex w-full self-end items-end gap-0'):
                #     webui.button(
                #         'Test Chat', color='gray-500', text_color='white', size='sm',
                #         no_caps=True
                #     ).classes('w-full self-end')
                #     ui.label('2023-01-01').classes('w-full text-xs self-end text-gray-900')

        # 双击会引起单击事件
        # chat_card.style('border: 1px solid red')


        ui.label('Yesterday').classes('text-xs text-slate-400')

        ui.label('Previous 30 Days').classes('text-xs text-slate-400')

    return left_drawer

