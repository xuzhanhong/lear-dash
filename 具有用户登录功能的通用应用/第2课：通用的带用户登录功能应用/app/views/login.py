from dash import html
import feffery_antd_components as fac

from server import app
import callbacks.login_c


def render_content():

    return fac.AntdCard(
        [
            fac.AntdForm(
                [
                    fac.AntdFormItem(
                        fac.AntdInput(
                            id='login-username'
                        ),
                        label='用户名',
                        id='login-username-form-item'
                    ),
                    fac.AntdFormItem(
                        fac.AntdInput(
                            id='login-password',
                            mode='password',
                            passwordUseMd5=True
                        ),
                        label='密码',
                        id='login-password-form-item'
                    ),
                    fac.AntdFormItem(
                        fac.AntdButton(
                            '登录',
                            id='login-submit',
                            type='primary',
                            block=True
                        )
                    )
                ],
                layout='vertical',
                style={
                    'width': '100%'
                }
            ),

            # 重定向容器
            html.Div(id='login-redirect-container')
        ],
        id='login-form-container',
        title='XXXXXX平台',
        hoverable=True,
        style={
            'position': 'fixed',
            'top': '20%',
            'left': '50%',
            'width': '500px',
            'padding': '20px 50px',
            'transform': 'translateX(-50%)'
        }
    )
