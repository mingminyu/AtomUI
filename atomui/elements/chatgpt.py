from nicegui import ui
from nicegui.events import ValueChangeEventArguments
from .footer import FooterBindableUi
from .input import InputBindableUi
from .button import ButtonBindableUi
from ..utils.signals import to_ref


class ChatSidebar:
    ...


class ChatBody:
    ...



class ChatFooter(FooterBindableUi):
    def __init__(
        self,
        chat_sidebar: ChatSidebar,
        # chat_body: ChatBody,
    ):
        """专用于 ChatGPT 的 Footer 组件
        Desc: ChatGPT UI 的核心组件之一就是底部的 footer 元素，它需要根据用户的首次输入时联动侧边栏
            进行卡片的新增。同时在已有对话历史上，便不再采取往侧边栏新增卡片，而是形成一个在当前对话界面
            上新增对话卡片。甚至后面还需添加上传PDF、图片、音频等文件。

        :param chat_sidebar: ChatGPT 的左侧边栏示例，用于控制联动底部输入框进行卡片新增。
        """
        super().__init__()
        # self.new_chat_card = None
        self.send_disabled = to_ref(True)

        with (self.classes('bg-white'), ui.column().classes('w-full max-w-4xl mx-auto my-6')):
            with ui.row().classes('w-full items-end content-end'):
                chat_box = InputBindableUi(
                    placeholder="Message AtomGPT", outlined=True,
                    input_class='mx-3', autogrow=True, item_aligned=True,
                    on_change=(
                        lambda e: self.send_disabled.set_value(True)
                        if len(e.value.strip()) == 0 else self.send_disabled.set_value(False)
                    )
                ).classes('flex-grow self-end rounded-lg')

                with chat_box.add_slot('append'):
                    # 通过设定 `absolute md:bottom-3 md:right-3` 来使图标沉底固定
                    send_btn_css = "self-center absolute md:bottom-3 md:right-3 rounded-lg"
                    ButtonBindableUi(
                        icon='send', shape='rounded', flat=True, size='xm', dense=True,
                        disabled=self.send_disabled,
                        on_click=lambda: (print({"role": "user", "content": chat_box.value})),
                    ).classes(send_btn_css)

            footer_hit = "AtomGPT can make mistakes. Consider checking important information."
            ui.markdown(footer_hit).classes('text-xs self-center mr-8 m-[-1em] text-grey')
