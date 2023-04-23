import re
import dash
import time
import pandas as pd
from dash import dcc, html
from datetime import datetime
from flask_login import logout_user, current_user
import feffery_antd_components as fac
from dash.dependencies import Input, Output, State, ALL

from server import app
from models.auth import UserAccount
from utils import str2md5
from config import RouterConfig


@app.callback(
    [Output('index-redirect-container', 'children'),
     Output('index-personal-info-modal', 'visible')],
    Input('index-header-dropdown', 'nClicks'),
    State('index-header-dropdown', 'clickedKey'),
    prevent_initial_call=True
)
def index_dropdown_click(nClicks, clickedKey):

    if clickedKey == '退出登录':
        logout_user()
        return [
            dcc.Location(
                pathname='/login',
                id='index-redirect'
            ),
            False
        ]

    elif clickedKey == '个人资料':
        return [
            None,
            True
        ]

    return dash.no_update


@app.callback(
    Output('index-user-manage-modal', 'visible'),
    Input('index-header-dropdown', 'nClicks'),
    State('index-header-dropdown', 'clickedKey'),
    prevent_initial_call=True
)
def index_dropdown_open_user_manage(nClicks, clickedKey):

    if clickedKey == '用户管理':
        return True
    return False


@app.callback(
    Output('index-user-manage-modal-children-container', 'children'),
    Input('index-user-manage-modal', 'visible'),
    prevent_initial_call=True
)
def index_user_manage_modal_update_children(visible):

    if visible:

        records = (
            pd
            .DataFrame(
                (
                    UserAccount
                    .select()
                    .where(UserAccount.role == '普通用户')
                    .dicts()
                )
            )
            .assign(
                register_time=lambda df: (
                    df
                    .register_time
                    .dt
                    .strftime('%Y-%m-%d %H:%M:%S')
                ),
                key=lambda df: df.username
            )
        )

        return [
            fac.AntdSpin(
                fac.AntdTable(
                    id='index-user-manage-user-list-table',
                    data=records.to_dict('records'),
                    columns=[
                        {
                            'dataIndex': 'username',
                            'title': '用户名'
                        },
                        {
                            'dataIndex': 'gender',
                            'title': '性别'
                        },
                        {
                            'dataIndex': 'password',
                            'title': '密码'
                        },
                        {
                            'dataIndex': 'register_time',
                            'title': '注册时间'
                        }
                    ],
                    rowSelectionType='checkbox',
                    rowSelectionWidth=50,
                    bordered=True,
                    style={
                        'width': '100%'
                    }
                ),
                text='更新中'
            ),

            # 辅助处理多输入 -> 相同输出型回调
            html.Div(
                [
                    dcc.Store(
                        id={
                            'type': 'index-user-manage-user-list-table-update-store',
                            'index': '新增用户'
                        }
                    ),
                    dcc.Store(
                        id={
                            'type': 'index-user-manage-user-list-table-update-store',
                            'index': '删除用户'
                        }
                    )
                ]
            ),

            # 新增用户表单modal
            fac.AntdModal(
                [
                    fac.AntdForm(
                        [
                            fac.AntdFormItem(
                                fac.AntdInput(
                                    id='index-user-manage-add-user-username'
                                ),
                                label='用户名',
                                id='index-user-manage-add-user-username-form-item'
                            ),
                            fac.AntdFormItem(
                                fac.AntdInput(
                                    id='index-user-manage-add-user-password',
                                ),
                                label='密码',
                                id='index-user-manage-add-user-password-form-item'
                            ),
                            fac.AntdFormItem(
                                fac.AntdRadioGroup(
                                    id='index-user-manage-add-user-gender',
                                    options=[
                                        {
                                            'label': '男',
                                            'value': '男'
                                        },
                                        {
                                            'label': '女',
                                            'value': '女'
                                        }
                                    ],
                                    optionType='button',
                                    defaultValue='男'
                                ),
                                label='性别'
                            ),

                            fac.AntdButton(
                                '确认添加',
                                id='index-user-manage-add-user-confirm',
                                type='primary',
                                block=True
                            )
                        ],
                        layout='vertical'
                    )
                ],
                id='index-user-manage-add-user-modal',
                title='新增用户',
                mask=False,
                centered=True
            ),

            fac.AntdSpace(
                [
                    fac.AntdButton(
                        '新增用户',
                        id='index-user-manage-add-user',
                        type='primary'
                    ),
                    fac.AntdPopconfirm(
                        fac.AntdButton(
                            '删除选中用户',
                            type='primary',
                            danger=True
                        ),
                        id='index-user-manage-delete-user',
                        placement='top',
                        title='确认删除'
                    ),
                ],
                style={
                    'paddingTop': '50px'
                }
            )
        ]

    return dash.no_update


@app.callback(
    Output('index-user-manage-add-user-modal', 'visible'),
    Input('index-user-manage-add-user', 'nClicks'),
    prevent_initiall_call=True
)
def index_user_manage_add_user_modal_open(nClicks):

    if nClicks:
        return True

    return False


