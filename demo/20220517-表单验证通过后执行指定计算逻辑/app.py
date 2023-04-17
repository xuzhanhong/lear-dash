import dash
import time
from dash import html, dcc
import feffery_antd_components as fac
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fac.AntdForm(
            [
                fac.AntdFormItem(
                    fac.AntdInputNumber(
                        id='input1',
                        style={
                            'width': '200px'
                        }
                    ),
                    id='input1-container',
                    label='请输入小于1的数值'
                ),
                fac.AntdFormItem(
                    fac.AntdInputNumber(
                        id='input2',
                        style={
                            'width': '200px'
                        }
                    ),
                    id='input2-container',
                    label='请输入大于10的数值'
                ),
                fac.AntdButton('提交', id='button', type='primary')
            ],
            layout='vertical'
        ),
        fac.AntdDivider(isDashed=True),
        fac.AntdSpin(
            html.Div(id='output'),
            text='计算中',
            delay=300
        )
    ],
    style={
        'padding': '50px'
    }
)


@app.callback(
    [Output('input1-container', 'validateStatus'),
     Output('input2-container', 'validateStatus'),
     Output('input1-container', 'help'),
     Output('input2-container', 'help')],
    Input('button', 'nClicks'),
    [State('input1', 'value'),
     State('input2', 'value')],
    prevent_initial_call=True
)
def validate_input_value(nClicks, value1, value2):
    return [
        ('success' if value1 < 1 else 'error') if value1 else 'error',
        ('success' if value2 > 10 else 'error') if value2 else 'error',
        ('参数合法' if value1 < 1 else '参数不合法') if value1 else '请完善参数',
        ('参数合法' if value2 > 10 else '参数不合法') if value2 else '请完善参数',
    ]


@app.callback(
    Output('output', 'children'),
    Input('button', 'nClicks'),
    [State('input1', 'value'),
     State('input2', 'value')],
    prevent_initial_call=True
)
def calculate_result(nClicks, value1, value2):
    if value1 and value2 and (value1 < 1 and value2 > 10):
        time.sleep(3)
        return 'value1 x value2 = {}'.format(value1 * value2)


if __name__ == '__main__':
    app.run_server(debug=True)
