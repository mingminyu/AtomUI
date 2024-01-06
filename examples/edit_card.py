from typing import Callable, List, Optional
from nicegui import ui
import asyncio


class FreeClick:
    """让元素把单双击事件区别开来"""

    def __init__(self, delay_seconds: float = 0.3) -> None:
        self.__delay_seconds = delay_seconds
        self.__click_task: Optional[asyncio.Task] = None
        self.__click_callbacks: List[Callable[[], None]] = []
        self.__dblclick_callbacks: List[Callable[[], None]] = []

    def apply(self, element: ui.element):
        async def one_click():
            if self.__click_task:
                self.__click_task.cancel()
            self.__click_task = asyncio.create_task(asyncio.sleep(self.__delay_seconds))
            await self.__click_task

            for cb in self.__click_callbacks:
                cb()

        def dblclick():
            if self.__click_task:
                self.__click_task.cancel()

            for cb in self.__dblclick_callbacks:
                cb()

        element.on("click", one_click).on("dblclick", dblclick)
        return self

    def on_click(self, callback: Callable[[], None]):
        self.__click_callbacks.append(callback)
        return self

    def on_dblclick(self, callback: Callable[[], None]):
        self.__dblclick_callbacks.append(callback)
        return self


class ClickEditCard(ui.card):
    def __init__(self) -> None:
        super().__init__()

        self.__click_callback: Optional[Callable[[], None]] = None
        self.__dblclick_callback: Optional[Callable[[], None]] = None

        with self.classes("p-0 pl-1 bg-blue-100").classes("cursor-pointer"):
            self._btn = ui.button("Test")
            # with self._btn:
            self._input = (
                ui.input(value="test")
                .classes("w-full bg-blue-grey-4")
                .props(
                    'dense standout="bg-blue-grey-4 text-white" input-class="text-white"'
                )
            )
            self._input.set_visibility(False)

            disable_class = "pointer-events-none bg-blue-500"

            def disable_input():
                self._input.classes(disable_class)
                self._input.set_visibility(False)
                self._btn.set_visibility(True)

            def enable_input():
                self._input.classes(remove=disable_class)

            disable_input()

            # 焦点离开或按回车，输入框就禁用吧
            self._input.on("blur", disable_input).on(
                "keyup.enter", lambda: self._input.run_method("blur")
            )

        fc = FreeClick().apply(self)

        @fc.on_click
        def _():
            if self.__click_callback:
                self.__click_callback()

        @fc.on_dblclick
        def _():
            if self.__dblclick_callback:
                self.__dblclick_callback()

            enable_input()
            self._input.run_method("focus")

    def on_dblclick(self, callback: Callable[[], None]):
        self.__dblclick_callback = callback
        return self

    def on_click(self, callback: Callable[[], None]):
        self.__click_callback = callback
        return self

    @property
    def title(self):
        return self._input.value


ui.label("单击卡片，显示信息，双击卡片，进入输入框编辑")
card = ClickEditCard()


@card.on_dblclick
def _():
    card._btn.set_visibility(False)
    card._input.set_visibility(True)


@card.on_click
def _():
    ui.notify('123')


ui.run()
