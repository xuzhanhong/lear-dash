from dash import dcc
from flask_login import login_user
from dash.dependencies import Input, Output, State

from server import app, User
from models.auth import UserAccount


@app.callback(
    [Output('login-username-form-item', 'validateStatus'),
     Output('login-password-form-item', 'validateStatus'),
     Output('login-username-form-item', 'help'),
     Output('login-password-form-item', 'help'),
     Output('login-redirect-container', 'children')],
    Input('login-submit', 'nClicks'),
    [State('login-username', 'value'),
     State('login-password', 'md5Value')],
    prevent_initial_call=True
)
def login_auth(nClicks, username, password_md5):

    # 校验全部输入值是否不为空
    if all([nClicks, username, password_md5]):

        # 校验用户名是否存在
        if UserAccount.check_user_exists(username).get('message') == '用户已存在':
            # 校验密码是否正确
            if (
                UserAccount
                .check_user_password(username,
                                     password_md5=password_md5,
                                     mode='md5')
                .get('message')
            ) == '密码正确':
                # 登录成功
                # 否则登录验证通过
                current_user = User()

                current_user.id = username

                login_user(current_user)

                return [
                    None,
                    None,
                    None,
                    None,
                    dcc.Location(
                        pathname='/',
                        id='login-redirect'
                    )
                ]

            return [
                None,
                'error',
                None,
                '密码错误！',
                None
            ]

        return [
            'error',
            None,
            '用户不存在！',
            None,
            None
        ]

    return [
        None if username else 'error',
        None if password_md5 else 'error',
        None if username else '请输入用户名！',
        None if password_md5 else '请输入密码！',
        None
    ]
