# coding: utf-8
import asyncio
from nicegui import ui
from atomui.utils.signals import Ref
from atomui import ref_computed, to_ref
from atomui import webui


@ui.page('/standard_button')
def standard_button():
    with ui.row().classes("q-pa-md q-gutter-sm"):
        webui.button("Standard", color="white")
        webui.button("Primary", color="primary")
        webui.button("Secondary", color="secondary")
        webui.button("Amber", color="amber").props("glossy")
        webui.button("Brown 5", color="brown-5")
        webui.button("Deep Orange", color="deep-orange").props("glossy")
        webui.button("Purple", color="purple")
        webui.button("Black", color="black").classes('text-white')


@ui.page('/custom_color_button')
def custom_color_button():
    with ui.row().classes("q-pa-md q-gutter-sm"):
        webui.button("Fuchsia", color="fuchsia", text_color="white")
        webui.button("Fuchsia", flat=True, text_color="fuchsia")
        webui.button("Goldenrod", color="goldenrod", text_color="white")
        # 没有 text-goldenrod 这个属性，必须使用 style
        webui.button("Goldenrod", outline=True, text_color="green")
        webui.button("Goldenrod", color="grey-4", text_color="purple",
                     outline=True, glossy=True, unelevated=True, icon="camera_enhance")


@ui.page('/button_with_icon')
def icon_button():
    with ui.row().classes("q-pa-md q-gutter-sm"):
        webui.button("On Left", icon="mail", color="primary")
        webui.button("On Right", icon_right="mail", color="primary")
        webui.button("On Left and Right", icon="mail", icon_right="send", color="red")
        webui.button("Stacked", icon="phone", glossy=True, stack=True, color="purple")


@ui.page('/button_round_icon')
def round_icon_button():
    with ui.row().classes("q-pa-md q-gutter-sm"):
        webui.button(icon="shopping_cart", color="primary", shape="round")
        webui.button(icon="navigation", color="secondary", shape="round")
        webui.button(icon="layers_clear", color="amber", shape="round", glossy=True, text_color="black")
        webui.button(icon="directions", color="brown-5", shape="round")
        webui.button(icon="edit_location", color="deep-orange", shape="round")
        webui.button(icon="local_grocery_store", color="purple", glossy=True, shape="round")
        webui.button(icon="my_location", color="black", shape="round", text_color="white")


@ui.page('/button_square_icon')
def square_icon_button():
    with ui.row().classes("q-pa-md q-gutter-sm"):
        webui.button(icon="shopping_cart", color="primary", shape="square")
        webui.button(icon="navigation", color="secondary", shape="square")
        webui.button(icon="layers_clear", color="amber", shape="square", glossy=True, text_color="black")
        webui.button(icon="directions", color="brown-5", shape="square")
        webui.button(icon="edit_location", color="deep-orange", shape="square")
        webui.button(icon="local_grocery_store", color="purple", glossy=True, shape="square")
        webui.button(icon="my_location", color="black", shape="square", text_color="white")


@ui.page('/button_custom_content')
def custom_content_button():
    """TODO: 还有一些未实现"""
    with ui.row().classes("q-pa-md q-gutter-sm"):
        btn = webui.button(color="teal")

        with btn:
            ui.icon("map", size="3em").props("left")
            ui.label("Label")

        btn2 = webui.button(shape="round")
        with btn2:
            ui.avatar(icon="img:https://nicegui.io/logo_square.png", color="white").classes("self-center")

        btn3 = webui.button(color="indigo", no_caps=True)
        with btn3:
            ui.html("Multiline<br>Button")

        btn4 = webui.button(color="deep-orange", push=True)
        with btn4.classes("row items-center no-wrap"):
            ui.icon("map").props("left")
            ui.html("Custom<br>Content")


@ui.page('/truncate_label')
def custom_content_button():
    """TODO: 还不知道怎么实现"""
    with ui.row().classes("q-pa-md q-gutter-sm"):
        with webui.button(color="primary").style("width: 200px"):
            ui.label("This is some very long text that is expected to be truncated").classes("ellipsis")


