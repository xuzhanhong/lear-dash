import dash
from dash import html, dcc
import feffery_antd_components as fac
from dash.dependencies import Input, Output, State

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True
)

# 定义各步骤所需表单内容
steps_form = [
    # 步骤1
    fac.AntdForm(
        [
            fac.AntdFormItem(
                fac.AntdInput(
                    id='step1-input1',
                    persistence=True,
                    persistence_type='memory',
                    style={
                        'width': '150px'
                    }
                ),
                label='步骤1输入框1'
            ),
            fac.AntdFormItem(
                fac.AntdInput(
                    id='step1-input2',
                    persistence=True,
                    persistence_type='memory',
                    style={
                        'width': '150px'
                    }
                ),
                label='步骤1输入框2'
            ),
            fac.AntdFormItem(
                fac.AntdRadioGroup(
                    id='step1-radio1',
                    persistence=True,
                    persistence_type='memory',
                    options=[
                        {
                            'label': f'单选{i}',
                            'value': f'单选{i}'
                        }
                        for i in range(3)
                    ],
                    defaultValue='单选1'
                ),
                label='步骤1单选1'
            )
        ]
    ),

    # 步骤2
    fac.AntdForm(
        [
            fac.AntdFormItem(
                fac.AntdInput(
                    id='step2-input1',
                    persistence=True,
                    persistence_type='memory',
                    style={
                        'width': '150px'
                    }
                ),
                label='步骤2输入框1'
            ),
            fac.AntdFormItem(
                fac.AntdSelect(
                    id='step2-select1',
                    persistence=True,
                    persistence_type='memory',
                    options=[
                        {
                            'label': f'选项{i}',
                            'value': f'选项{i}'
                        }
                        for i in range(5)
                    ],
                    style={
                        'width': '200px'
                    }
                ),
                label='步骤1单选1'
            )
        ]
    ),

    # 步骤3
    html.Div(
        [
            fac.AntdResult(
                status='success',
                title='完成填写'
            )
        ]
    )
]

app.layout = html.Div(
    [
        # 缓存每一步骤最近填写的参数
        html.Div(
            [
                dcc.Store(
                    id='step1-form-cache'
                ),
                dcc.Store(
                    id='step2-form-cache'
                )
            ]
        ),

        fac.AntdSteps(
            id='steps',
            steps=[
                {
                    'title': f'步骤{i + 1}'
                }
                for i in range(3)
            ],
            progressDot=True,
            current=0
        ),

        fac.AntdDivider(isDashed=True),

        # 表单容器
        html.Div(
            id='form-container'
        ),

        fac.AntdDivider(isDashed=True),

        fac.AntdRow(
            [
                fac.AntdCol(
                    fac.AntdButton(
                        '上一步',
                        id='last-step'
                    ),
                    span=12
                ),
                fac.AntdCol(
                    fac.AntdButton(
                        '下一步',
                        id='next-step',
                        style={
                            'float': 'right'
                        }
                    ),
                    span=12
                ),
            ]
        )
    ],
    style={
        'padding': '50px'
    }
)


@app.callback(
    Output('form-container', 'children'),
    Input('steps', 'current')
)
def step_to_form(current):
    return steps_form[current]


@app.callback(
    [Output('last-step', 'disabled'),
     Output('next-step', 'disabled')],
    Input('steps', 'current')
)
def steps_to_last_next_disabled(current):
    return [
        current == 0,
        current == 2
    ]


@app.callback(
    Output('steps', 'current'),
    [Input('last-step', 'nClicks'),
     Input('next-step', 'nClicks')],
    State('steps', 'current'),
    prevent_initial_call=True
)
def switch_steps(last_step, next_step, current):
    triggered_id = dash.callback_context.triggered[0]['prop_id']

    if triggered_id == 'last-step.nClicks':
        return current - 1

    return current + 1


if __name__ == '__main__':
    app.run_server(debug=True)
