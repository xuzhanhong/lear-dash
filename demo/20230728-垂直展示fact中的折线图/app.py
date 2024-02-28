import dash
import random
from dash import html
import feffery_antd_charts as fact

app = dash.Dash(__name__)

mock_data = [
    {
        '系列': f'系列{i}',
        'x': j,
        'y': j + j * random.uniform(0, 1)
    }
    for i in range(1, 6)
    for j in range(25)
]

app.layout = html.Div(
    [
        html.Div(
            fact.AntdLine(
                data=mock_data,
                meta={
                    'x': {
                        'type': 'linear',
                        'range': [1, 0] # 技巧，用于翻转坐标轴
                    },
                    'y': {
                        'type': 'linear'
                    }
                },
                xField='y',
                yField='x',
                seriesField='系列',
                color=[
                    '#f6e58d', '#ffbe76', '#ff7979', '#badc58', '#dff9fb'
                ],
                xAxis={
                    'position': 'top'
                },
                legend={
                    'position': 'left'
                }
            ),
            style={
                'height': 400,
                'width': 400
            }
        )
    ],
    style={
        'padding': '50px 100px'
    }
)

if __name__ == '__main__':
    app.run(debug=True)
