# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# Time       ：2023/4/15
# Author     ：xuzhanhong
# Description：dash中的layout跟基础回调函数
"""
import dash
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Input, Output, State, ALL


# 实例化的Dash对象，一般命名为app，并非规定
app = dash.Dash(__name__)

app.layout = html.Div(
    # 编写相应的内容和功能
    fac.AntdSpace(
        [
            fac.AntdInputNumber(
                id='number1'
            ),
            '+',
            fac.AntdInputNumber(
                id='number2'
            ),
            fac.AntdButton(
                '计算',
                id='button'
            ),
            '=',
            fac.AntdText(
                '结果',
                id='result'
            ),
            fac.AntdText(
                id='formula'
            )
        ]
    )
)


# # 监听输入值的回调函数
# @app.callback(
#     # 更新组件的id，更新组件的属性
#     Output('result', 'children'),
#     # 输入组件的id，输入组件的属性
#     [Input('number1', 'value'),
#      Input('number2', 'value')]
# )
# # 回调函数的入参需要按照Input组件的顺序一一对应，参数名与组件无关
# def render_result(number1_value, number2_value):
#     if number1_value and number2_value:
#         return number1_value + number2_value
#     return '请完善输入！'


# 监听按钮的回调函数
@app.callback(
    # 更新组件的id，更新组件的属性
    [Output('formula', 'children'),
     Output('result', 'children')],
    # 按钮组件的属性，nClick监听点击了多少次按钮
    Input('button', 'nClicks'),
    # 输入组件的id，输入组件的属性
    [State('number1', 'value'),
     State('number2', 'value')]
)
# 回调函数的入参需要按照Input、State组件的顺序一一对应，参数名与组件无关
def render_result(nClicks, number1_value, number2_value):
    if nClicks:
        if number1_value and number2_value:
            return [
                f'{number1_value} + {number2_value}',
                number1_value + number2_value
            ]
    return [
        None,
        '请完善输入！'
    ]


if __name__ == '__main__':
    app.run_server(debug=True)
