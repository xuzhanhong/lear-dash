# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# Time       ：2023/3/23
# Author     ：xuzhanhong
# Description：通过固钉fac.AntdAffix固定页首
"""
import dash
from dash import html
import feffery_antd_components as fac


app = dash.Dash(__name__)

app.layout = html.Div(
    [
        # 页首行
        fac.AntdAffix(
            fac.AntdRow(
                style={
                    'background': 'white',
                    'height': '64px',
                    'boxShadow': 'rgb(240 241 242) 0px 2px 14px'
                }
            ),
        ),

        # 页面元素
        html.Div(
            '巴拉' * 10000,
            style={
                'padding': '25px'
            }
        )
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)
