from typing import Callable, Dict, Union
from nicegui import background_tasks, ui, helpers


"""
参考文档: https://github.com/zauberzeug/nicegui/tree/main/examples/single_page_app
"""


class RouterFrame(ui.element, component='router_frame.js'):
    pass


class Router:
    def __init__(self) -> None:
        self.routes: Dict[str, Callable] = {}
        self.content: ui.element = None
        self.current_path: str = '/'

    def add(self, path: str):
        def decorator(func: Callable):
            self.routes[path] = func
            return func
        return decorator

    def open(self, target: Union[Callable, str]) -> None:
        if isinstance(target, str):
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

        # self.content.clear()
        background_tasks.create(build())
        self.current_path = path  # 记录当前URL

    def frame(self) -> ui.element:
        self.content = RouterFrame().on('open', lambda e: self.open(e.args))
        return self.content
