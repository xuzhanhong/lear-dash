import dash
from dash import html
import feffery_antd_components as fac

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fac.AntdText(
            '这是“示例字体名字随便起反正是自己注册的”的使用示例',
            style={
                'fontFamily': '示例字体名字随便起反正是自己注册的',
                'fontSize': 40
            }
        )
    ],
    style={
        'padding': '100px'
    }
)

if __name__ == '__main__':
    app.run(debug=True)