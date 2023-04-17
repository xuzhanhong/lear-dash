# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# Time       ：2023/3/18
# Author     ：xuzhanhong
# Description：页面布局
"""
import dash
from dash import html
import feffery_antd_components as fac


app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fac.AntdTitle('1 常用的长度度量单位'),
        fac.AntdTitle('1.1 绝对长度', level=2),
        fac.AntdTitle('1.1.1 px', level=3),

        html.Div(
            'width: 100px',
            style={
                'width': '100px',
                'height': '50px',
                'backgroundColor': 'rgb(243, 243, 244)'
            }
        ),

        html.Div(
            'width: 200px',
            style={
                'width': '200px',
                'height': '50px',
                'backgroundColor': 'rgb(243, 243, 244)'
            }
        ),

        fac.AntdTitle('1.2 相对长度', level=2),
        fac.AntdTitle('1.2.1 %', level=3),

        # 父级元素
        html.Div(
            # 子级元素
            html.Div(
                'width: 66.6%',
                style={
                    'width': '66.6%',
                    'height': '100%',
                    'backgroundColor': '#008272'
                }
            ),
            style={
                'width': '200px',
                'height': '50px',
                'backgroundColor': 'rgb(243, 243, 244)'
            }
        ),

        fac.AntdTitle('1.2.2 rem', level=3),
        # 父级元素
        html.Div(
            # 子级元素
            html.Div(
                'width: 5rem',
                style={
                    'width': '5rem',
                    'height': '100%',
                    'backgroundColor': '#008272'
                }
            ),
            style={
                'width': '200px',
                'height': '50px',
                'backgroundColor': 'rgb(243, 243, 244)'
            }
        ),

        fac.AntdTitle('1.2.3 em', level=3),
        # 父级元素
        html.Div(
            # 子级元素
            html.Div(
                # 这里加上文字就贼大，不知道为啥
                # 'width: 0.5em',
                style={
                    'width': '0.5em',
                    'height': '100%',
                    'backgroundColor': '#008272'
                }
            ),
            style={
                'width': '200px',
                'height': '50px',
                'fontSize': '200px',
                'backgroundColor': 'rgb(243, 243, 244)'
            }
        ),

        fac.AntdTitle('1.2.4 vh/vw', level=3),
        html.Div(
            'width: 50vw, height: 20vh',
            style={
                'width': '50vw',
                'height': '20vh',
                'backgroundColor': '#008272'
            }
        ),

        fac.AntdTitle('2 尺寸度量主要用武之地'),
        fac.AntdTitle('2.1 width、height', level=2),

        fac.AntdInput(
            style={
                'width': '200px'
            }
        ),
        fac.AntdInput(
            style={
                'width': '100px'
            }
        ),

        fac.AntdTitle('2.2 max-width、max-height、min-width、min-height', level=2),
        fac.AntdTooltip(
            fac.AntdButton(
                '请将鼠标悬浮于此',
                type='primary'
            ),
            title='测试' * 20,
            overlayStyle={
                'maxWidth': '400px'  # 这样设置是为了自适应文字的长度，一行如果超过400px就会换行，不超过也不会显示400px
            }
        ),

        fac.AntdTitle('2.3 font-size', level=2),
        fac.AntdParagraph(
            [
                fac.AntdText('默认尺寸'),
                fac.AntdText('22px', style={'fontSize': '22px'}),
                fac.AntdText('10px', style={'fontSize': '10px'}),
            ]
        ),

        fac.AntdTitle('2.4 margin', level=2),
        html.Div(
            style={
                'width': '200px',
                'height': '100px',
                'backgroundColor': 'green',
                # 距离下方盒子的距离
                # 'margin': '10px'  上下左右都是间距10px
                'marginBottom': '10px'
            }
        ),
        html.Div(
            style={
                'width': '200px',
                'height': '100px',
                'backgroundColor': 'red'
            }
        ),

        fac.AntdTitle('2.4 padding', level=2),
        html.Div(
            '测试',
            style={
                'width': '200px',
                'height': '100px',
                'padding': '10px',
                'backgroundColor': 'green'
            }
        ),

        fac.AntdTitle('2.5 border与border-radius', level=2),
        html.Div(
            'border 边框',
            style={
                'width': '200px',
                'height': '100px',
                'backgroundColor': 'green',
                'border': '5px dashed red'
            }
        ),
        html.Div(
            'borderRadius 圆角',
            style={
                'width': '200px',
                'height': '100px',
                'padding': '25px',
                'backgroundColor': 'green',
                'borderRadius': '20px'
            }
        ),

        fac.AntdTitle('3 基于fac组件布局'),

        fac.AntdTitle('3.1 基于fac.AntdSpace的布局', level=2),
        fac.AntdSpace(
            [
                fac.AntdInput(
                    placeholder='这是一个输入框',
                    style={
                        'width': '150px'
                    }
                )
            ] * 4,
            size='large'
        ),

        fac.AntdTitle('3.2 基于fac.AntdRow、fac.AntdCol的网格系统布局', level=2),

        fac.AntdTitle('3.3 基于fac.AntdRow、fac.AntdCol的网格系统布局', level=2),

    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)
