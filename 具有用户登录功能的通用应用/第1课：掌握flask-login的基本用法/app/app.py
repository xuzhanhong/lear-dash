from datetime import timedelta
from dash import html, dcc
import feffery_utils_components as fuc
import feffery_antd_components as fac
from dash.dependencies import Input, Output, State
from flask_login import logout_user, login_user, current_user

from server import app, User

app.layout = html.Div(
    [
        dcc.Location(id='url'),

        # 重载页面用
        fuc.FefferyExecuteJs(id='login-refresh-page'),
        fuc.FefferyExecuteJs(id='logout-refresh-page'),

        html.Div(
            id='content-container'
        )
    ],
    style={
        'padding': '100px'
    }
)


@app.callback(
    Output('content-container', 'children'),
    Input('url', 'pathname')
)
def render_content(pathname):

    # 判断当前用户会话是否已登录
    if current_user.is_authenticated:

        return [
            fac.AntdAlert(
                type='success',
                showIcon=True,
                message='欢迎您！用户：{}'.format(current_user.id),
                style={
                    'marginBottom': '10px'
                }
            ),
            fac.AntdButton(
                '登出',
                id='logout',
                type='primary',
                danger=True
            )
        ]

    return [
        fac.AntdAlert(
            type='warning',
            showIcon=True,
            message='检测到您还未登录，请在下方输入信息后登录！',
            style={
                'marginBottom': '10px'
            }
        ),
        fac.AntdSpace(
            [
                fac.AntdInput(
                    id='username',
                    placeholder='输入用户名',
                    style={
                        'width': '300px'
                    }
                ),
                fac.AntdButton(
                    '登入',
                    id='login',
                    type='primary'
                )
            ]
        )
    ]


@app.callback(
    Output('login-refresh-page', 'jsString'),
    Input('login', 'nClicks'),
    State('username', 'value')
)
def login(nClicks, username):

    if nClicks and username:

        new_user = User()

        new_user.id = username

        login_user(new_user,
                   remember=True)

        return 'window.location.reload()'


@app.callback(
    Output('logout-refresh-page', 'jsString'),
    Input('logout', 'nClicks')
)
def logout(nClicks):

    if nClicks:

        logout_user()

        return 'window.location.reload()'


if __name__ == '__main__':
    app.run(debug=True)
