import pandas as pd
from nicegui import ui
from ex4nicegui.reactive import rxui
from atomui import webui


@ui.page('/test')
def index():
    df = pd.DataFrame({"name": ["a", "b"], "value": [1, 2]})
    # 创建容器，之后创建的东西都往里面放即可
    box = ui.element("div")

    with box:
        rxui.table.from_pandas(df)

    def build_table():
        # 执行之前，清空容器
        box.clear()
        # 创建的时候，记得要在 box 中即可
        with box:
            table = rxui.table.from_pandas(df)

        def on_row_click(e):
            data = e.args[-2]
            build_card(data["name"])

        table.element.on("rowDblclick", on_row_click)

    build_table()

    def build_card(name: str):
        box.clear()
        with box:
            ui.label(f"这是切换后的内容，双击的行数据的name：{name}")
            ui.button("切换到表格", on_click=build_table)


@ui.page('/')
def basic():
    # TODO: 在 columns 中自定义 sort 排序方法未生效
    columns = [
        {
            "name": 'name',
            "required": True,
            "label": 'Dessert (100g serving)',
            "align": 'left',
            "field": "name",
            "sortable": True
        },
        {"name": 'calories', "align": 'center', "label": 'Calories', "field": 'calories', "sortable": True},
        {"name": 'fat', "label": 'Fat (g)', "field": 'fat', "sortable": True},
        {"name": 'carbs', "label": 'Carbs (g)', "field": 'carbs'},
        {"name": 'protein', "label": 'Protein (g)', "field": 'protein'},
        {"name": 'sodium', "label": 'Sodium (mg)', "field": 'sodium'},
        {"name": 'calcium', "label": 'Calcium (%)', "field": 'calcium', "sortable": True},
        {"name": 'iron', "label": 'Iron (%)', "field": 'iron', "sortable": True}
    ]
    rows = [
        {
            "name": 'Frozen Yogurt',
            "calories": 159,
            "fat": 6.0,
            "carbs": 24,
            "protein": 4.0,
            "sodium": 87,
            "calcium": '14%',
            "iron": '1%'
        },
        {
            "name": 'Ice cream sandwich',
            "calories": 237,
            "fat": 9.0,
            "carbs": 37,
            "protein": 4.3,
            "sodium": 129,
            "calcium": '8%',
            "iron": '1%'
        },
        {
            "name": 'Eclair',
            "calories": 262,
            "fat": 16.0,
            "carbs": 23,
            "protein": 6.0,
            "sodium": 337,
            "calcium": '6%',
            "iron": '7%'
        },
        {
            "name": 'Cupcake',
            "calories": 305,
            "fat": 3.7,
            "carbs": 67,
            "protein": 4.3,
            "sodium": 413,
            "calcium": '3%',
            "iron": '8%'
        },
        {
            "name": 'Gingerbread',
            "calories": 356,
            "fat": 16.0,
            "carbs": 49,
            "protein": 3.9,
            "sodium": 327,
            "calcium": '7%',
            "iron": '16%'
        },
        {
            "name": 'Jelly bean',
            "calories": 375,
            "fat": 0.0,
            "carbs": 94,
            "protein": 0.0,
            "sodium": 50,
            "calcium": '0%',
            "iron": '0%'
        },
        {
            "name": 'Lollipop',
            "calories": 392,
            "fat": 0.2,
            "carbs": 98,
            "protein": 0,
            "sodium": 38,
            "calcium": '0%',
            "iron": '2%'
        },
        {
            "name": 'Honeycomb',
            "calories": 408,
            "fat": 3.2,
            "carbs": 87,
            "protein": 6.5,
            "sodium": 562,
            "calcium": '0%',
            "iron": '45%'
        },
        {
            "name": 'Donut',
            "calories": 452,
            "fat": 25.0,
            "carbs": 51,
            "protein": 4.9,
            "sodium": 326,
            "calcium": '2%',
            "iron": '22%'
        },
        {
            "name": 'KitKat',
            "calories": 518,
            "fat": 26.0,
            "carbs": 65,
            "protein": 7,
            "sodium": 54,
            "calcium": '12%',
            "iron": '6%'
        }
    ]
    webui.table(rows=rows, columns=columns, title="Standard Table", row_key="name")
    ui.separator()

    webui.table(rows=rows, columns=columns, title="Dark Mode", row_key="name", dark=True)
    ui.separator()

    webui.table(rows=rows, columns=columns, title="Dense Mode", row_key="name", dense=True)
    ui.separator()
    # 粘性标题/列
    webui.table(
            rows=rows, columns=columns, title="Sticky Header", row_key="name", flat=True, bordered=True,
            table_header_class="text-red", table_header_style='background-color: #c1f4cd')
    ui.separator()
    # TODO: 暂时未实现 sticky column 的效果
    webui.table(
        rows=rows, columns=columns, title="Sticky Column", row_key="name", flat=True, bordered=True,
        table_style="width: 600px", )
    ui.separator()
    # TODO: 暂时未实现 sticky header and column 的效果

    # 分割栏
    webui.table(
        rows=rows, columns=columns, title="Vertical", row_key="name", flat=True, bordered=True,
        separator="vertical")
    ui.separator()
    webui.table(
        rows=rows, columns=columns, title="Cell", row_key="name", flat=True, bordered=True,
        separator="cell")

    webui.table(
        rows=rows, columns=columns, title="Cell", row_key="name", flat=True, bordered=True,
        separator="None")
    ui.separator()

    # 风格
    webui.table(
        rows=rows, columns=columns, title="Custom Coloring", row_key="name", flat=True, bordered=True,
        table_header_class="text-brown", table_class="text-grey-8", card_class="bg-amber-5 text-brown",
        color="primary"
    )
    ui.separator()

    webui.table(
        rows=rows, columns=columns, title="No Header/Footer", row_key="name", hide_header=True, hide_bottom=True
    )
    ui.separator()
    # 虚拟滚动
    webui.table(
        rows=rows, columns=columns, title="Basic Virtual Scroll", row_key="name", virtual_scroll=True,
        pagination=None,
    ).style("height: 400px")
    ui.separator()
    # TODO: 还未实现动态加载
    webui.table(
        rows=rows, columns=columns, title="Dynamic loading virtual scroll", row_key="name", virtual_scroll=True,
        pagination=None, loading=True,
    ).style("height: 400px")
    ui.separator()


ui.run(language='zh-CN', port=8085, reload=True)

