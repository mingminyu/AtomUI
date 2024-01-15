from typing import Callable, Dict, Union, Optional
from nicegui import background_tasks, ui, helpers

from atomui import to_ref
from ..utils.signals import _TMaybeRef as TMaybeRef


"""
参考文档: https://github.com/zauberzeug/nicegui/tree/main/examples/single_page_app
"""


class RouterFrame(ui.element, component='router_frame.js'):
    pass


class Router:
    def __init__(self) -> None:
        self.routes: Dict[str, Callable] = {}
        self.content: Optional[ui.element] = None
        self.curr_path: Optional[TMaybeRef[str]] = to_ref('/')

    def add(self, path: str):
        def decorator(func: Callable):
            self.routes[path] = func
            return func
        return decorator


    def open(
        self,
        target: str = "/chat",
        *,
        chat_id: Optional[str] = None
    ) -> None:
        if target.startswith("/chat") and target.count("/") == 2:
            chat_id = target.split("/")[-1]
            target = "/chat"

        if target in self.routes.keys() and chat_id is not None:
            builder = self.routes[target]
            path = f"{target}/{chat_id}"
        else:
            path = "/"
            builder = self.routes[path]

        async def build() -> None:
            with self.content:
                ui.run_javascript(
                    f'''
                        if (window.location.pathname !== "{path}") {{
                            history.pushState({{page: "{path}"}}, "", "{path}");
                        }}
                    ''')
                result = builder(chat_id) if chat_id is not None else builder()

                if helpers.is_coroutine_function(builder):
                    await result

        self.content.clear()
        background_tasks.create(build())
        self.curr_path.value = path


    def frame(self) -> ui.element:
        self.content = RouterFrame().on('open', lambda e: self.open(e.args))
        return self.content
