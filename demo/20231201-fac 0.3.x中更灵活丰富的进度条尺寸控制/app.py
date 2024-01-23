import dash
import numpy as np
import feffery_antd_components as fac

app = dash.Dash(__name__)

np.random.seed(2)

app.layout = fac.AntdSpace(
    [
        fac.AntdSpace(
            [
                fac.AntdProgress(
                    percent=50
                ),
                fac.AntdProgress(
                    percent=50,
                    size='small'
                ),
                fac.AntdProgress(
                    percent=50,
                    size=[300, 50]
                )
            ],
            direction='vertical',
            style={
                'width': 300
            }
        ),
        fac.AntdSpace(
            [
                fac.AntdProgress(
                    percent=50,
                    type='circle'
                ),
                fac.AntdProgress(
                    percent=50,
                    size='small',
                    type='circle'
                ),
                fac.AntdProgress(
                    percent=50,
                    size=20,
                    type='circle'
                )
            ]
        ),
        fac.AntdSpace(
            [
                fac.AntdProgress(
                    percent=50,
                    type='dashboard'
                ),
                fac.AntdProgress(
                    percent=50,
                    size='small',
                    type='dashboard'
                ),
                fac.AntdProgress(
                    percent=50,
                    size=20,
                    type='dashboard'
                )
            ]
        ),
        fac.AntdSpace(
            [
                fac.AntdProgress(
                    percent=50,
                    steps=5
                ),
                fac.AntdProgress(
                    percent=50,
                    size='small',
                    steps=5
                ),
                fac.AntdProgress(
                    percent=50,
                    size=20,
                    steps=5
                ),
                fac.AntdProgress(
                    percent=50,
                    size=[50, 50],
                    steps=5
                )
            ]
        ),
        fac.AntdTitle(
            '在表格中使用',
            level=4
        ),
        fac.AntdTable(
            columns=[
                {
                    'title': '示例字段',
                    'dataIndex': '示例字段'
                }
            ],
            data=[
                {
                    '示例字段': fac.AntdProgress(
                        percent=round(value, 2),
                        size=20,
                        type='circle',
                        strokeColor='#ff4d4f' if value <= 40 else None
                    )
                }
                for value in np.random.uniform(0, 100, 8)
            ],
            size='small',
            pagination=False,
            style={
                'width': 150
            }
        )
    ],
    direction='vertical',
    style={
        'padding': 50
    }
)


if __name__ == '__main__':
    app.run(debug=True)
