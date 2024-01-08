from typing import Callable, Dict, Union, Optional
from nicegui import background_tasks, ui, helpers
from functools import partial
from atomui import to_ref
from ..utils.signals import ReadonlyRef, is_ref, effect
from ..utils.signals import _TMaybeRef as TMaybeRef


"""
参考文档: https://github.com/zauberzeug/nicegui/tree/main/examples/single_page_app
"""


class RouterFrame(ui.element, component='router_frame.js'):
    pass


class Router:
    def __init__(self) -> None:
        self.routes: Dict[str, Callable] = {}
        self.content: ui.element = None
        self.curr_path: Optional[TMaybeRef[str]] = to_ref('/')

    def add(self, path: str):
        def decorator(func: Callable):
            self.routes[path] = func
            return func
        return decorator

    def add_parameters_url(self, chat_id: str, func: Callable):
        self.routes[chat_id] = partial(func, chat_id=chat_id)


    def open(self, target: Union[Callable, str], func: Optional[Callable] = None) -> None:
        if isinstance(target, str):
            if target not in self.routes and func is not None:
                self.add_parameters_url(target, func)

            path = target if target in self.routes.keys() else "/"
            builder = self.routes[path]  # 如果未找到路径，则重定向的到首页
        else:
            path = {v: k for k, v in self.routes.items()}.get(target, "/")
            builder = target

        async def build() -> None:
            with self.content:
                ui.run_javascript(f'''
                    if (window.location.pathname !== "{path}") {{
                        history.pushState({{page: "{path}"}}, "", "{path}");
                    }}
                    ''')
                result = builder()

                if helpers.is_coroutine_function(builder):
                    await result

        self.content.clear()
        background_tasks.create(build())
        self.curr_path.value = path  # 记录当前URL

    def frame(self) -> ui.element:
        self.content = RouterFrame().on('open', lambda e: self.open(e.args))
        return self.content
