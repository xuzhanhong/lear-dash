import dash
from dash import html, dcc
from dash.dependencies import Input, Output
from flask_login import current_user

from server import app
from config import RouterConfig

# 载入子页面
import views

app.layout = html.Div(
    [
        # 注入url监听
        dcc.Location(id='url'),

        # 注入页面内容挂载点
        html.Div(id='app-mount'),

        # 路由重定向
        html.Div(id='router-redirect-container'),

        # 注入消息提示容器
        html.Div(
            [
                # "用户管理-新增用户"消息提示
                html.Div(id='index-user-manage-add-user-message-container'),
            ]
        )
    ]
)


@app.callback(
    [Output('app-mount', 'children'),
     Output('router-redirect-container', 'children')],
    Input('url', 'pathname')
)
def router(pathname):

    # 检验pathname合法性
    if pathname not in RouterConfig.VALID_PATHNAME:
        # 渲染404状态页
        return [
            views._404.render_content(),
            None
        ]

    # 检查当前会话是否已经登录
    # 若已登录
    if current_user.is_authenticated:
        # 根据pathname控制渲染行为
        if pathname == '/login':
            # 重定向到主页面
            return [
                dash.no_update,
                dcc.Location(
                    pathname='/',
                    id='router-redirect'
                )
            ]

        # 否则正常渲染主页面
        return [
            views.index.render_content(
                current_user.id,
                current_user.gender,
                current_user.role,
                current_user.register_time,
                current_user.accessible_apps
            ),
            None
        ]

    # 若未登录
    # 根据pathname控制渲染行为
    if pathname == '/login':
        return [
            views.login.render_content(),
            None
        ]

    # 否则重定向到登录页
    return [
        dash.no_update,
        dcc.Location(
            pathname='/login',
            id='router-redirect'
        )
    ]


if __name__ == '__main__':
    app.run(debug=True)
