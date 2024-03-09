from server import *
from dash import dcc
from dash import html
import feffery_antd_components as fac
from models.new_media_data import media_index_value_chart_data
from view.render_chart_control import render_one_chart
from callbacks.app_callback_control import media_indexValueDataAnalysis, media_indexValueContentData

# 指标卡数据（近七天最大值、最大值占比，环比等）
index_value_cardData_list = [
    ['品牌活跃度',
     media_indexValueDataAnalysis[0].get('seven_max'),
     f"{media_indexValueDataAnalysis[0].get('seven_qoq')[1]}",
     f"{media_indexValueDataAnalysis[0].get('seven_qoq')[4]}",
     {'type': 'circle', 'steps': 0, 'content': '40',
      'percent': media_indexValueDataAnalysis[0].get('seven_max_proportion'),
      'strokeColor': {'from': '#00F5A0', 'to': '#00D9F5'}},
     '近七天各平台日活曝光量（最大值、昨日、三日环比）'],
    ['微博-品牌活跃度',
     media_indexValueDataAnalysis[1].get('seven_max'),
     f"{media_indexValueDataAnalysis[1].get('seven_qoq')[1]}",
     f"{media_indexValueDataAnalysis[1].get('seven_qoq')[4]}",
     {'type': 'circle', 'steps': 0, 'content': '60',
      'percent': media_indexValueDataAnalysis[1].get('seven_max_proportion'),
      'strokeColor': '#2e62cd'},
     '近七天各平台互动量（最大值、昨日、三日环比）'],
    ['抖音-品牌活跃度',
     media_indexValueDataAnalysis[2].get('seven_max'),
     f"{media_indexValueDataAnalysis[2].get('seven_qoq')[1]}",
     f"{media_indexValueDataAnalysis[2].get('seven_qoq')[4]}",
     {'type': 'circle', 'steps': 0, 'content': '32',
      'percent': media_indexValueDataAnalysis[2].get('seven_max_proportion'),
      'strokeColor': '#2e62cd'},
     '近七天各平台热搜（最大值、昨日、三日环比）'], ]

