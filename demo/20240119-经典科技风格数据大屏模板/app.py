import dash
from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc

from server import app
from config import AppConfig
from components import left_charts, bottom_charts, right_charts


def render_layout():

    return html.Div(
        [
            html.Div(
                [
                    # 页首
                    fac.AntdCenter(
                        fac.AntdText(
                            AppConfig.app_title,
                            className='gradient-text',
                            style={
                                'fontFamily': '钉钉进步体',
                                'fontSize': 46,
                                'fontWeight': 'bold'
                            }
                        ),
                        style={
                            'height': 81,
                            'position': 'absolute',
                            'top': 0,
                            'left': 0,
                            'right': 0,
                            'background': 'url("assets/imgs/页首.jpg")',
                            'backgroundRepeat': 'no-repeat',
                            'backgroundPosition': 'center',
                            'objectFit': 'contain'
                        }
                    ),

                    # 左侧容器
                    html.Div(
                        [
                            fac.AntdFlex(
                                [
                                    html.Div(
                                        fac.AntdText(
                                            'XXX数据趋势',
                                            className='gradient-text',
                                            style={
                                                'fontFamily': '钉钉进步体',
                                                'fontSize': 26
                                            }
                                        ),
                                        className='panel-item-title'
                                    ),
                                    html.Div(
                                        left_charts.render_chart1(),
                                        style={
                                            'height': '100%',
                                            'padding': '16px 6px'
                                        }
                                    )
                                ],
                                className='left-panel-item',
                                vertical=True
                            ),
                            fac.AntdFlex(
                                [
                                    html.Div(
                                        fac.AntdText(
                                            'XXX项目统计TOP5',
                                            className='gradient-text',
                                            style={
                                                'fontFamily': '钉钉进步体',
                                                'fontSize': 26
                                            }
                                        ),
                                        className='panel-item-title'
                                    ),
                                    html.Div(
                                        left_charts.render_chart2(),
                                        style={
                                            'height': '100%',
                                            'padding': '16px 6px'
                                        }
                                    )
                                ],
                                className='left-panel-item',
                                vertical=True
                            ),
                            fac.AntdFlex(
                                [
                                    html.Div(
                                        fac.AntdText(
                                            'XXX历史数据追踪',
                                            className='gradient-text',
                                            style={
                                                'fontFamily': '钉钉进步体',
                                                'fontSize': 26
                                            }
                                        ),
                                        className='panel-item-title'
                                    ),
                                    html.Div(
                                        left_charts.render_chart3(),
                                        style={
                                            'height': '100%',
                                            'padding': '16px 6px'
                                        }
                                    )
                                ],
                                className='left-panel-item',
                                vertical=True
                            ),
                        ],
                        className='left-panel'
                    ),

                    # 中央容器
                    html.Div(
                        [
                            fac.AntdFlex(
                                [
                                    html.Div(
                                        fac.AntdText(
                                            'XXX关键业务指标',
                                            className='gradient-text',
                                            style={
                                                'fontFamily': '钉钉进步体',
                                                'fontSize': 26
                                            }
                                        ),
                                        className='panel-item-title'
                                    ),
                                    fac.AntdRow(
                                        [
                                            fac.AntdCol(
                                                html.Div(
                                                    html.Div(
                                                        [
                                                            fuc.FefferyCountUp(
                                                                end=666.66,
                                                                decimals=2,
                                                                duration=1,
                                                                className='gradient-text',
                                                                style={
                                                                    'fontSize': 28,
                                                                    'fontFamily': '钉钉进步体',
                                                                }
                                                            ),
                                                            '\n',
                                                            fac.AntdText(
                                                                f'指标{i}',
                                                                className='gradient-text',
                                                                style={
                                                                    'fontFamily': '钉钉进步体',
                                                                    'fontSize': 20
                                                                }
                                                            ),
                                                        ],
                                                        style={
                                                            'width': '100%',
                                                            'position': 'absolute',
                                                            'top': '10%',
                                                            'textAlign': 'center',
                                                            'whiteSpace': 'pre'
                                                        }
                                                    ),
                                                    className='index-value-tray'
                                                ),
                                                span=6
                                            )
                                            for i in range(1, 5)
                                        ],
                                        style={
                                            'padding': '16px 6px',
                                            'height': '150px'
                                        }
                                    )
                                ],
                                className='center-top-panel-item',
                                vertical=True
                            ),
                            fac.AntdFlex(
                                [
                                    html.Div(
                                        fac.AntdText(
                                            'XXX市场综合占比',
                                            className='gradient-text',
                                            style={
                                                'fontFamily': '钉钉进步体',
                                                'fontSize': 26
                                            }
                                        ),
                                        className='panel-item-title'
                                    ),
                                    html.Div(
                                        bottom_charts.render_chart1(),
                                        style={
                                            'height': '100%',
                                            'padding': '16px 6px'
                                        }
                                    )
                                ],
                                className='center-bottom-panel-item',
                                vertical=True
                            ),
                        ],
                        className='center-panel'
                    )
                ],
                className='root-container',
                style={
                    'height': '100vh',
                    'position': 'relative',
                    'backgroundColor': '#0c1422'
                }
            ),

            # 右侧容器
            html.Div(
                [
                    fac.AntdFlex(
                        [
                            html.Div(
                                fac.AntdText(
                                    'XXX任务总进度',
                                    className='gradient-text',
                                    style={
                                        'fontFamily': '钉钉进步体',
                                        'fontSize': 26
                                    }
                                ),
                                className='panel-item-title'
                            ),
                            html.Div(
                                right_charts.render_chart1(),
                                style={
                                    'height': '100%',
                                    'padding': '16px 6px'
                                }
                            )
                        ],
                        className='right-panel-item',
                        vertical=True
                    ),
                    fac.AntdFlex(
                        [
                            html.Div(
                                fac.AntdText(
                                    'XXX分任务进度情况',
                                    className='gradient-text',
                                    style={
                                        'fontFamily': '钉钉进步体',
                                        'fontSize': 26
                                    }
                                ),
                                className='panel-item-title'
                            ),
                            html.Div(
                                right_charts.render_chart2(),
                                style={
                                    'height': '100%',
                                    'padding': '16px 6px'
                                }
                            )
                        ],
                        className='right-panel-item',
                        vertical=True
                    )
                ],
                className='right-panel'
            ),
        ]
    )


app.layout = render_layout


if __name__ == '__main__':
    app.run(debug=False)
