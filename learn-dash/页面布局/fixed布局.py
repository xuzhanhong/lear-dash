# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# Time       ：2023/3/25
# Author     ：xuzhanhong
# Description：
"""
import dash
from dash import html
import feffery_antd_components as fac


app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fac.AntdAffix(
            fac.AntdButton(
                'AntdAffix 固定不动',
                type='primary',
            ),
            offsetTop=100,
            style={
                'margin-left': '100px'
            }
        ),

        # 页面元素
        html.Div(
            '巴拉' * 10000,
            style={
                'padding': '25px'
            }
        ),

        # 固定元素
        fac.AntdButton(
            'fixed 固定不动',
            type='primary',
            style={
                'position': 'fixed',
                'top': '100px',
                'right': '100px'
            }
        ),


    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)
