from nicegui import ui
from atomui import to_ref
from atomui import webui
from atomui.elements.drawer import DrawerBindableUi


def chat_header(left_drawer: DrawerBindableUi):
    toggle_icon = to_ref("format_indent_decrease")

    with (
        ui.header(elevated=True, add_scroll_padding=True)
        .classes("self-center items-center justify-between")
        .style("background: white; height: 55px")
    ):
        def _change_toggle_icon():
            """改变侧滑按钮的图标"""
            if toggle_icon.value == "format_indent_decrease":
                toggle_icon.value = "format_indent_increase"
            else:
                toggle_icon.value = "format_indent_decrease"

            left_drawer.toggle()

        webui.button(
            icon=toggle_icon, color="primary", flat=True, dense=True,
            on_click=_change_toggle_icon
        ).classes('self-center')

        with ui.row().classes("items-center justify-center self-end bg-white"):
            with webui.chip(color="stone-50").classes('text-white-10'):
                webui.avatar(icon="img:/static/avatar/default.png", color='blue-2')
                ui.label('draven').classes('font-bold')
                webui.badge('3', color='red', floating=True).props('dense')

                with webui.menu(dense=True, flat=True, fit=True).classes('user-setting w-28'):
                    webui.button(
                        "Instructions", icon="library_books", color="zinc-50", flat=True, align='left', dense=True
                    ).classes('w-full self-center font-normal text-xs')
                    webui.button(
                        "Settings", icon="settings", color="zinc-50", flat=True, align='left', dense=True
                    ).classes('w-full self-center font-normal text-xs')
                    ui.separator()
                    webui.button(
                        "Logout", icon="logout", color="zinc-50", flat=True, align='left', dense=True
                    ).classes('w-full self-center font-normal text-xs')
