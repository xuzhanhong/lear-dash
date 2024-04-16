from dash import html
import feffery_antd_components as fac
from dash.dependencies import Input, Output, State

from server import app
from components import demo_component

app.layout = html.Div(
    [
        fac.AntdCenter(
            fac.AntdSpace(
                [
                    fac.AntdColorPicker(id="select-color", value="#b7eb8f"),
                    fac.AntdButton("刷新", type="primary", id="update-components"),
                ]
            ),
            style={"padding": "24px 0"},
        ),
        html.Div(id="components-container"),
    ]
)


@app.callback(
    Output("components-container", "children"),
    Input("update-components", "nClicks"),
    State("select-color", "value"),
)
def update_components(nClicks, color):
    return demo_component.render(color)


if __name__ == "__main__":
    app.run(debug=True)