@ui.page('/button_alignment')
def alignment_button():
    with ui.row().classes("q-pa-md q-gutter-sm"):
        webui.button("Align to left", align="left").classes("btn-fixed-width w-40")
        webui.button("Align to right", align="right", color="secondary").classes("btn-fixed-width w-40")
        webui.button("Align between", align="between", color="accent",
                     icon="flight_takeoff").classes("btn-fixed-width w-60")
        webui.button("Align around", align="around", color="brown-5",
                     icon="lightbulb_outline").classes("btn-fixed-width w-60")


@ui.page('/button_design')
def standard_button():
    with ui.row():
        webui.button("Flat", flat=True)
        webui.button("Flat Round", flat=True, shape="rounded")
        webui.button(icon="card_giftcard", flat=True, shape="rounded")

    with ui.row():
        webui.button("Outline", outline=True)
        webui.button("Outline Rounded", outline=True, shape="rounded")
        webui.button(icon="card_giftcard", outline=True, shape="round")

    with ui.row():
        webui.button("Push", push=True)
        webui.button(icon="card_giftcard", push=True, shape="round")
        webui.button("Push", push=True, text_color="primary", color="white")
        webui.button(push=True, text_color="primary", color="white", shape="round", icon="card_giftcard")

    with ui.row():
        webui.button("Unelevated", unelevated=True)
        webui.button("Unelevated Rounded", unelevated=True, shape="rounded")
        webui.button(icon="card_giftcard", unelevated=True, shape="rounded")

    with ui.row():
        webui.button("No-Caps", no_caps=True)

    with ui.row():
        webui.button("Glossy", glossy=True, color="teal")
        webui.button("Glossy", glossy=True, color="deep-orange", shape="rounded")
        webui.button(icon="card_giftcard", glossy=True, shape="round")
        webui.button(icon="local_florist", glossy=True, shape="round", color="secondary")
        webui.button(icon="local_activity", glossy=True, shape="round", color="deep-orange")


@ui.page('/button_size')
def alignment_button():
    with ui.row().classes("q-pa-md q-gutter-sm"):
        webui.button("Size xs", size="xs")
        webui.button("Size xm", size="xm")
        webui.button("Size md", size="md")
        webui.button("Size lg", size="lg")
        webui.button("Size xl", size="xl")

    with ui.row().classes("q-pa-md q-gutter-sm"):
        webui.button("Size xs", size="xs", shape="rounded")
        webui.button("Size xm", size="xm", shape="rounded")
        webui.button("Size md", size="md", shape="rounded")
        webui.button("Size lg", size="lg", shape="rounded")
        webui.button("Size xl", size="xl", shape="rounded")

    with ui.row().classes("q-pa-md q-gutter-sm"):
        webui.button(icon="navigation", size="xs", shape="round")
        webui.button(icon="add_a_photo", size="xm", shape="round")
        webui.button(icon="camera", size="md", shape="round")
        webui.button(icon="camera_front", size="lg", shape="round")
        webui.button(icon="my_location", size="xl", shape="round")

    with ui.row().classes("q-pa-md q-gutter-sm"):
        webui.button("Size xs", size="xs", dense=True)
        webui.button("Size xm", size="xm", dense=True)
        webui.button("Size md", size="md", dense=True)
        webui.button("Size lg", size="lg", dense=True)
        webui.button("Size xl", size="xl", dense=True)

    with ui.row().classes("q-pa-md q-gutter-sm"):
        webui.button("Size xs", size="xs", dense=True, shape="rounded")
        webui.button("Size xm", size="xm", dense=True, shape="rounded")
        webui.button("Size md", size="md", dense=True, shape="rounded")
        webui.button("Size lg", size="lg", dense=True, shape="rounded")
        webui.button("Size xl", size="xl", dense=True, shape="rounded")

    with ui.row().classes("q-pa-md q-gutter-sm"):
        webui.button(icon="navigation", size="xs", shape="round", dense=True,)
        webui.button(icon="add_a_photo", size="xm", shape="round", dense=True,)
        webui.button(icon="camera", size="md", shape="round", dense=True,)
        webui.button(icon="camera_front", size="lg", shape="round", dense=True,)
        webui.button(icon="my_location", size="xl", shape="round", dense=True,)

    with ui.row().classes("q-pa-md q-gutter-sm"):
        webui.button("Text height: 10px", size="10px")
        webui.button("Custom", size="22px", color="purple").classes("q-px-xl q-py-xs")
        webui.button(icon="map", size="35px", color="teal", shape="round")


