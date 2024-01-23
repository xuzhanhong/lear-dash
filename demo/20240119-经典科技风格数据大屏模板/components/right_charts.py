import numpy as np
import pandas as pd
import feffery_antd_charts as fact


def render_chart1():

    return fact.AntdGauge(
        percent=0.66,
        indicator={
            'shape': 'simple',
            'pointer': {
                'style': {
                    'fill': '#188bf5',
                },
            }
        },
        range={
            'color': '#188bf5'
        },
        axis={
            'label': {
                'style': {
                    'fill': '#c2e7ff',
                    'fontSize': 16
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
                '项目': [f'任务{i}' for i in range(1, 16)],
                '数值': np.random.uniform(40, 100, 15)
            }
        )
        .sort_values('数值', ascending=False)
    )

    demo_data['数值'] = demo_data['数值'].round()

    return fact.AntdColumn(
        data=demo_data.to_dict('records'),
        xField='项目',
        yField='数值',
        columnStyle={
            'fill': '#0a73ff'
        },
        columnBackground={
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
