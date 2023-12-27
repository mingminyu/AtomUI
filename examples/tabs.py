from nicegui import ui
from atomui import webui


with webui.tabs(
            active_color="teal", active_bg_color="grey", left_icon="home", right_icon="arrow_right",
            outside_arrows=True, mobile_arrows=True, align="left"
          ).classes('w-full').props('inline-label') as tabs:
    for i in range(1, 5):
        webui.tab(f"a{i}", removable=True, icon='home', remove_mode='delete')

with webui.tab_panels(tabs=tabs.element).classes('w-full') as tab_panels:
    with webui.tab_panel('a2'):
        ui.label('abc')

    with webui.tab_panel('a3'):
        ui.label('123')

ui.run()