app.layout = html.Div(
    [
        # 数据存储
        dcc.Store('media-index-value-chart-data', data=media_index_value_chart_data()),
        html.Div(
            [
                fac.AntdSpace(
                    [
                        fac.AntdText(
                            '新媒体平台实时数据',
                            strong=True,
                            style={
                                'fontSize': '18px'
                            }
                        ),
                        fac.AntdText(
                            '基于微博、抖音等数据统计，非全量数据，仅供参考',
                            style={
                                'color': 'rgb(163, 146, 158)'
                            }
                        ),
                        html.Div(
                            [

                                html.Div(
                                    html.Span('时间'),
                                    className='inputGroupLabel'
                                ),
                                fac.AntdDateRangePicker(picker='date', id='media-dateRange'),
                                fac.AntdButton(
                                    [
                                        fac.AntdIcon(
                                            icon='antd-file-search'
                                        ),
                                        '查询',
                                    ],
                                    id='media-search',
                                    type='primary',
                                    style={'height': '38px'}
                                ),

                            ],

                            style={'display': 'flex', 'marginLeft': 'auto'}
                        ),
                    ]
                ),
                # 指标卡区域
                fac.AntdRow(
                    [
                        fac.AntdCol(
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            fac.AntdIcon(
                                                icon='antd-check-circle',
                                                className='top-right-check-unselected',
                                                id={
                                                    'type': 'index-value-card-top-right-check',
                                                    'index': i
                                                }
                                            ),

                                            fac.AntdStatistic(
                                                title=item[0],
                                                value=item[1],
                                                titleTooltip=f'{item[5]}',
                                                className='main-index-value-maxValue'
                                            ),
                                            html.Div(
                                                [
                                                    fac.AntdText(f'较昨日{item[0]}环比',
                                                                 style={'fontSize': '12px'}
                                                                 ),
                                                    fac.AntdText(f' {item[2]}',
                                                                 className='pop-value',
                                                                 style={'fontSize': '15px',
                                                                        'fontFamily': 'CDSHT-Regular,CDSHT'}
                                                                 )
                                                ],
                                                className='main-index-value-oneDayPop',
                                            ),
                                            html.Div(
                                                [
                                                    fac.AntdText(f'较近三天{item[0]}环比',
                                                                 style={'fontSize': '12px'}
                                                                 ),
                                                    fac.AntdText(f' {item[3]}',
                                                                 className='pop-value',
                                                                 style={'fontSize': '15px',
                                                                        'fontFamily': 'CDSHT-Regular,CDSHT'}
                                                                 )
                                                ],
                                                className='main-index-value-threeDayPop',
                                            ),

                                        ],
                                        style={'flex': '2'}
                                    ),
                                    fac.AntdTooltip(
                                        fac.AntdProgress(
                                            percent=item[4].get('percent'),
                                            strokeColor=f"{item[4].get('strokeColor')}" if type(
                                                item[4].get('strokeColor')) == "str"
                                            else item[4].get('strokeColor'),
                                            steps=item[4].get('steps'),
                                            type=f"{item[4].get('type')}",
                                            style={'flex': '1'}
                                        ),
                                        title=f'近七天{item[0]}最大值占比',
                                        className='main-index-value-maxValueProportion',
                                    ),

                                ],
                                id={
                                    'type': 'index-value-card',
                                    'index': i
                                },
                                className='index-value-card',
                                style={'display': 'flex'}
                            ),

                            flex=1,

                            style={'padding': '10px 10px'}
                        )
                        for i, item in enumerate(index_value_cardData_list)
                    ],
                    className='wb-statistic-area',
                    wrap=False,
                ),

                fac.AntdText(
                    id='selected-card'
                )
            ],
            style={
                'background': 'white',
                'padding': '25px'
            }
        ),
        # 图表区域
        html.Div(
            render_one_chart(media_index_value_chart_data()[0]),
            style={
                'background': 'white',
                'boxShadow': '0 5px 30px 0 rgb(0 0 0 / 7%)',
                'padding': '25px'
            }
        ),
        # 内容区域
        html.Div(

            [
                fac.AntdDivider('具体内容', id='divider-display', innerTextOrientation='center', isDashed=True,
                                fontStyle='oblique'),
                fac.AntdTable(
                    columns=[
                        {
                            'title': '内容',
                            'dataIndex': 'media_content',
                            'width': '25%',
                            'renderOptions': {'renderType': 'ellipsis'},
                        },
                        {
                            'title': '发布时间',
                            'dataIndex': 'media_create_time',
                            'width': '13%',
                            'renderOptions': {'renderType': 'ellipsis'},
                        },

                        {
                            'title': '点赞数',
                            'dataIndex': 'media_attitude_counts',
                            'width': '10%',
                        },
                        {
                            'title': '评论数',
                            'dataIndex': 'media_comment_counts',
                            'width': '8%'
                        },
                        {
                            'title': '转发数',
                            'dataIndex': 'media_share_counts',
                            'width': '8%'
                        },
                        {
                            'title': '收藏数',
                            'dataIndex': 'media_collect_counts',
                            'width': '8%'
                        },
                        {
                            'title': '平台',
                            'dataIndex': 'platform',
                            'width': '10%',
                        },
                        {
                            'title': '网页链接',
                            'dataIndex': 'web_link',
                            'width': '8%',
                            'renderOptions': {
                                'renderType': 'link',
                                'renderLinkText': '链接'
                            }

                        },

                    ],
                    data=media_indexValueContentData,
                    id='media-content-table-data',
                    # containerId='ps-container',
                    bordered=True,
                    maxHeight=180,
                    pagination={
                        'hideOnSinglePage': True,
                        'pageSize': 6,
                        'showSizeChanger': False
                    },
                    sortOptions={
                        'sortDataIndexes': ['media_create_time', 'media_attitude_counts',
                                            'media_comment_counts']},
                    style={'maxWidth': '95%', 'margin': '0 auto'}
                )
            ],
            id='index-content-area',
            style={'height': '350px',
                   'background': 'white',
                   'boxShadow': '0 5px 30px 0 rgb(0 0 0 / 7%)',
                   'padding': '25px'
                   },

        )

    ],
    style={
        'padding': '50px'
    }
)

if __name__ == '__main__':
    app.run_server(debug=True, port=8051)
