from nicegui import ui
from atomui import webui
from atomui import to_ref


@ui.page('/input_design')
def input_design():
    with ui.row().classes("q-pa-md q-gutter-sm"):
        webui.input("Standard")
        webui.input("Filled", filled=True)
        webui.input("Outlined", outlined=True)
        webui.input("Standout ", standout=True)
        webui.input("Custom standout", standout="bg-teal text-white")

    with ui.row().classes("q-pa-md q-gutter-sm"):
        webui.input("Borderless", borderless=True)
        webui.input("Rounded filled", shape="rounded", filled=True)
        webui.input("Rounded outlined", shape="rounded", outlined=True)
        webui.input("Rounded standout", shape="rounded", standout=True)

    with ui.row().classes("q-pa-md q-gutter-sm"):
        webui.input("Square filled", shape="square", filled=True)
        webui.input("Square outlined", shape="square", outlined=True)
        webui.input("Square standout", shape="square", standout=True)


@ui.page('/input_coloring')
def input_coloring():
    with ui.row().classes("q-pa-md q-gutter-sm"):
        webui.input("Label", color="purple-12", left_icon="event")

    with ui.row().classes("q-pa-md q-gutter-sm"):
        webui.input("Label", color="teal", left_icon="event", filled=True)

    with ui.row().classes("q-pa-md q-gutter-sm"):
        webui.input("Label", color="lime-11", bg_color="green", left_icon="event", filled=True)

    with ui.row().classes("q-pa-md q-gutter-sm"):
        webui.input(
            "Label", color="teal", outlined=True,
            right_icon="https://cdn.quasar.dev/logo-v2/svg/logo.svg",
            right_icon_kwargs={"slot_type": "append", "size": "xl", "type": "avatar", "color": "white"}
        )

    with ui.row().classes("q-pa-md q-gutter-sm"):
        webui.input(
            "Label", color="teal", standout=True, bottom_slots=True, counter=True,
            clearable=True, left_icon="place", right_icon="favorite", hint="Field hint"
                  )


@ui.page('/input_standard')
def input_standard():
    ref_dense_mode = to_ref(False)
    with ui.row().classes("q-pa-md q-gutter-sm"):
        dense_switch = ui.switch("Dense Input", value=False)
        dense_switch.bind_value_to(ref_dense_mode, 'value')

    webui.input(dense=ref_dense_mode)
    webui.input("Label (stacked)", dense=ref_dense_mode, stack_label=True)
    webui.input("Label", dense=ref_dense_mode)
    webui.input(
        "Label", dense=ref_dense_mode, placeholder="Placeholder", hint="With placeholder"
    )
    webui.input(dense=ref_dense_mode, placeholder="Placeholder", hint="With placeholder")
    webui.input(dense=ref_dense_mode, left_icon="event")
    webui.input(dense=ref_dense_mode, right_icon="https://cdn.quasar.dev/logo-v2/svg/logo.svg")
    webui.input(
        "Label", dense=ref_dense_mode, bottom_slots=True, counter=True,
        left_icon="place", right_icon="close", hint="Field hint"
    )
    webui.input(
        "Label", dense=ref_dense_mode, bottom_slots=True, counter=True,
        left_icon="flight_takeoff", right_icon="search",
        left_icon_kwargs={"slot_type": "before"},
        hint="Field hint", max_length="12",
    )
    # 这里没有在后面再添加图表，实际上既可以添加 append，也可以添加 after
    webui.input(
        "Label", dense=ref_dense_mode, bottom_slots=True, counter=True,
        left_icon="https://cdn.quasar.dev/img/avatar5.jpg",
        right_icon="schedule", hint="Field hint", max_length="12",
        left_icon_kwargs={"slot_type": "before"},
        right_icon_kwargs={"slot_type": "after"},
    )

    webui.input(
        "Label", dense=ref_dense_mode, bottom_slots=True, counter=True,
        left_icon="event", right_icon="add", hint="Field hint", max_length="12",
        left_icon_kwargs={"slot_type": "before"},
        right_icon_kwargs={"slot_type": "append", "type": "button", "round": True, "flat": True},
              )
    webui.input(dense=ref_dense_mode, hint="Disable", disable=True)
    webui.input(dense=ref_dense_mode, hint="Readonly", readonly=True)
    webui.input(dense=ref_dense_mode, hint="Disable and readonly", readonly=True, disable=True)


