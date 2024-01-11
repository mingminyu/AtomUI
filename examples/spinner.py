import time
from nicegui import ui, run
from atomui import webui


ui.query('.nicegui-content').classes('flex-center')


def sleep_task(number: int):
    time.sleep(number)


def build_task_loading(message: str, is_done: bool = False):
    with ui.row():
        if is_done:
            ui.icon('done', color="negative")
        else:
            ui.spinner(color="positive")

        ui.label(message)


async def run_tasks():
    task_loading = ui.refreshable(build_task_loading)
    task_loading("任务A")
    await run.io_bound(sleep_task, number=2)
    task_loading.refresh("任务A结束", is_done=True)


async def run_multi_tasks():
    container.clear()

    with container:
        task_loading = ui.refreshable(build_task_loading)
        task_loading("任务A")
        await run.io_bound(sleep_task, number=3)
        task_loading.refresh("任务A结束", is_done=True)

        task_loading = ui.refreshable(build_task_loading)
        task_loading("任务B")
        await run.io_bound(sleep_task, number=4)
        task_loading.refresh("任务B结束", is_done=True)

        task_loading = ui.refreshable(build_task_loading)
        task_loading("任务C")
        await run.io_bound(sleep_task, number=5)
        task_loading.refresh("任务C结束", is_done=True)


webui.button("执行", on_click=run_tasks)
webui.button("多任务执行", on_click=run_multi_tasks)
container = ui.row().classes('w-24')

ui.run()
