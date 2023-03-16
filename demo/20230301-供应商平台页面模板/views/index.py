import dash
from dash import html, dcc
import feffery_antd_components as fac
import feffery_utils_components as fuc

# 绑定回调
import callbacks.index_c


def render():

    return fac.AntdCol(
        [
            # 内容区页首
            fac.AntdAffix(
                fac.AntdRow(
                    [
                        fac.AntdCol(
                            fac.AntdText(
                                '数据总览',
                                strong=True,
                                style={
                                    'fontSize': 22
                                }
                            )
                        ),

                        fac.AntdCol(
                            fac.AntdSpace(
                                [
                                    fac.AntdBadge(
                                        fac.AntdIcon(
                                            icon='antd-bell',
                                            style={
                                                'fontSize': 22
                                            }
                                        ),
                                        count=66,
                                        size='small'
                                    ),

                                    fac.AntdSpace(
                                        [
                                            fac.AntdAvatar(
                                                style={
                                                    'background': '#485ac1'
                                                }
                                            ),
                                            fac.AntdText(
                                                '用户：费弗里',
                                                style={
                                                    'color': '#c0c0c8'
                                                }
                                            )
                                        ],
                                        size='small'
                                    )
                                ],
                                size=40,
                                style={
                                    'paddingRight': 10
                                }
                            )
                        )
                    ],
                    justify='space-between',
                    style={
                        'padding': '20px 30px',
                        'boxShadow': 'rgb(240 241 242) 0px 2px 14px',
                        'background': 'white'
                    }
                ),
                offsetTop=0
            ),

            # 内容信息区域
            html.Div(
                [
                    fac.AntdTabs(
                        id='time-range-tabs',
                        items=[
                            {
                                'key': time_range,
                                'label': time_range
                            }
                            for time_range in [
                                '全部', '今天', '昨天', '本月', '上月'
                            ]
                        ],
                        tabBarGutter=40,
                        defaultActiveKey='全部'
                    ),

                    # 内容区域，与时间范围切换标签页联动
                    fac.AntdSpin(
                        html.Div(
                            id='time-range-content-container',
                            style={
                                'minHeight': 500
                            }
                        ),
                        indicator=fuc.FefferyExtraSpinner(
                            type='flag',
                            color='#335efb',
                            style={
                                'transform': 'translateY(150px)'
                            }
                        )
                    )
                ],
                style={
                    'padding': 25
                }
            )
        ],
        flex='auto'
    )
