from dash import html
import feffery_antd_charts as fact


def render_one_chart(chart_data):
    return html.Div(
        [

            fact.AntdLine(
                id='media-index-value-chart',
                data=chart_data,
                xField='created_at',
                yField='count',
                seriesField='series',
                xAxis={
                    'label': {
                        'style': {
                            'fontFamily': 'Times New Roman',
                            'fontSize': 16
                        }
                    },
                },
                yAxis={

                    'label': {
                        # 'offset': 20,
                        'style': {
                            'fontFamily': 'Times New Roman',
                            'fontSize': 16
                        }
                    },
                    'line': {
                        'style': {
                            'opacity': 1
                        }
                    },
                    'tickLine': {
                        'length': 5
                    },

                },
                label={},
                point={
                    'shape': {
                        'func': '''
                                    (ref)=>{
                                         if(ref.series==="螺霸王"){

                                         }   
                                    }

                                '''
                    }
                },
                # color= ['#00F5A0', '#9FDABF', '#E98F6F', '#4fc3f7'],
                lineStyle={
                    'func': '''
                                               (ref) => {
                                                   if (ref.series === '螺霸王') {
                                                       return {
                                                           lineWidth:'3',
                                                           cursor: 'pointer'

                                                       }
                                                   } else if (ref.series == '好欢螺') {
                                                       return {
                                                            lineWidth:'3',
                                                           cursor: 'pointer'
                                                       }
                                                   }
                                                   return {
                                                        lineWidth:'3',
                                                       cursor: 'pointer'
                                                   }
                                               }''',

                },
                legend={
                    'position': 'top-right',
                    'offsetX': -10,
                    'itemHeight': 20,
                    'selected': {
                        '螺蛳粉': False,
                    }
                },
                annotations=[
                    {
                        'type': 'region',
                        'start': ['0%', '0%'],
                        'end': ['20%', '14%'],
                        'top': True,
                        'style': {
                            'fill': '#1890ff',
                            'fillOpacity': 1,
                            'opacity': 0.6,
                        },
                    },
                    {
                        'type': 'text',
                        'position': ['10%', '6.5%'],
                        'content': f'基础趋势图',
                        'style': {
                            'fill': '#fff',
                            'fontSize': 15,
                            'textAlign': 'center',
                            'textBaseline': 'middle'
                        },
                    }
                ],
                tooltip={
                    'enterable': True,
                    'showTitle': True,
                    # 'title': '情感趋势走向',
                    'marker': {
                        'r': 5
                    },
                    'domStyles': {
                        'g2-tooltip-title': {
                            'font-size': '18px'
                        },
                        'g2-tooltip': {
                            'background-color': 'rgba(255, 255, 255, 0.8)'
                        }
                    }
                },
                style={'padding': '0 10px', },
                smooth=False,
                isStack=False,
                height=300,
            ),

        ],
        style={'maxWidth': '95%'}
    )