@ui.page('/input_filled')
def input_standard():
    ref_dense_mode = to_ref(False)
    with ui.row().classes("q-pa-md q-gutter-sm"):
        dense_switch = ui.switch("Dense Input", value=False)
        dense_switch.bind_value_to(ref_dense_mode, 'value')

    webui.input(filled=True, dense=ref_dense_mode)
    webui.input("Label (stacked)", filled=True, dense=ref_dense_mode, stack_label=True)
    webui.input("Label", filled=True, dense=ref_dense_mode)
    webui.input(
        "Label", filled=True, dense=ref_dense_mode, placeholder="Placeholder", hint="With placeholder"
    )
    webui.input(dense=ref_dense_mode, filled=True, placeholder="Placeholder", hint="With placeholder")
    webui.input(dense=ref_dense_mode, filled=True, left_icon="event")
    webui.input(dense=ref_dense_mode, filled=True, right_icon="https://cdn.quasar.dev/logo-v2/svg/logo.svg")
    webui.input(
        "Label", filled=True, dense=ref_dense_mode, bottom_slots=True, counter=True,
        left_icon="place", right_icon="close", hint="Field hint"
    )
    webui.input(
        "Label", filled=True, dense=ref_dense_mode, bottom_slots=True, counter=True,
        left_icon="flight_takeoff", right_icon="search", hint="Field hint", max_length="12",
        left_icon_kwargs={"slot_type": "before"}
              )
    # 这里没有在后面再添加图表，实际上既可以添加 append，也可以添加 after
    webui.input(
        "Label", filled=True, dense=ref_dense_mode, bottom_slots=True, counter=True,
        left_icon="https://cdn.quasar.dev/img/avatar5.jpg", right_icon="schedule", hint="Field hint", max_length="12",
        left_icon_kwargs={"slot_type": "before"}, right_icon_kwargs={"slot_type": "after"},
              )

    webui.input(
            "Label", filled=True, dense=ref_dense_mode, bottom_slots=True, counter=True,
            left_icon="event", right_icon="add", hint="Field hint", max_length="12",
            left_icon_kwargs={"slot_type": "before"},
            right_icon_kwargs={"slot_type": "append", "type": "button", "round": True, "flat": True},
    )
    webui.input(dense=ref_dense_mode, filled=True, hint="Disable", disable=True)
    webui.input(dense=ref_dense_mode, filled=True, hint="Readonly", readonly=True)
    webui.input(dense=ref_dense_mode, filled=True, hint="Disable and readonly", readonly=True, disable=True)