@ui.page('/button_padding')
def alignment_button():
    with ui.row().classes("q-pa-md q-gutter-sm"):
        webui.button(icon="eco", padding="none")
        webui.button(icon="eco", padding="xs")
        webui.button(icon="eco", padding="lg")
        webui.button(icon="eco", padding="10px 5px")
        webui.button(icon="eco", padding="xs lg")
        webui.button(icon="eco", padding="xl", shape="round")
        webui.button(icon="eco", padding="lg xs", shape="round")


@ui.page('/button_progress')
def alignment_button():
    async def _loading_3_seconds(loading_ref: Ref) -> None:
        """等待3秒"""
        loading_ref.value = True
        await asyncio.sleep(3)
        loading_ref.value = False

    loading_status = to_ref(False)
    with ui.row().classes("q-pa-md q-gutter-sm"):
        webui.button(
            "Button", color="secondary", loading=loading_status,
            on_click=lambda e: _loading_3_seconds(loading_status)
        )

    loading_status2 = to_ref(False)
    with ui.row().classes("q-pa-md q-gutter-sm"):
        btn2 = webui.button(
            "Button", color="red", loading=loading_status2,
            on_click=lambda e: _loading_3_seconds(loading_status2))
        btn2.add_slot('loading', 'Loading...')

    loading_status21 = to_ref(False)
    with ui.row().classes("q-pa-md q-gutter-sm"):
        webui.button(
            "Button", color="red",
            loading=loading_status21, loading_text="Loading...",
            on_click=lambda e: _loading_3_seconds(loading_status21)
        )

    loading_status3 = to_ref(False)
    with ui.row().classes("q-pa-md q-gutter-sm"):
        btn3 = webui.button(
            "Button", color="purple", loading=loading_status3, on_click=lambda e: _loading_3_seconds(loading_status3))

        # btn3.add_slot('loading', '<q-spinner-radio />')
        with btn3.add_slot('loading', ):
            ui.spinner('radio')

    loading_status31 = to_ref(False)
    with ui.row().classes("q-pa-md q-gutter-sm"):
        webui.button(
            "Button", color="purple", loading=loading_status31, loading_icon="radio",
            on_click=lambda e: _loading_3_seconds(loading_status31)
        )

    loading_status4 = to_ref(False)
    with ui.row().classes("q-pa-md q-gutter-sm"):
        btn4 = webui.button(
            "Button", color="primary", loading=loading_status4, on_click=lambda e: _loading_3_seconds(loading_status4)
        ).style("width: 150px")

        # TODO: 先加载的 Loading...，后加载的 spinner，暂时无法做到示例中的图标靠左
        with btn4.add_slot('loading', 'Loading...'):
            ui.spinner('hourglass', color="white").classes("on-left")

    loading_status41 = to_ref(False)
    with ui.row().classes("q-pa-md q-gutter-sm"):
        webui.button(
            "Button", color="secondary",
            loading=loading_status41, loading_icon="hourglass",
            loading_text="Loading...", loading_icon_color="white",
            on_click=lambda e: _loading_3_seconds(loading_status41)
        ).style("width: 150px")

    # 使用前端的方式可以
    loading_status5 = to_ref(False)
    with ui.row().classes("q-pa-md q-gutter-sm"):
        btn5 = webui.button(
            "Button", color="primary", loading=loading_status5,
            on_click=lambda e: _loading_3_seconds(loading_status5)
        ).style("width: 150px")
        # 采用源码的方式添加 spinner 可能会更好
        btn5.add_slot('loading', '''
            <q-spinner-hourglass class="on-left" />
            Loading...
        ''')

    loading_status51 = to_ref(False)
    with ui.row().classes("q-pa-md q-gutter-sm"):
        webui.button(
            "Button", color="secondary", loading_icon_left=True,
            loading=loading_status51, loading_icon="hourglass", loading_text="Loading...", loading_icon_color="white",
            on_click=lambda e: _loading_3_seconds(loading_status51)
        ).style("width: 150px")

    loading_status6 = to_ref(False)
    with ui.row().classes("q-pa-md q-gutter-sm"):
        btn6 = webui.button(
            icon="camera_front", color="brown", loading=loading_status6, shape="round",
            on_click=lambda e: _loading_3_seconds(loading_status6)
        )
        btn6.add_slot('loading', '''<q-spinner-facebook />''')

    loading_status7 = to_ref(False)
    with ui.row().classes("q-pa-md q-gutter-sm"):
        btn7 = webui.button(
            icon="camera_rear", color="black", text_color="white",
            loading=loading_status7, shape="round",
            on_click=lambda e: _loading_3_seconds(loading_status7)
        )
        btn7.add_slot('loading', '''<q-spinner-gears />''')

    async def _start_loading() -> None:
        """等待3秒"""
        loading_status8.value = True

    async def _loading_stop_by_another_button() -> None:
        """等待3秒"""
        loading_status8.value = False

    loading_status8 = to_ref(False)
    loading_status9 = ref_computed(lambda: not loading_status8.value)

    with ui.row().classes("q-pa-md q-gutter-sm"):
        btn8 = webui.button(
            "Controlled from outside",
            loading=loading_status8,
            on_click=lambda e: _start_loading()
        )
        btn8.add_slot('loading', '''
            <q-spinner-radio class="on-left" />
            Click "Stop" Button
        ''')

        btn9 = webui.button(
            "Stop", color="negative",
            on_click=lambda e: _loading_stop_by_another_button()
        )
        btn9.bind_disable(loading_status9)

    async def _loading_with_process() -> None:
        """等待3秒"""
        loading_status10.value = True
        while loading_percent10.value <= 100:
            loading_percent10.value += 10
            await asyncio.sleep(0.5)

        loading_status10.value = False

    loading_status10 = to_ref(False)
    loading_percent10 = to_ref(0)
    with ui.row().classes("q-pa-md q-gutter-sm"):
        btn10 = webui.button(
            "Compute PI",
            percentage=loading_percent10,
            loading=loading_status10,
            on_click=lambda e: _loading_with_process()
        ).classes("w-40")
        btn10.add_slot('loading', '''
                <q-spinner-gears class="on-left" />
                Computing...
                ''')

    async def _loading_with_process2() -> None:
        """等待3秒"""
        loading_status11.value = True
        while loading_percent11.value <= 100:
            loading_percent11.value += 10
            await asyncio.sleep(0.5)

        loading_status11.value = False

    loading_status11 = to_ref(False)
    loading_percent11 = to_ref(0)
    with ui.row().classes("q-pa-md q-gutter-sm"):
        webui.button(
            icon="cloud_upload",
            shape="round",
            percentage=loading_percent11,
            loading=loading_status11,
            on_click=lambda e: _loading_with_process2()
        )

    async def _loading_with_process3() -> None:
        """等待3秒"""
        loading_status12.value = True
        while loading_percent12.value <= 100:
            loading_percent12.value += 10
            await asyncio.sleep(0.5)

        loading_status12.value = False

    loading_status12 = to_ref(False)
    loading_percent12 = to_ref(0)
    with ui.row().classes("q-pa-md q-gutter-sm"):
        webui.button(
            icon="cloud_upload",
            color="orange",
            unelevated=True,
            dark_percentage=True,
            percentage=loading_percent12,
            loading=loading_status12,
            on_click=lambda e: _loading_with_process3()
        ).classes('w-40')


ui.run(language='zh-CN', port=8084)
