import numpy as np
import pandas as pd
import feffery_antd_charts as fact


def render_chart1():

    # 示例数据集
    demo_data = (
        pd
        .DataFrame(
            {
                '类型': [f'类型{i}' for i in range(1, 6)],
                '数值': np.random.normal(100, 30, 5)
            }
        )
        .sort_values('数值', ascending=False)
    )

    demo_data['数值'] = demo_data['数值'].round(2)

    return fact.AntdPie(
        data=demo_data.to_dict('records'),
        angleField='数值',
        colorField='类型',
        radius=0.7,
        innerRadius=0.65,
        statistic=False,
        color=['#1890ff', '#40a9ff', '#69c0ff', '#95d3ff', '#bae7ff'],
        label={
            'style': {
                'fill': '#c2e7ff',
                'fontSize': 18
            },
            'formatter': {
                'func': '(e) => `${e.数值}\n${e.类型}`'
            },
            'type': 'outer',
            'offset': 30
        },
        legend=False
    )
