from time import sleep
from nicegui import context, ui, run
import asyncio

ui.button.default_props("no-caps")


def task1():
    sleep(5)
    return "task1"


def task2():
    sleep(2)
    return "task2"


def task3(num: int):
    sleep(5)
    return f"task3:{num}"


async def onclick_TaskGroup():
    async with asyncio.TaskGroup() as tg:
        task1_bound = tg.create_task(run.io_bound(task1))
        task2_bound = tg.create_task(run.io_bound(task2))
        task3_bound = tg.create_task(run.io_bound(task3, 666))

        # 离开 TaskGroup 作用域，这开始所有任务，并等待
        ui.notify("开始执行3个任务")

    # 所以，代码运行到这里，里面的3个任务必定完成

    ui.notify(task1_bound.result())
    ui.notify(task2_bound.result())
    ui.notify(task3_bound.result())


async def onclick_gather():
    task1_bound = asyncio.create_task(run.io_bound(task1))
    task2_bound = asyncio.create_task(run.io_bound(task2))
    task3_bound = asyncio.create_task(run.io_bound(task3, 666))

    ui.notify("开始执行3个任务")

    total_result = await asyncio.gather(task1_bound, task2_bound, task3_bound)

    # 所以，代码运行到这里，里面的3个任务必定完成

    ui.notify(total_result[0])
    ui.notify(total_result[1])
    ui.notify(total_result[2])


async def onclick_as_completed():
    task1_bound = asyncio.create_task(run.io_bound(task1))
    task2_bound = asyncio.create_task(run.io_bound(task2))
    task3_bound = asyncio.create_task(run.io_bound(task3, 666))

    ui.notify("开始执行3个任务")
    for coro in asyncio.as_completed([task1_bound, task2_bound, task3_bound]):
        earliest_result = await coro
        ui.notify(earliest_result)


def onclick_with_task():
    """
    这种方式相当于丢弃异步语法，使用原始的callback方式。
    由于没有异步等待，因此下面的代码，各个耗时task并没有影响此函数的执行时间。可以理解成此函数一下子执行完毕
    接着，当 task 完成的时候，会触发 `when_task_done` 执行。但是，此时已经没有了前端客户端的连接对象。你无法创建新的组件(比如 notify)
    因此，需要先把client 保存起来 `cur_client = context.get_client()`
    创建组件时，使用 with 语法，确保在正确的 client 下执行即可
    """

    # 没有等待，所以任务开始并不会阻塞或等待这里的语句执行
    task1_bound = asyncio.create_task(run.io_bound(task1))
    task2_bound = asyncio.create_task(run.io_bound(task2))
    task3_bound = asyncio.create_task(run.io_bound(task3, 666))

    ui.notify("开始执行3个任务")

    cur_client = context.get_client()

    def when_task_done(task):
        with cur_client:
            ui.notify(task.result())

    task1_bound.add_done_callback(when_task_done)
    task2_bound.add_done_callback(when_task_done)
    task3_bound.add_done_callback(when_task_done)


# ui
ui.label("同时执行3个耗时任务")
ui.button("使用 TaskGroup(py3.11可用)", on_click=onclick_TaskGroup)
ui.button("使用 gather(py3.8可用)", on_click=onclick_gather)

ui.button(
    "使用 as_completed(py3.8可用)，先完成的任务先提示", on_click=onclick_as_completed
)

ui.button(
    "普通的 task callback，没有异步等待 (py3.8可用)，先完成的任务先提示",
    on_click=onclick_with_task,
)

ui.run()
