import dash
from dash import html
import feffery_antd_components as fac

app = dash.Dash(__name__)

app.layout = html.Div(
    fac.AntdLayout(
        [
            fac.AntdSider(
                collapsible=True,
                style={
                    'backgroundColor': 'rgb(240, 242, 245)'
                }
            ),

            fac.AntdContent(
                html.Div(
                    fac.AntdTitle(
                        '内容区示例',
                        level=2,
                        style={
                            'margin': '0'
                        }
                    ),
                    style={
                        'display': 'flex',
                        'height': '100%',
                        'justifyContent': 'center',
                        'alignItems': 'center'
                    }
                ),
                style={
                    'backgroundColor': 'white'
                }
            )
        ],
        style={
            'height': '100%'
        }
    ),
    style={
        'height': '100vh'
    }
)

if __name__ == '__main__':
    app.run_server(debug=True)
