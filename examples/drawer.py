from nicegui import ui
from atomui import to_ref
from atomui import webui


@ui.page('/')
def input_standard():
    def _switch_mini_mode():
        """开启侧边栏折叠"""
        mini_ref.value = not mini_ref.value

    mini_ref = to_ref(False)

    with (
        ui.header(elevated=True, add_scroll_padding=True)
        .classes("self-center items-center justify-between")
        .style("background: white; height: 72px")
    ):
        webui.button(icon="menu_open", flat=True, dense=True, on_click=_switch_mini_mode)

    with webui.drawer(
            side="left",
            value=True,
            top_corner=True,
            bottom_corner=True,
            fixed=True,
            bordered=True,
            elevated=True,
            mini=mini_ref,
            mini_to_overlay=True,
            overlay=False,
            show_if_above=False,
            width="260",
    ).style('background: #777E90'):
        with ui.row().classes('items-center justify-center'):
            site_name = (
                ui.input(value='    AI.FUN')
                .style('padding-left: 15px; height: 40px')
                .classes('self-center bg-white-10 text-xl')
                .props('readonly borderless dark')
            )


ui.run(language='zh-CN', port=8081, reload=True)
