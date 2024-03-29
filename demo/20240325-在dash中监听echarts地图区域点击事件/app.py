import dash
import json
from dash import html, dcc
import feffery_antd_charts as fact
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, ClientsideFunction

from mock_data import MockData

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True
)

app.title = 'XX地区XXX专题数据库'

app.layout = html.Div(
    [
        # 注入辅助用数据
        dcc.Store(
            id='map-data',
            data=json.load(open('./demo_map.json', encoding='utf-8'))
        ),

        # echarts事件同步dash示例目标
        html.Div(id='echarts-sync-event'),

        # 页首
        html.Div(
            [
                fac.AntdText(
                    'XX地区XXX专题数据库',
                    strong=True,
                    style={
                        'fontSize': 36,
                        'position': 'absolute',
                        'left': 25,
                        'top': '50%',
                        'transform': 'translateY(-50%)',
                        'fontFamily': 'SimHei'
                    }
                ),

                fac.AntdMenu(
                    id='header-menu',
                    menuItems=[
                        {
                            'component': 'Item',
                            'props': {
                                'title': level1,
                                'key': level1
                            }
                        }
                        for level1 in [
                            '人口发展', '经济发展', '公共服务', '基础设施'
                        ]
                    ],
                    defaultSelectedKey='人口发展',
                    mode='horizontal',
                    style={
                        'borderBottom': 'none',
                        'width': 'fit-content',
                        'paddingLeft': 25,
                        'paddingRight': 25,
                        'position': 'absolute',
                        'left': '50%',
                        'top': '50%',
                        'transform': 'translate(-50%, -50%)'
                    }
                )
            ],
            style={
                'height': 64,
                'borderBottom': '1px solid #f0f2f6',
                'position': 'relative'
            }
        ),

        # 总结图表栏
        fac.AntdRow(
            [
                fac.AntdCol(
                    fact.AntdPie(
                        data=MockData.mock_pie_data(),
                        angleField='value',
                        colorField='type',
                        innerRadius=0.75,
                        radius=0.85,
                        statistic={
                            'title': {
                                'content': level1
                            },
                            'content': {
                                'content': 'xx.xx%'
                            }
                        },
                        label=False
                    ),
                    span=6,
                    style={
                        'padding': 10
                    }
                )
                for level1 in [
                    '人口发展', '经济发展', '公共服务', '基础设施'
                ]
            ],
            wrap=False,
            style={
                'paddingLeft': 25,
                'paddingRight': 25,
                'height': 'calc((100vh - 64px) * 0.25)',
                'boxShadow': 'rgba(0, 0, 0, 0.12) 0px 6px 12px -5px'
            }
        ),

        html.Div(
            [
                # 左侧四川地区指标,
                fuc.FefferyDiv(
                    [
                        html.Div(
                            fac.AntdText(
                                'A地区人口指标',
                                style={
                                    'borderBottom': '3px solid #4dacfa',
                                    'fontSize': 20,
                                    'display': 'block',
                                    'transform': 'translateY(3px)',
                                    'fontFamily': '微软雅黑'
                                }
                            ),
                            style={
                                'paddingRight': 100,
                                'borderBottom': '3px solid #d8d8d8',
                                'display': 'inline-block',
                                'marginBottom': 25
                            }
                        ),
                        # 多指标图表
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    fac.AntdTabs(
                                        items=[
                                            {
                                                'label': f'指标{i}',
                                                'key': f'指标{i}'
                                            }
                                            for i in range(1, 21)
                                        ],
                                        tabPosition='left'
                                    ),
                                    flex='none',
                                    style={
                                        'height': 'calc((100vh - 64px) * 0.75 / 2 - 100px)',
                                        'overflowY': 'auto'
                                    }
                                ),
                                fac.AntdCol(
                                    fact.AntdBar(
                                        data=sorted(
                                            MockData.mock_bar_data(),
                                            key=lambda x: x['销售额'],
                                            reverse=True
                                        ),
                                        isGroup=True,
                                        xField='销售额',
                                        yField='城市',
                                        marginRatio=0,
                                        scrollbar={
                                            'type': 'vertical',
                                        }
                                    ),
                                    flex='auto',
                                    style={
                                        'height': 'calc((100vh - 64px) * 0.75 / 2 - 100px)',
                                        'paddingLeft': 5
                                    }
                                )
                            ],
                            wrap=False,
                            style={
                                'marginBottom': 15
                            }
                        ),

                        html.Div(
                            fac.AntdText(
                                'A地区人口指标',
                                style={
                                    'borderBottom': '3px solid #4dacfa',
                                    'fontSize': 20,
                                    'display': 'block',
                                    'transform': 'translateY(3px)',
                                    'fontFamily': '微软雅黑'
                                }
                            ),
                            style={
                                'paddingRight': 100,
                                'borderBottom': '3px solid #d8d8d8',
                                'display': 'inline-block',
                                'marginBottom': 25
                            }
                        ),
                        # 多指标图表
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    fac.AntdTabs(
                                        items=[
                                            {
                                                'label': f'指标{i}',
                                                'key': f'指标{i}'
                                            }
                                            for i in range(1, 21)
                                        ],
                                        tabPosition='left'
                                    ),
                                    flex='none',
                                    style={
                                        'height': 'calc((100vh - 64px) * 0.75 / 2 - 100px)',
                                        'overflowY': 'auto'
                                    }
                                ),
                                fac.AntdCol(
                                    fact.AntdBar(
                                        data=sorted(
                                            MockData.mock_bar_data(),
                                            key=lambda x: x['销售额'],
                                            reverse=True
                                        ),
                                        isGroup=True,
                                        xField='销售额',
                                        yField='城市',
                                        marginRatio=0,
                                        scrollbar={
                                            'type': 'vertical',
                                        }
                                    ),
                                    flex='auto',
                                    style={
                                        'height': 'calc((100vh - 64px) * 0.75 / 2 - 100px)',
                                        'paddingLeft': 5
                                    }
                                )
                            ],
                            wrap=False
                        )
                    ],
                    style={
                        'width': '27.5%',
                        'position': 'absolute',
                        'top': 15,
                        'bottom': 15,
                        'left': 20
                    }
                ),

                # 右侧重庆地区指标,
                fuc.FefferyDiv(
                    [
                        html.Div(
                            fac.AntdText(
                                'B地区人口指标',
                                style={
                                    'borderBottom': '3px solid #4dacfa',
                                    'fontSize': 20,
                                    'display': 'block',
                                    'transform': 'translateY(3px)',
                                    'fontFamily': '微软雅黑'
                                }
                            ),
                            style={
                                'paddingRight': 100,
                                'borderBottom': '3px solid #d8d8d8',
                                'display': 'inline-block',
                                'marginBottom': 25
                            }
                        ),
                        # 多指标图表
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    fact.AntdBar(
                                        data=sorted(
                                            MockData.mock_bar_data(),
                                            key=lambda x: x['销售额'],
                                            reverse=True
                                        ),
                                        isGroup=True,
                                        xField='销售额',
                                        yField='城市',
                                        marginRatio=0,
                                        scrollbar={
                                            'type': 'vertical',
                                        }
                                    ),
                                    flex='auto',
                                    style={
                                        'height': 'calc((100vh - 64px) * 0.75 / 2 - 100px)',
                                        'paddingLeft': 5
                                    }
                                ),
                                fac.AntdCol(
                                    fac.AntdTabs(
                                        items=[
                                            {
                                                'label': f'指标{i}',
                                                'key': f'指标{i}'
                                            }
                                            for i in range(1, 21)
                                        ],
                                        tabPosition='left'
                                    ),
                                    flex='none',
                                    style={
                                        'height': 'calc((100vh - 64px) * 0.75 / 2 - 100px)',
                                        'overflowY': 'auto'
                                    }
                                )
                            ],
                            wrap=False,
                            style={
                                'marginBottom': 15
                            }
                        ),

                        html.Div(
                            fac.AntdText(
                                'B地区人口指标',
                                style={
                                    'borderBottom': '3px solid #4dacfa',
                                    'fontSize': 20,
                                    'display': 'block',
                                    'transform': 'translateY(3px)',
                                    'fontFamily': '微软雅黑'
                                }
                            ),
                            style={
                                'paddingRight': 100,
                                'borderBottom': '3px solid #d8d8d8',
                                'display': 'inline-block',
                                'marginBottom': 25
                            }
                        ),
                        # 多指标图表
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    fact.AntdBar(
                                        data=sorted(
                                            MockData.mock_bar_data(),
                                            key=lambda x: x['销售额'],
                                            reverse=True
                                        ),
                                        isGroup=True,
                                        xField='销售额',
                                        yField='城市',
                                        marginRatio=0,
                                        scrollbar={
                                            'type': 'vertical',
                                        }
                                    ),
                                    flex='auto',
                                    style={
                                        'height': 'calc((100vh - 64px) * 0.75 / 2 - 100px)',
                                        'paddingLeft': 5
                                    }
                                ),
                                fac.AntdCol(
                                    fac.AntdTabs(
                                        items=[
                                            {
                                                'label': f'指标{i}',
                                                'key': f'指标{i}'
                                            }
                                            for i in range(1, 21)
                                        ],
                                        tabPosition='left'
                                    ),
                                    flex='none',
                                    style={
                                        'height': 'calc((100vh - 64px) * 0.75 / 2 - 100px)',
                                        'overflowY': 'auto'
                                    }
                                )
                            ],
                            wrap=False
                        )
                    ],
                    style={
                        'width': '27.5%',
                        'position': 'absolute',
                        'top': 15,
                        'bottom': 15,
                        'right': 20
                    }
                ),

                # 地图
                html.Div(
                    id='map-container',
                    style={
                        'position': 'absolute',
                        'width': '40%',
                        'left': '50%',
                        'transform': 'translateX(-50%)',
                        'top': 15,
                        'bottom': 15
                    }
                )
            ],
            style={
                'height': 'calc((100vh - 64px) * 0.75)',
                'position': 'relative'
            }
        )
    ]
)

app.clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='render_map'
    ),
    Output('map-container', 'children'),
    Input('map-data', 'data')
)


if __name__ == '__main__':
    app.run(debug=True)
