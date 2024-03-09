import dash
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Input, Output, State, MATCH, ALL

app = dash.Dash(__name__)

info_list = [
    ['直播间热度', 4270, '+6.55%'],
    ['观众热度', 7622, '+25.23%'],
    ['商品热度', 4216, '+19.97%'],
    ['销售额热度', 10428, '+17.12%'],
    ['销量热度', 15143, '+19.57%'],
]


@app.callback(
    [Output({'type': 'index-value-card', 'index': MATCH}, 'className'),
     Output({'type': 'index-value-card-top-right-check', 'index': MATCH}, 'className')],
    Input({'type': 'index-value-card', 'index': MATCH}, 'n_clicks'),
    State({'type': 'index-value-card', 'index': MATCH}, 'className'),
)
def handle_card_click_event(n_clicks, className):
    if n_clicks:

        if 'index-value-card-selected' in className:
            return [
                'index-value-card',
                'top-right-check-unselected'
            ]

        return [
            'index-value-card index-value-card-selected',
            'top-right-check'
        ]

    return dash.no_update


@app.callback(
    Output('selected-card', 'children'),
    Input({'type': 'index-value-card', 'index': ALL}, 'className')
)
def get_all_selected_card_index(className_list):
    return str([i for i, className in enumerate(className_list) if 'index-value-card-selected' in className])


app.layout = html.Div(
    [
        html.Div(
            [
                fac.AntdSpace(
                    [
                        fac.AntdText(
                            '直播电商1小时实时数据',
                            strong=True,
                            style={
                                'fontSize': '18px'
                            }
                        ),
                        fac.AntdText(
                            '基于蝉妈妈案例库数据统计，非全量数据，仅供参考',
                            style={
                                'color': 'rgb(163, 146, 158)'
                            }
                        )
                    ]
                ),

                fac.AntdRow(
                    [
                        fac.AntdCol(
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
                                        title=info[0],
                                        value=info[1],
                                        valueStyle={
                                            'fontSize': '28px',
                                            'fontWeight': 'bold'
                                        },
                                        titleTooltip='示例'
                                    ),
                                    fac.AntdParagraph(
                                        [
                                            fac.AntdText(
                                                '较昨日同期',
                                                style={
                                                    'color': 'rgb(85, 85, 85)',
                                                    'fontSize': '15px'
                                                }
                                            ),

                                            fac.AntdText(
                                                info[2],
                                                strong=True,
                                                style={
                                                    'color': 'rgb(255, 87, 77)',
                                                    'fontSize': '16px'
                                                }
                                            )
                                        ]
                                    )
                                ],
                                id={
                                    'type': 'index-value-card',
                                    'index': i
                                },
                                className='index-value-card'
                            ),
                            flex=1,
                            style={
                                'padding': '10px'
                            }
                        )
                        for i, info in enumerate(info_list)
                    ]
                ),

                fac.AntdText(
                    id='selected-card'
                )
            ],
            style={
                'background': 'white',
                'padding': '25px'
            }
        )
    ],
    style={
        'padding': '50px'
    }
)

if __name__ == '__main__':
    app.run_server(debug=True)
