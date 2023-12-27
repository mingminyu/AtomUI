from nicegui import ui
from atomui import to_ref
from atomui import webui


@ui.page('/')
def index():
    webui.chip("Add to calendar", icon="event")
    webui.chip("Add to calendar", icon="event", dense=True)
    webui.chip("Add to calendar", icon="event", disable=True)
    webui.chip("Add to calendar", icon="event", outline=True)
    webui.chip("Add to calendar", icon="event", clickable=False)
    webui.chip("Add to calendar", icon="event", color="grey")
    webui.chip("Add to calendar", icon="event", color="primary", text_color="white")

    def update_chip_removable_status():
        removable_ref.value = False

    removable_ref = to_ref(True)
    webui.chip(
        "Add to calendar", icon="home", removable=removable_ref,
        on_remove=update_chip_removable_status
    )


ui.run(language='zh-CN', port=8081, reload=True)
