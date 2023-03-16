import json
import random
from dash import html
import feffery_antd_charts as fact
import feffery_antd_components as fac
import feffery_leaflet_components as flc


def generate_demo_geojson():

    data = json.load(open('./demo-data/100000_full.json', encoding='utf-8'))

    # 提取部分省份
    data['features'] = [
        feature
        for feature in data['features']
        if feature['properties']['name'] in
        ['广东省', '福建省', '浙江省', '上海市', '台湾省', '江西省', '湖南省', '安徽省', '江苏省']
    ]

    # 构建随机示例属性字段
    for i in range(len(data['features'])):
        data['features'][i]['properties'] = {
            **data['features'][i]['properties'],
            'random_value': round(random.uniform(0.01, 1), 3)
        }

        data['features'][i]['properties']['tooltip'] = '{}，示例数值：{}'.format(
            data['features'][i]['properties']['name'],
            data['features'][i]['properties']['random_value']
        )

    return data


pie_demo_data = [
    {
        'type': '纯文本',
        'value': 148564,
    },
    {
        'type': '图文类',
        'value': 334271,
    },
    {
        'type': '视频类',
        'value': 445695,
    }
]


def render_content():

    return html.Div(
        [
            fac.AntdBreadcrumb(
                items=[
                    {
                        'title': '仪表盘',
                        'icon': 'antd-dashboard'
                    },
                    {
                        'title': '概览面板',
                        'href': '/#概览面板'
                    }
                ],
                style={
                    'marginBottom': '16px'
                }
            ),

            html.Div(
                [
                    fac.AntdParagraph(
                        '欢迎，用户Feffery',
                        style={
                            'fontSize': '20px'
                        }
                    ),

                    fac.AntdDivider(
                        lineColor='#e5e6eb'
                    ),

                    fac.AntdRow(
                        [
                            fac.AntdCol(
                                fac.AntdSpace(
                                    [
                                        fac.AntdAvatar(
                                            mode='icon',
                                            size=60,
                                            icon=item['icon'],
                                            style={
                                                'backgroundColor': '#f2f3f5',
                                                'fontSize': '36px'
                                            }
                                        ),
                                        fac.AntdSpace(
                                            [
                                                fac.AntdText(
                                                    item['title']
                                                ),
                                                html.Span(
                                                    [
                                                        fac.AntdText(
                                                            item['value'],
                                                            strong=True,
                                                            style={
                                                                'fontSize': '28px',
                                                                'paddingRight': '10px'
                                                            }
                                                        ),
                                                        fac.AntdText(
                                                            item['unit']
                                                        )
                                                    ]
                                                )
                                            ],
                                            direction='vertical',
                                            size=0
                                        )
                                    ]
                                ),
                                span=6,
                                style={
                                    'height': '100%',
                                    'borderRight': '1px solid #e5e6eb' if col < 3 else 'none',
                                    'display': 'flex',
                                    'justifyContent': 'center'
                                }
                            )
                            for col, item in enumerate(
                                # 示例数据
                                [
                                    {
                                        'icon': 'fc-document',
                                        'title': 'Total online data',
                                        'value': '373.5w+',
                                        'unit': 'pecs'
                                    },
                                    {
                                        'icon': 'fc-rules',
                                        'title': 'Content in market',
                                        'value': '368',
                                        'unit': 'pecs'
                                    },
                                    {
                                        'icon': 'fc-conference-call',
                                        'title': 'Comments',
                                        'value': '8874',
                                        'unit': 'pecs'
                                    },
                                    {
                                        'icon': 'fc-statistics',
                                        'title': 'Growth',
                                        'value': '2.8%',
                                        'unit': ''
                                    }
                                ]
                            )
                        ],
                        style={
                            'height': '70px'
                        }
                    ),

                    fac.AntdDivider(
                        lineColor='#e5e6eb'
                    ),

                    fac.AntdParagraph(
                        [
                            fac.AntdText(
                                'Content Data',
                                style={
                                    'fontSize': '22px',
                                    'paddingRight': '5px'
                                }
                            ),

                            fac.AntdText(
                                '(Nearly 1 Year)',
                                style={
                                    'color': '#86909c'
                                }
                            )
                        ]
                    ),

                    html.Div(
                        fact.AntdArea(
                            data=json.load(
                                open(
                                    './demo-data/1d565782-dde4-4bb6-8946-ea6a38ccf184.json')
                            ),
                            smooth=True,
                            xField='Date',
                            yField='scales',
                            areaStyle={
                                'func': '''
() => {
      return {
        fill: 'l(270) 0:#ffffff 0.5:#7ec2f3 1:#1890ff',
      };
    }'''
                            }
                        ),
                        style={
                            'height': '400px'
                        }
                    )
                ],
                style={
                    'background': 'white',
                    'marginBottom': '16px',
                    'borderRadius': '4px',
                    'padding': '20px'
                }
            ),

            fac.AntdRow(
                [
                    fac.AntdCol(
                        html.Div(
                            [
                                fac.AntdParagraph(
                                    [
                                        fac.AntdText(
                                            'Regional Sales',
                                            style={
                                                'fontSize': '22px',
                                                'paddingRight': '5px'
                                            }
                                        ),

                                        fac.AntdText(
                                            '(Nearly 1 Year)',
                                            style={
                                                'color': '#86909c'
                                            }
                                        )
                                    ]
                                ),

                                html.Div(
                                    flc.LeafletMap(
                                        [
                                            flc.LeafletTileLayer(),

                                            flc.LeafletGeoJSON(
                                                data=generate_demo_geojson(),
                                                mode='choropleth',
                                                featureValueField='random_value',
                                                showTooltip=True,
                                                featureValueToStyles={
                                                    'bins': [
                                                        [0, 0.33],
                                                        [0.33, 0.66],
                                                        [0.66, 1]
                                                    ],
                                                    'styles': [
                                                        {
                                                            'fillColor': '#ffccc7',
                                                            'fillOpacity': 1,
                                                            'weight': 1,
                                                            'color': 'white'
                                                        },
                                                        {
                                                            'fillColor': '#ff7875',
                                                            'fillOpacity': 1,
                                                            'weight': 1,
                                                            'color': 'white'
                                                        },
                                                        {
                                                            'fillColor': '#f5222d',
                                                            'fillOpacity': 1,
                                                            'weight': 1,
                                                            'color': 'white'
                                                        }
                                                    ]
                                                }
                                            )
                                        ],
                                        style={
                                            'height': '100%'
                                        }
                                    ),
                                    style={
                                        'height': 'calc(100% - 45px)'
                                    }
                                )
                            ],
                            style={
                                'background': 'white',
                                'borderRadius': '4px',
                                'height': '100%',
                                'padding': '20px'
                            }
                        ),
                        span=12,
                        style={
                            'paddingRight': '10px'
                        }
                    ),

                    fac.AntdCol(
                        html.Div(
                            [
                                fac.AntdParagraph(
                                    [
                                        fac.AntdText(
                                            'Percentage of content categories',
                                            style={
                                                'fontSize': '22px'
                                            }
                                        )
                                    ]
                                ),

                                html.Div(
                                    fact.AntdPie(
                                        data=pie_demo_data,
                                        angleField='value',
                                        colorField='type',
                                        radius=0.8,
                                        innerRadius=0.5,
                                        color=['#2ccfff',
                                               '#3c46ad',
                                               '#2fa3ff'],
                                        label={
                                            'type': 'spider',
                                            'style': {
                                                'fontSize': 18
                                            }
                                        },
                                        statistic={
                                            'title': {
                                                'content': '内容量'
                                            },
                                            'content': {
                                                'content': '928,530'
                                            }
                                        },
                                        legend={
                                            'position': 'bottom'
                                        }
                                    ),
                                    style={
                                        'height': 'calc(100% - 45px)'
                                    }
                                )
                            ],
                            style={
                                'background': 'white',
                                'borderRadius': '4px',
                                'height': '100%',
                                'padding': '20px'
                            }
                        ),
                        span=12,
                        style={
                            'paddingLeft': '10px'
                        }
                    )
                ],
                style={
                    'marginBottom': '16px',
                    'height': '600px'
                }
            ),

            fac.AntdDivider(isDashed=True),

            html.Div(
                fac.AntdText('玩转Dash知识星球出品'),
                style={
                    'textAlign': 'center'
                }
            )
        ],
        style={
            'padding': '25px 20px',
            'background': '#f2f3f5'
        }
    )
