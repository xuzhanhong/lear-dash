import dash
from dash import html, dcc
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

import views
from server import app

app.layout = html.Div(
    [
        # 注入url监听
        dcc.Location(
            id='url'
        ),

        # 页面内容容器
        fac.AntdConfigProvider(
            fac.AntdRow(
                [
                    # 侧边菜单
                    fac.AntdCol(
                        fac.AntdAffix(
                            html.Div(
                                [
                                    # logo+标题+菜单栏
                                    fac.AntdSpace(
                                        [
                                            # logo+标题
                                            fac.AntdSpace(
                                                [
                                                    fac.AntdImage(
                                                        src=dash.get_asset_url(
                                                            './imgs/logo.svg'),
                                                        height=50,
                                                        preview=False
                                                    ),
                                                    fac.AntdSpace(
                                                        [
                                                            fac.AntdText(
                                                                '产品名称',
                                                                italic=True,
                                                                strong=True,
                                                                style={
                                                                    'fontSize': 28
                                                                }
                                                            ),
                                                            fac.AntdText(
                                                                '供应商平台',
                                                                strong=True,
                                                                style={
                                                                    'color': '#adb5bd',
                                                                    'fontSize': 15
                                                                }
                                                            )
                                                        ],
                                                        direction='vertical',
                                                        size=0
                                                    )
                                                ],
                                                style={
                                                    'width': '100%',
                                                    'padding': '20px 30px'
                                                }
                                            ),

                                            # 与侧边菜单栏绑定的样式
                                            fuc.FefferyStyle(
                                                rawStyle='''
#side-menu {
    background: transparent !important;
}

#side-menu .ant-menu-item-selected {
    background: #335efb !important;
    color: white !important;
    border-radius: 6px;
}

#side-menu .ant-menu-item-selected * {
    color: white !important;
}

#side-menu .ant-menu-item {
    border-radius: 6px;
}

#side-menu .ant-menu-item-selected::after {
    border-right: none !important;
}
'''
                                            ),

                                            # 菜单栏
                                            fac.AntdMenu(
                                                id='side-menu',
                                                mode='inline',
                                                menuItems=[
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'title': '数据总览',
                                                            'key': '数据总览',
                                                            'icon': 'antd-dashboard',
                                                            'href': '/'
                                                        }
                                                    },
                                                    {
                                                        'component': 'Item',
                                                        'props': {
                                                            'title': '商品管理',
                                                            'icon': 'antd-shopping-cart'
                                                        }
                                                    },
                                                    {
                                                        'component': 'SubMenu',
                                                        'props': {
                                                            'title': '订单管理',
                                                            'icon': 'antd-file-add'
                                                        },
                                                        'children': []
                                                    },
                                                    {
                                                        'component': 'SubMenu',
                                                        'props': {
                                                            'title': '物流工具',
                                                            'icon': 'antd-car'
                                                        },
                                                        'children': []
                                                    },
                                                    {
                                                        'component': 'SubMenu',
                                                        'props': {
                                                            'title': '账户安全',
                                                            'icon': 'antd-insurance'
                                                        },
                                                        'children': []
                                                    },
                                                    {
                                                        'component': 'SubMenu',
                                                        'props': {
                                                            'title': '通知公告',
                                                            'icon': 'antd-notification'
                                                        },
                                                        'children': []
                                                    },
                                                    {
                                                        'component': 'SubMenu',
                                                        'props': {
                                                            'title': '个人中心',
                                                            'icon': 'antd-user'
                                                        }
                                                    }
                                                ],
                                                defaultSelectedKey='数据总览',
                                                style={
                                                    'padding': '0 20px'
                                                }
                                            )
                                        ],
                                        direction='vertical',
                                        style={
                                            'width': '100%'
                                        }
                                    ),

                                    # 底部联系方式
                                    fac.AntdRow(
                                        [
                                            fac.AntdCol(
                                                fac.AntdSpace(
                                                    [
                                                        fac.AntdIcon(
                                                            icon='antd-phone'
                                                        ),
                                                        '咨询电话'
                                                    ]
                                                )
                                            ),

                                            fac.AntdCol(
                                                '400****666'
                                            )
                                        ],
                                        justify='space-between',
                                        align='middle',
                                        style={
                                            'position': 'absolute',
                                            'bottom': 0,
                                            'background': '#f0effd',
                                            'width': '100%',
                                            'padding': '20px 20px',
                                            'color': '#a6a9b6'
                                        }
                                    )
                                ],
                                style={
                                    'width': 250,
                                    'background': '#f8f9fd',
                                    'height': '100vh',
                                    'position': 'relative'
                                }
                            ),
                            offsetTop=0
                        ),
                        flex='none'
                    ),

                    # 主体内容区域
                    fac.AntdCol(
                        id='main-container',
                        flex='auto'
                    )
                ],
                wrap=False
            ),
            primaryColor='#335efb'
        )
    ]
)


@app.callback(
    [Output('main-container', 'children'),
     Output('side-menu', 'currentKey')],
    Input('url', 'pathname')
)
def render_main_container(pathname):

    if pathname == '/':

        return [
            views.index.render(),
            '数据总览'
        ]

    return [
        fac.AntdParagraph(
            [
                '当前页面不存在或正在开发中，',
                dcc.Link(
                    '回首页',
                    href='/'
                )
            ]
        ),
        None
    ]


if __name__ == '__main__':
    app.run(debug=True)