@app.callback(
    [Output('index-user-manage-user-list-table', 'data'),
     Output('index-user-manage-user-list-table', 'selectedRowKeys')],
    Input(
        {
            'type': 'index-user-manage-user-list-table-update-store',
            'index': ALL
        },
        'data'
    ),
    prevent_initial_call=True
)
def index_user_manage_user_list_table_update(*args):

    records = (
        pd
        .DataFrame(
            (
                UserAccount
                .select()
                .where(UserAccount.role == '普通用户')
                .dicts()
            )
        )
        .assign(
            register_time=lambda df: (
                df
                .register_time
                .dt
                .strftime('%Y-%m-%d %H:%M:%S')
            ),
            key=lambda df: df.username
        )
    )

    return [
        records.to_dict('records'),
        []
    ]


@app.callback(
    [
        Output(
            {
                'type': 'index-user-manage-user-list-table-update-store',
                'index': '新增用户'
            },
            'data'
        ),
        Output('index-user-manage-add-user-message-container', 'children')],
    Input('index-user-manage-add-user-confirm', 'nClicks'),
    [State('index-user-manage-add-user-username', 'value'),
     State('index-user-manage-add-user-password', 'value'),
     State('index-user-manage-add-user-gender', 'value')],
    prevent_initiall_call=True
)
def index_user_manage_add_user(nClicks, username, password, gender):

    if nClicks:

        if all([nClicks, username, password, gender]):
            # 检查用户名是否重复
            if UserAccount.check_user_exists(username).get('message') == '用户不存在':
                (
                    UserAccount
                    .create(
                        username=username,
                        gender=gender,
                        role='普通用户',
                        password=password,
                        password_md5=str2md5(password),
                        register_time=datetime.now()
                    )
                )

                return [
                    {
                        'timestamp': time.time()
                    },
                    fac.AntdMessage(
                        type='success',
                        content='添加成功'
                    )
                ]

            return [
                dash.no_update,
                fac.AntdMessage(
                    type='error',
                    content='用户名已存在'
                )
            ]

        return [
            dash.no_update,
            fac.AntdMessage(
                type='error',
                content='请完善信息'
            )
        ]

    return dash.no_update


@app.callback(
    [
        Output(
            {
                'type': 'index-user-manage-user-list-table-update-store',
                'index': '删除用户'
            },
            'data'
        ),
        Output('index-user-manage-delete-user-message-container', 'children')
    ],
    Input('index-user-manage-delete-user', 'confirmCounts'),
    State('index-user-manage-user-list-table', 'selectedRowKeys')
)
def index_user_manage_delete_selected_user(confirmCounts, selectedRowKeys):

    if confirmCounts:
        if selectedRowKeys:

            (
                UserAccount
                .delete()
                .where(UserAccount.username.in_(selectedRowKeys))
                .execute()
            )

            return [
                {
                    'timestamp': time.time()
                },
                fac.AntdMessage(
                    type='success',
                    content='删除完成'
                )
            ]

        return [
            dash.no_update,
            fac.AntdMessage(
                type='warning',
                content='请先选择要删除的用户'
            )
        ]

    return dash.no_update


@app.callback(
    Output('index-side-menu', 'currentKey'),
    Input('url', 'hash')
)
def index_update_current_key(hash):

    if hash == '':
        return '首页'

    return '子应用' + re.sub('^#sub-app', '', hash)


@app.callback(
    Output('index-main-content-container', 'children'),
    Input('url', 'hash'),
    State('url', 'pathname'),
)
def index_render_main_content(hash, pathname):

    if pathname == '/':

        if hash == '':
            return [
                fac.AntdSpace(
                    [
                        fac.AntdResult(
                            status='info',
                            title='欢迎来到首页',
                            style={
                                'boxShadow': '0 6px 16px rgb(107 147 224 / 14%)'
                            }
                        )
                    ] * 20,
                    direction='vertical',
                    size='large',
                    style={
                        'width': '100%'
                    }
                ),
                fac.AntdBackTop()
            ]

        elif hash[1:] not in RouterConfig.VALID_HASH:
            return fac.AntdResult(
                status='404',
                subTitle='您访问的页面不存在！'
            )

        # 检查当前用户是否有权限访问当前应用
        elif hash[1:] in current_user.accessible_apps:

            return [
                fac.AntdSpace(
                    [
                        fac.AntdResult(
                            status='info',
                            title=f'欢迎来到{hash[1:]}',
                            style={
                                'boxShadow': '0 6px 16px rgb(107 147 224 / 14%)'
                            }
                        )
                    ] * 20,
                    direction='vertical',
                    size='large',
                    style={
                        'width': '100%'
                    }
                ),
                fac.AntdBackTop()
            ]

        # 否则提示无权限访问
        return fac.AntdResult(
            status='403',
            subTitle='您没有权限访问当前应用！'
        )

    return dash.no_update
