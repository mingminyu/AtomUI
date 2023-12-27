from nicegui import ui
from atomui import webui

# 基础
webui.switch(value=True)
webui.switch(value=True, color="green")

# 带标签
webui.switch(value=True, label="On Right")
webui.switch(value=True, label="On Left", left_label=True)

# 保持色彩
webui.switch(value=True, keep_color=True, color="red")

# 带图标
webui.switch(icon="alarm")
webui.switch(icon="mail")
webui.switch(checked_icon="check", unchecked_icon="clear", color="teal")

# 自定义模型值
# TODO: 这个功能完全可以响应式代替，没必要实现
webui.switch(true_value="Agreed", false_value="Disagreed", value=True,
           ).props('label="pinkModel"')

# 不确定的状态
indeterminate_switch = webui.switch(
                    value=True, indeterminate_icon="lock", indeterminate_value="abc",
                    toggle_indeterminate=True, on_change=lambda e: (print(e.value)))
# 数组模型
# TODO: 实现上有 BUG，显示不了数组，显示的内容会是 yellowred 或者 yellowredblue
# 实现有问题
array_switch = webui.switch(
    value=["yellow", "red"],
    label="Blue",
    val="blue"
)
ui.label("").bind_text_from(array_switch, 'value')

# TODO: 使用 QOptionGroup，对应到 nicegui 中的 radio 组件
# 暂时实现不了效果
webui.radio(
    options=[
        {'label': 'Battery too low', 'value': 'bat'},
        {'label': 'Friend request', 'value': 'friend', 'color': "green"},
        {'label': 'Picture uploaded', 'value': 'upload', 'color': "red"},
    ],
    type_='toggle',
    value="bat"
)

# TODO: 使用 QItem

# TODO: 原生表单提交

ui.run()
