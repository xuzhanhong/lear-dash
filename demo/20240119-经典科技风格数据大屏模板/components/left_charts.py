import numpy as np
import pandas as pd
import feffery_antd_charts as fact


def render_chart1():

    # 示例数据集
    demo_data = (
        pd
        .DataFrame(
            {
                '日期': pd.date_range('2024-01-01', periods=31),
                '数值': np.random.normal(100, 30, 31)
            }
        )
    )

    demo_data['日期'] = demo_data['日期'].dt.date
    demo_data['数值'] = demo_data['数值'].round(2)

    return fact.AntdArea(
        data=demo_data.to_dict('records'),
        xField='日期',
        yField='数值',
        smooth=True,
        line={
            'style': {
                'stroke': '#7fcdff'
            }
        },
        areaStyle={
            'fill': 'l(90) 0:#1890ff 0.5:#7ec2f3 1:transparent'
        },
        xAxis={
            'label': {
                'autoRotate': True,
                'style': {
                    'fill': '#c2e7ff'
                },
                'autoHide': True
            },
            'tickCount': 5
        },
        yAxis={
            'label': {
                'autoRotate': True,
                'style': {
                    'fill': '#c2e7ff'
                }
            },
            'grid': {
                'line': {
                    'style': {
                        'stroke': '#394c6d',
                        'lineDash': [2, 2]
                    }
                }
            }
        }
    )


def render_chart2():

    # 示例数据集
    demo_data = (
        pd
        .DataFrame(
            {
                '项目': [f'项目{i}' for i in range(1, 6)],
                '数值': np.random.uniform(200, 1000, 5)
            }
        )
        .sort_values('数值', ascending=False)
    )

    demo_data['数值'] = demo_data['数值'].round()

    return fact.AntdBar(
        data=demo_data.to_dict('records'),
        xField='数值',
        yField='项目',
        barStyle={
            'fill': '#0a73ff'
        },
        barBackground={
            'style': {
                'fill': 'rgba(255, 255, 255, 0.1)'
            }
        },
        xAxis={
            'label': {
                'autoRotate': True,
                'style': {
                    'fill': '#c2e7ff'
                },
                'autoHide': True
            },
            'grid': {
                'line': {
                    'style': {
                        'lineWidth': 0
                    }
                }
            }
        },
        yAxis={
            'label': {
                'autoRotate': True,
                'style': {
                    'fill': '#c2e7ff'
                }
            },
            'grid': {
                'line': {
                    'style': {
                        'stroke': '#394c6d',
                        'lineDash': [2, 2]
                    }
                }
            }
        }
    )


def render_chart3():

    # 示例数据集
    demo_data = (
        pd
        .DataFrame(
            {
                '日期': pd.date_range('2024-01-01', periods=31),
                '数值': np.random.uniform(-20, 40, 31)
            }
        )
    )

    demo_data['日期'] = demo_data['日期'].dt.date
    demo_data['数值'] = demo_data['数值'].cumsum().round(2)

    return fact.AntdLine(
        data=demo_data.to_dict('records'),
        xField='日期',
        yField='数值',
        lineStyle={
            'stroke': '#7fcdff'
        },
        xAxis={
            'label': {
                'autoRotate': True,
                'style': {
                    'fill': '#c2e7ff'
                },
                'autoHide': True
            },
            'tickCount': 10
        },
        yAxis={
            'label': {
                'autoRotate': True,
                'style': {
                    'fill': '#c2e7ff'
                }
            },
            'grid': {
                'line': {
                    'style': {
                        'stroke': '#394c6d',
                        'lineDash': [2, 2]
                    }
                }
            }
        }
    )
