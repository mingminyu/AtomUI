from nicegui import ui
from nicegui.events import ValueChangeEventArguments
from atomui import to_ref
from atomui import webui


def chat_footer():
    send_disabled = to_ref(True)

    def update_send_btn_disabled(e: ValueChangeEventArguments):
        if len(e.value.strip()) == 0:
            send_disabled.value = True
        else:
            send_disabled.value = False

    with ui.footer().classes('bg-white'), ui.column().classes('w-full max-w-4xl mx-auto my-6'):
        with ui.row().classes('w-full items-end content-end'):
            chat_box = webui.input(
                placeholder="Message AtomGPT", outlined=True, input_class='mx-3', autogrow=True, item_aligned=True,
                on_change=lambda e: update_send_btn_disabled(e)
            ).classes('flex-grow self-end')

            with chat_box.add_slot('append'):
                # 通过设定 `absolute md:bottom-3 md:right-3` 来使图标沉底固定
                webui.button(
                    icon='send', shape='rounded', flat=True, size='xm', dense=True, disabled=send_disabled
                ).classes('self-center absolute md:bottom-3 md:right-3').style('border-radius: 0.5rem')

        ui.markdown(
            'AtomGPT can make mistakes. Consider checking important information.'
        ).classes('text-xs self-center mr-8 m-[-1em] text-grey')


    return chat_box, send_disabled
