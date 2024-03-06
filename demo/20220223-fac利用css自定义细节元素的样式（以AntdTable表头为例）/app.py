import dash
from dash import html
import feffery_antd_components as fac

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fac.AntdTable(
            columns=[
                {
                    'title': '字段1',
                    'dataIndex': '字段1'
                },
                {
                    'title': '字段2',
                    'dataIndex': '字段2'
                }
            ],
            data=[
                {
                    '字段1': i,
                    '字段2': i
                }
                for i in range(10)
            ],
            bordered=True
        )
    ],
    style={
        'padding': '50px 100px'
    }
)

if __name__ == '__main__':
    app.run_server(debug=True)
