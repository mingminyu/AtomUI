import asyncio
from typing import Callable, List, Optional, Union
from nicegui import ui
from ..elements.base import BindableUi


class FreeClick:
    """让元素把单双击事件区别开来"""
    def __init__(self, delay_seconds: float = 0.3) -> None:
        self.delay_seconds = delay_seconds
        self.click_task: Optional[asyncio.Task] = None
        self.click_callbacks: List[Callable[[], None]] = []
        self.dblclick_callbacks: List[Callable[[], None]] = []

    def apply(self, element: Union[ui.element, BindableUi]):
        async def one_click():
            if self.click_task:
                self.click_task.cancel()

            self.click_task = asyncio.create_task(asyncio.sleep(self.delay_seconds))
            await self.click_task

            _ = [cb() for cb in self.click_callbacks]

        def dblclick():
            if self.click_task:
                self.click_task.cancel()

            _ = [cb() for cb in self.dblclick_callbacks]

        element.on("click", one_click).on("dblclick", dblclick)
        return self

    def on_click(self, callback: Callable[[], None]):
        self.click_callbacks.append(callback)
        return self

    def on_dblclick(self, callback: Callable[[], None]):
        self.dblclick_callbacks.append(callback)
        return self
