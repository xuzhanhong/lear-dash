# !/usr/bin/env python
# -*-coding:utf-8 -*-

import dash
from dash import html
import feffery_antd_components as fac


app = dash.Dash(__name__)

app.layout = html.Div(
    [

        fac.AntdSpace(
            [
                fac.AntdText('text1'),
                fac.AntdDivider(),  # 分割线
                fac.AntdText('text2'),
            ],
            direction='vertical',
            align='center',  # 加上这个就不显示分割线了
            style={
                'width': '100%'
            }
        ),

    ],
    style={
        'padding': '25px'
    }
)


if __name__ == '__main__':
    app.run_server(debug=True)
