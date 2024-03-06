import dash
from dash import html
import feffery_antd_components as fac

app = dash.Dash(__name__)

app.layout = html.Div(
    [

        html.Div(
            style={
                'height': '10px'
            }
        ),

        fac.AntdSpace(
            [
                html.Div(
                    '输入框',
                    className='prefix-label-box'
                ),
                fac.AntdInput(
                    style={
                        'width': '200px'
                    }
                )
            ],
            size=0
        ),

        html.Div(
            style={
                'height': '10px'
            }
        ),

        fac.AntdSpace(
            [
                html.Div(
                    '选择框',
                    className='prefix-label-box'
                ),
                fac.AntdSelect(
                    style={
                        'width': '200px'
                    }
                )
            ],
            size=0
        )
    ] * 5,
    style={
        'padding': '50px'
    }
)

if __name__ == '__main__':
    app.run_server(debug=True)
