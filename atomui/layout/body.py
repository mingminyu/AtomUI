from nicegui import ui
from atomui.utils.signals import ReadonlyRef


def chat_greet(show: ReadonlyRef):
    with ui.column().classes('items-center self-center gap-0 mt-60 mb-0').style('padding-top: 120px') as home_greet:
        ui.avatar(
            icon="img:static/images/site_logo.svg", size="100px", color="white"
            )
        ui.markdown("**How can I help you today?**").classes('text-xl gap-0 mt-0')
    home_greet.bind_visibility_from(show, 'value')
