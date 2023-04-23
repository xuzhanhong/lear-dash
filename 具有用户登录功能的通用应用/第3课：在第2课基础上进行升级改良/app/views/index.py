from dash import html
import feffery_utils_components as fuc
import feffery_antd_components as fac

import callbacks.index_c
from models.auth import UserAccount


def render_content(username, gender, role, register_time, accessible_apps):

    # 根据用户名获取密码信息
    password = list(
        UserAccount
        .select()
        .where(UserAccount.username == username)
        .dicts()
    )[0]['password']

    return fuc.FefferyTopProgress(
        html.Div(
            [
                # 消息提示
                html.Div(id='index-user-manage-delete-user-message-container'),

                # 重定向容器
                html.Div(id='index-redirect-container'),

                # 注入相关modal
                html.Div(
                    [
                        # 个人资料面板
                        fac.AntdModal(
                            [
                                fac.AntdForm(
                                    [
                                        fac.AntdFormItem(
                                            fac.AntdText(
                                                username,
                                                copyable=True
                                            ),
                                            label='用户名'
                                        ),
                                        fac.AntdFormItem(
                                            fac.AntdText(
                                                gender,
                                                copyable=True
                                            ),
                                            label='性别'
                                        ),
                                        fac.AntdFormItem(
                                            fac.AntdText(
                                                password,
                                                copyable=True
                                            ),
                                            label='密码'
                                        ),
                                        fac.AntdFormItem(
                                            fac.AntdText(
                                                register_time
                                                .strftime(
                                                    '%Y-%m-%d %H:%M:%S'
                                                ),
                                                copyable=True
                                            ),
                                            label='注册时间'
                                        )
                                    ],
                                    labelCol={
                                        'span': 4
                                    }
                                )
                            ],
                            id='index-personal-info-modal',
                            title='个人资料',
                            mask=False
                        ),

                        # 用户角色为管理员时注入用户管理modal
                        *(
                            [
                                fac.AntdModal(
                                    fac.AntdSkeleton(
                                        html.Div(
                                            id='index-user-manage-modal-children-container'
                                        ),
                                        active=True,
                                        listenPropsMode='include',
                                        includeProps=[
                                            'index-user-manage-modal-children-container.children'
                                        ]
                                    ),
                                    id='index-user-manage-modal',
                                    title='用户管理',
                                    mask=False,
                                    width=800
                                )
                            ] if role == '管理员' else []
                        )
                    ]
                ),

                # 平台主页面页首
                fac.AntdRow(
                    [
                        # 页首左侧标题区域
                        fac.AntdCol(
                            html.Div(
                                fac.AntdText(
                                    'XXXXXX平台',
                                    style={
                                        'fontSize': '45px',
                                        'paddingLeft': '20px'
                                    }
                                ),
                                style={
                                    'height': '100%',
                                    'display': 'flex',
                                    'alignItems': 'center'
                                }
                            )
                        ),

                        # 页首右侧用户信息区域
                        fac.AntdCol(
                            fac.AntdSpace(
                                [
                                    fac.AntdTooltip(
                                        fac.AntdAvatar(
                                            mode='text',
                                            size=36,
                                            text=username,
                                            style={
                                                'background': 'gold' if role == '管理员' else (
                                                    '#3498db' if gender == '男' else '#ff6b81'
                                                )
                                            }
                                        ),
                                        title='当前用户：'+username,
                                        placement='bottom'
                                    ),

                                    fac.AntdDropdown(
                                        id='index-header-dropdown',
                                        title='个人中心',
                                        arrow=True,
                                        menuItems=[
                                            {
                                                'title': '个人资料',
                                                'key': '个人资料'
                                            },
                                            *(
                                                [
                                                    {
                                                        'title': '用户管理',
                                                        'key': '用户管理'
                                                    }
                                                ]
                                                if role == '管理员'
                                                else []
                                            ),
                                            {
                                                'isDivider': True
                                            },
                                            {
                                                'title': '退出登录',
                                                'key': '退出登录'
                                            },
                                        ],
                                        placement='bottomRight',
                                        overlayStyle={
                                            'width': '125px'
                                        }
                                    )
                                ],
                                style={
                                    'height': '100%',
                                    'float': 'right',
                                    'paddingRight': '50px',
                                    'display': 'flex',
                                    'alignItems': 'center'
                                }
                            ),
                            flex=1
                        )
                    ],
                    style={
                        'height': '64px',
                        'boxShadow': 'rgb(240 241 242) 0px 2px 14px',
                        'background': 'white',
                        'marginBottom': '5px',
                        'position': 'sticky',
                        'top': 0,
                        'zIndex': 999
                    }
                ),

                fac.AntdRow(
                    [
                        # 左侧固定菜单区域
                        fac.AntdCol(
                            fac.AntdAffix(
                                html.Div(
                                    fac.AntdMenu(
                                        id='index-side-menu',
                                        menuItems=[
                                            {
                                                'component': 'Item',
                                                'props': {
                                                    'key': '首页',
                                                    'title': '首页',
                                                    'icon': 'antd-home',
                                                    'href': '/'
                                                }
                                            },
                                            {
                                                'component': 'SubMenu',
                                                'props': {
                                                    'key': '子应用',
                                                    'title': '子应用',
                                                    'icon': 'antd-app-store'
                                                },
                                                'children': [
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'key': f'子应用{i}',
                                                            'title': f'子应用{i}',
                                                            'icon': 'antd-app-store',
                                                            'href': f'#sub-app{i}'
                                                        }
                                                    }
                                                    for i in range(1, 25)
                                                    if f'sub-app{i}' in accessible_apps
                                                ]
                                            }
                                        ],
                                        mode='inline',
                                        openKeys=['子应用'],
                                        style={
                                            'width': '100%',
                                            'height': '100%'
                                        }
                                    ),
                                    style={
                                        'width': '250px',
                                        'height': 'calc(100vh - 69px)',
                                        'overflowY': 'auto',
                                        'transition': 'width 0.2s'
                                    }
                                ),
                                offsetTop=69.1
                            ),
                            flex='none'
                        ),

                        # 右侧主体内容区域
                        fac.AntdCol(
                            [
                                html.Div(
                                    id='index-main-content-container',
                                    style={
                                        'padding': '25px',
                                    }
                                )
                            ],
                            flex='auto'
                        )
                    ],
                    wrap=False
                )
            ]
        ),
        listenPropsMode='include',
        includeProps=[
            'index-main-content-container.children'
        ]
    )