@ui.page('/input_outlined')
def input_standard():
    ref_dense_mode = to_ref(False)
    with ui.row().classes("q-pa-md q-gutter-sm"):
        dense_switch = ui.switch("Dense Input", value=False)
        dense_switch.bind_value_to(ref_dense_mode, 'value')

    webui.input(outlined=True, dense=ref_dense_mode)
    webui.input("Label (stacked)", outlined=True, dense=ref_dense_mode, stack_label=True)
    webui.input("Label", outlined=True, dense=ref_dense_mode)
    webui.input(
        "Label", outlined=True, dense=ref_dense_mode, placeholder="Placeholder", hint="With placeholder"
    )
    webui.input(dense=ref_dense_mode, outlined=True, placeholder="Placeholder", hint="With placeholder")
    webui.input(dense=ref_dense_mode, outlined=True, left_icon="event")
    webui.input(dense=ref_dense_mode, outlined=True, right_icon="https://cdn.quasar.dev/logo-v2/svg/logo.svg")
    webui.input(
        "Label", outlined=True, dense=ref_dense_mode, bottom_slots=True, counter=True,
        left_icon="place", right_icon="close", hint="Field hint"
    )
    webui.input(
            "Label", outlined=True, dense=ref_dense_mode, bottom_slots=True, counter=True,
            left_icon="flight_takeoff", right_icon="search", left_icon_kwargs={"slot_type": "before"},
            hint="Field hint", max_length="12",
              )
    # 这里没有在后面再添加图表，实际上既可以添加 append，也可以添加 after
    webui.input(
        "Label", outlined=True, dense=ref_dense_mode, bottom_slots=True, counter=True,
        left_icon="https://cdn.quasar.dev/img/avatar5.jpg", right_icon="schedule", hint="Field hint", max_length="12",
        left_icon_kwargs={"slot_type": "before"},
        right_icon_kwargs={"slot_type": "after"},
    )

    webui.input(
        "Label", outlined=True, dense=ref_dense_mode, bottom_slots=True, counter=True,
        left_icon="event", left_icon_kwargs={"slot_type": "before"},
        right_icon="add", right_icon_kwargs={"slot_type": "append", "type": "button", "round": True, "flat": True},
        hint="Field hint", max_length="12",
              )
    webui.input(dense=ref_dense_mode, outlined=True, hint="Disable", disable=True)
    webui.input(dense=ref_dense_mode, outlined=True, hint="Readonly", readonly=True)
    webui.input(dense=ref_dense_mode, outlined=True, hint="Disable and readonly", readonly=True, disable=True)


@ui.page('/input_standout')
def input_standard():
    ref_dense_mode = to_ref(False)
    with ui.row().classes("q-pa-md q-gutter-sm"):
        dense_switch = ui.switch("Dense Input", value=False)
        dense_switch.bind_value_to(ref_dense_mode, 'value')

    webui.input(standout=True, dense=ref_dense_mode)
    webui.input("Label (stacked)", standout=True, dense=ref_dense_mode, stack_label=True)
    webui.input("Label", standout=True, dense=ref_dense_mode)
    webui.input(
        "Label", standout=True, dense=ref_dense_mode, placeholder="Placeholder", hint="With placeholder"
    )
    webui.input(dense=ref_dense_mode, standout=True, placeholder="Placeholder", hint="With placeholder")
    webui.input(dense=ref_dense_mode, standout=True, left_icon="event")
    webui.input(dense=ref_dense_mode, standout=True, right_icon="https://cdn.quasar.dev/logo-v2/svg/logo.svg")
    webui.input(
        "Label", standout=True, dense=ref_dense_mode, bottom_slots=True, counter=True,
        left_icon="place", right_icon="close", hint="Field hint"
              )
    webui.input(
        "Label", standout=True, dense=ref_dense_mode, bottom_slots=True, counter=True,
        left_icon="flight_takeoff", right_icon="search", left_icon_kwargs={"slot_type": "before"},
        hint="Field hint", max_length="12",
              )
    # 这里没有在后面再添加图表，实际上既可以添加 append，也可以添加 after
    webui.input(
        "Label", standout=True, dense=ref_dense_mode, bottom_slots=True, counter=True,
        left_icon="https://cdn.quasar.dev/img/avatar5.jpg", left_icon_kwargs={"slot_type": "before"},
        right_icon="schedule", right_icon_kwargs={"slot_type": "after"}, hint="Field hint", max_length="12",
    )

    webui.input(
        "Label", standout=True, dense=ref_dense_mode, bottom_slots=True, counter=True,
        left_icon="event", right_icon="add", hint="Field hint", max_length="12",
        left_icon_kwargs={"slot_type": "before"},
        right_icon_kwargs={"slot_type": "append", "type": "button", "round": True, "flat": True}
    )
    webui.input(dense=ref_dense_mode, standout=True, hint="Disable", disable=True)
    webui.input(dense=ref_dense_mode, standout=True, hint="Readonly", readonly=True)
    webui.input(dense=ref_dense_mode, standout=True, hint="Disable and readonly", readonly=True, disable=True)


ui.run(language='zh-CN', port=8081)
