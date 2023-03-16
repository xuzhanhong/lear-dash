import dash
import time
import random
from dash import html
import feffery_antd_charts as fact
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('time-range-content-container', 'children'),
    Input('time-range-tabs', 'activeKey')
)
def index_render_time_range_content(activeKey):

    time.sleep(1)  # 提升系统动画效果 ^_^

    return [
        fac.AntdRow(
            [
                fac.AntdCol(
                    fuc.FefferyDiv(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdText(
                                        item['name'],
                                        type='secondary'
                                    ),
                                    fac.AntdText(
                                        item['value'],
                                        strong=True,
                                        style={
                                            'fontSize': 28
                                        }
                                    )
                                ],
                                direction='vertical',
                                size='small'
                            ),
                            fac.AntdSpace(
                                [
                                    fac.AntdText(
                                        str(abs(item['change']))+'%',
                                        strong=True
                                    ),
                                    fac.AntdIcon(
                                        icon=(
                                            'antd-arrow-up'
                                            if item['change'] >= 0
                                            else 'antd-arrow-down'
                                        ),
                                        style={
                                            'color': (
                                                '#65a893'
                                                if item['change'] >= 0
                                                else '#c0b382'
                                            )
                                        }
                                    )
                                ],
                                style={
                                    'position': 'absolute',
                                    'right': 25,
                                    'bottom': 25
                                }
                            )
                        ],
                        shadow='always-shadow',
                        style={
                            'borderRadius': 8,
                            'height': 120,
                            'border': '1px solid #e9ecef',
                            'padding': '25px 30px',
                            'position': 'relative'
                        }
                    ),
                    span=4
                )
                for item in [
                    {
                        'name': '订单数量',
                        'value': 5504,
                        'change': 12.3
                    },
                    {
                        'name': '退单数量',
                        'value': 103,
                        'change': -11.2
                    },
                    {
                        'name': '供应金额',
                        'value': 7504.2,
                        'change': 26.4
                    },
                    {
                        'name': '退款金额',
                        'value': 2305,
                        'change': 6.5
                    },
                    {
                        'name': '竞价成功',
                        'value': 1743,
                        'change': 18.7
                    },
                    {
                        'name': '竞价失败',
                        'value': 752,
                        'change': 1.5
                    }
                ]
            ],
            gutter=15,
            style={
                'marginBottom': 25
            }
        ),

        fuc.FefferyDiv(
            [
                fac.AntdSpace(
                    [
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    fac.AntdText(
                                        '订单数量',
                                        strong=True,
                                        style={
                                            'fontSize': 16
                                        }
                                    )
                                ),
                                fac.AntdCol(
                                    fac.AntdRadioGroup(
                                        options=[
                                            {
                                                'label': '上期',
                                                'value': '上期'
                                            },
                                            {
                                                'label': '本期',
                                                'value': '本期'
                                            }
                                        ],
                                        defaultValue='本期'
                                    )
                                )
                            ],
                            justify='space-between'
                        ),

                        # 折线图
                        fact.AntdArea(
                            data=[
                                {
                                    '月份': f'{i}月',
                                    '数值': random.randint(5000, 10000)
                                }
                                for i in range(1, 13)
                            ],
                            xField='月份',
                            yField='数值',
                            areaStyle={
                                'fill': 'l(270) 0:#ffffff 0.5:#f0effd 1:#335efb'
                            },
                            xAxis={
                                'range': [0, 1]
                            },
                            smooth=True,
                            style={
                                'height': 300
                            }
                        )
                    ],
                    direction='vertical',
                    style={
                        'width': '100%'
                    }
                )
            ],
            shadow='always-shadow',
            style={
                'padding': 25,
                'borderRadius': 8,
                'marginBottom': 25
            }
        ),

        fac.AntdRow(
            [
                fac.AntdCol(
                    fuc.FefferyDiv(
                        [
                            fac.AntdRow(
                                [
                                    fac.AntdCol(
                                        fac.AntdImage(
                                            src=dash.get_asset_url(
                                                './imgs/订单logo.svg'),
                                            height=50,
                                            preview=False
                                        ),
                                        flex='none'
                                    ),

                                    fac.AntdCol(
                                        fac.AntdSpace(
                                            [
                                                fac.AntdText(
                                                    '订单',
                                                    strong=True,
                                                    style={
                                                        'fontSize': 16
                                                    }
                                                ),
                                                fac.AntdRow(
                                                    [
                                                        fac.AntdCol(
                                                            fac.AntdText(
                                                                '待发货订单',
                                                                type='secondary'
                                                            )
                                                        ),
                                                        fac.AntdCol(
                                                            fac.AntdText(
                                                                213,
                                                                type='secondary',
                                                                strong=True
                                                            )
                                                        )
                                                    ],
                                                    justify='space-between'
                                                ),
                                                fac.AntdRow(
                                                    [
                                                        fac.AntdCol(
                                                            fac.AntdText(
                                                                '售后中订单',
                                                                type='secondary'
                                                            )
                                                        ),
                                                        fac.AntdCol(
                                                            fac.AntdText(
                                                                17,
                                                                type='secondary',
                                                                strong=True
                                                            )
                                                        )
                                                    ],
                                                    justify='space-between'
                                                )
                                            ],
                                            size='small',
                                            direction='vertical',
                                            style={
                                                'width': '100%'
                                            }
                                        ),
                                        flex='auto'
                                    )
                                ],
                                gutter=25
                            )
                        ],
                        shadow='always-shadow',
                        style={
                            'borderRadius': 8,
                            'height': 175,
                            'border': '1px solid #e9ecef',
                            'padding': '25px 30px',
                            'position': 'relative'
                        }
                    ),
                    span=6
                ),

                fac.AntdCol(
                    fuc.FefferyDiv(
                        [
                            fac.AntdRow(
                                [
                                    fac.AntdCol(
                                        fac.AntdImage(
                                            src=dash.get_asset_url(
                                                './imgs/账户logo.svg'),
                                            height=50,
                                            preview=False
                                        ),
                                        flex='none'
                                    ),

                                    fac.AntdCol(
                                        fac.AntdSpace(
                                            [
                                                fac.AntdText(
                                                    '账户',
                                                    strong=True,
                                                    style={
                                                        'fontSize': 16
                                                    }
                                                ),
                                                fac.AntdRow(
                                                    [
                                                        fac.AntdCol(
                                                            fac.AntdText(
                                                                '可提现金额',
                                                                type='secondary'
                                                            )
                                                        ),
                                                        fac.AntdCol(
                                                            fac.AntdText(
                                                                '￥17423.47',
                                                                type='secondary',
                                                                strong=True
                                                            )
                                                        )
                                                    ],
                                                    justify='space-between'
                                                ),
                                                fac.AntdRow(
                                                    [
                                                        fac.AntdCol(
                                                            fac.AntdText(
                                                                '未提现金额',
                                                                type='secondary'
                                                            )
                                                        ),
                                                        fac.AntdCol(
                                                            fac.AntdText(
                                                                '￥894',
                                                                type='secondary',
                                                                strong=True
                                                            )
                                                        )
                                                    ],
                                                    justify='space-between'
                                                )
                                            ],
                                            size='small',
                                            direction='vertical',
                                            style={
                                                'width': '100%'
                                            }
                                        ),
                                        flex='auto'
                                    )
                                ],
                                gutter=25
                            )
                        ],
                        shadow='always-shadow',
                        style={
                            'borderRadius': 8,
                            'height': 175,
                            'border': '1px solid #e9ecef',
                            'padding': '25px 30px',
                            'position': 'relative'
                        }
                    ),
                    span=6
                ),

                fac.AntdCol(
                    fuc.FefferyDiv(
                        [
                            fac.AntdRow(
                                [
                                    fac.AntdCol(
                                        fac.AntdImage(
                                            src=dash.get_asset_url(
                                                './imgs/评分logo.svg'),
                                            height=50,
                                            preview=False
                                        ),
                                        flex='none'
                                    ),

                                    fac.AntdCol(
                                        fac.AntdSpace(
                                            [
                                                fac.AntdText(
                                                    'DSR商家评分',
                                                    strong=True,
                                                    style={
                                                        'fontSize': 16
                                                    }
                                                ),
                                                fac.AntdRow(
                                                    [
                                                        fac.AntdCol(
                                                            fac.AntdText(
                                                                '质量描述',
                                                                type='secondary'
                                                            )
                                                        ),
                                                        fac.AntdCol(
                                                            fac.AntdSpace(
                                                                [
                                                                    fac.AntdText(
                                                                        '5.0',
                                                                        strong=True
                                                                    ),
                                                                    fac.AntdRate(
                                                                        value=5,
                                                                        count=5,
                                                                        allowHalf=True,
                                                                        disabled=True,
                                                                        style={
                                                                            'fontSize': 15,
                                                                            'lineHeight': '15px'
                                                                        }
                                                                    )
                                                                ],
                                                                size='small'
                                                            )
                                                        )
                                                    ],
                                                    justify='space-between',
                                                    align='middle'
                                                ),
                                                fac.AntdRow(
                                                    [
                                                        fac.AntdCol(
                                                            fac.AntdText(
                                                                '物流包装',
                                                                type='secondary'
                                                            )
                                                        ),
                                                        fac.AntdCol(
                                                            fac.AntdSpace(
                                                                [
                                                                    fac.AntdText(
                                                                        '3.5',
                                                                        strong=True
                                                                    ),
                                                                    fac.AntdRate(
                                                                        value=3.5,
                                                                        count=5,
                                                                        allowHalf=True,
                                                                        disabled=True,
                                                                        style={
                                                                            'fontSize': 15,
                                                                            'lineHeight': '15px'
                                                                        }
                                                                    )
                                                                ],
                                                                size='small'
                                                            )
                                                        )
                                                    ],
                                                    justify='space-between',
                                                    align='middle'
                                                ),
                                                fac.AntdRow(
                                                    [
                                                        fac.AntdCol(
                                                            fac.AntdText(
                                                                '客服售后',
                                                                type='secondary'
                                                            )
                                                        ),
                                                        fac.AntdCol(
                                                            fac.AntdSpace(
                                                                [
                                                                    fac.AntdText(
                                                                        '4.0',
                                                                        strong=True
                                                                    ),
                                                                    fac.AntdRate(
                                                                        value=4,
                                                                        count=5,
                                                                        allowHalf=True,
                                                                        disabled=True,
                                                                        style={
                                                                            'fontSize': 15,
                                                                            'lineHeight': '15px'
                                                                        }
                                                                    )
                                                                ],
                                                                size='small'
                                                            )
                                                        )
                                                    ],
                                                    justify='space-between',
                                                    align='middle'
                                                ),
                                            ],
                                            size='small',
                                            direction='vertical',
                                            style={
                                                'width': '100%'
                                            }
                                        ),
                                        flex='auto'
                                    )
                                ],
                                gutter=25
                            )
                        ],
                        shadow='always-shadow',
                        style={
                            'borderRadius': 8,
                            'height': 175,
                            'border': '1px solid #e9ecef',
                            'padding': '25px 30px',
                            'position': 'relative'
                        }
                    ),
                    span=6
                ),

                fac.AntdCol(
                    fuc.FefferyDiv(
                        [
                            fac.AntdRow(
                                [
                                    fac.AntdCol(
                                        fac.AntdImage(
                                            src=dash.get_asset_url(
                                                './imgs/违规logo.svg'),
                                            height=50,
                                            preview=False
                                        ),
                                        flex='none'
                                    ),

                                    fac.AntdCol(
                                        fac.AntdSpace(
                                            [
                                                fac.AntdText(
                                                    '违规',
                                                    strong=True,
                                                    style={
                                                        'fontSize': 16
                                                    }
                                                ),
                                                fac.AntdRow(
                                                    [
                                                        fac.AntdCol(
                                                            fac.AntdText(
                                                                '发货超时',
                                                                type='secondary'
                                                            )
                                                        ),
                                                        fac.AntdCol(
                                                            fac.AntdText(
                                                                89,
                                                                type='secondary',
                                                                strong=True
                                                            )
                                                        )
                                                    ],
                                                    justify='space-between'
                                                ),
                                                fac.AntdRow(
                                                    [
                                                        fac.AntdCol(
                                                            fac.AntdText(
                                                                '售后纠纷',
                                                                type='secondary'
                                                            )
                                                        ),
                                                        fac.AntdCol(
                                                            fac.AntdText(
                                                                15,
                                                                type='secondary',
                                                                strong=True
                                                            )
                                                        )
                                                    ],
                                                    justify='space-between'
                                                ),
                                                fac.AntdRow(
                                                    [
                                                        fac.AntdCol(
                                                            fac.AntdText(
                                                                '违规包装',
                                                                type='secondary'
                                                            )
                                                        ),
                                                        fac.AntdCol(
                                                            fac.AntdText(
                                                                27,
                                                                type='secondary',
                                                                strong=True
                                                            )
                                                        )
                                                    ],
                                                    justify='space-between'
                                                )
                                            ],
                                            size='small',
                                            direction='vertical',
                                            style={
                                                'width': '100%'
                                            }
                                        ),
                                        flex='auto'
                                    )
                                ],
                                gutter=25
                            )
                        ],
                        shadow='always-shadow',
                        style={
                            'borderRadius': 8,
                            'height': 175,
                            'border': '1px solid #e9ecef',
                            'padding': '25px 30px',
                            'position': 'relative'
                        }
                    ),
                    span=6
                ),
            ],
            gutter=15,
            style={
                'marginBottom': 25
            }
        ),

        fuc.FefferyDiv(
            [
                fac.AntdSpace(
                    [
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    fac.AntdText(
                                        '供应商品数量',
                                        strong=True,
                                        style={
                                            'fontSize': 16
                                        }
                                    )
                                ),
                                fac.AntdCol(
                                    fac.AntdButton(
                                        [
                                            '查看更多',
                                            fac.AntdIcon(
                                                icon='antd-right'
                                            )
                                        ],
                                        type='link'
                                    )
                                )
                            ],
                            justify='space-between'
                        ),

                        # 与示例表格绑定的自定义样式
                        fuc.FefferyStyle(
                            rawStyle='''
#table-demo .ant-table-thead{
    background: #f9fafe !important;
}

#table-demo .ant-table-thead .ant-table-cell{
    font-weight: bold !important;
}
'''
                        ),
                        # 表格示例
                        fac.AntdTable(
                            id='table-demo',
                            columns=[
                                {
                                    'title': '商品名称',
                                    'dataIndex': '商品名称',
                                    'width': '40%',
                                    'align': 'left'
                                },
                                {
                                    'title': '浏览量',
                                    'dataIndex': '浏览量',
                                    'width': '10%',
                                    'align': 'left'
                                },
                                {
                                    'title': '下单总量',
                                    'dataIndex': '下单总量',
                                    'width': '10%',
                                    'align': 'left'
                                },
                                {
                                    'title': '下单总额',
                                    'dataIndex': '下单总额',
                                    'width': '10%',
                                    'align': 'left'
                                },
                                {
                                    'title': '我的供应数',
                                    'dataIndex': '我的供应数',
                                    'width': '10%',
                                    'align': 'left'
                                },
                                {
                                    'title': '我的供应链',
                                    'dataIndex': '我的供应链',
                                    'width': '10%',
                                    'align': 'left'
                                },
                                {
                                    'title': '供应状态',
                                    'dataIndex': '供应状态',
                                    'width': '10%',
                                    'align': 'left',
                                    'renderOptions': {
                                        'renderType': 'status-badge'
                                    }
                                }
                            ],
                            data=[
                                {
                                    '商品名称': 'x'*10,
                                    '浏览量': 'xxx',
                                    '下单总量': 'xxx',
                                    '下单总额': 'xxx',
                                    '我的供应数': 'xxx',
                                    '我的供应链': 'xxx',
                                    '供应状态': {
                                        'text': '部分在售',
                                        'status': 'processing'
                                    }
                                }
                            ] * 50
                        )
                    ],
                    direction='vertical',
                    style={
                        'width': '100%'
                    }
                )
            ],
            shadow='always-shadow',
            style={
                'padding': 25,
                'borderRadius': 8,
                'marginBottom': 25
            }
        ),
    ]
