from dash import html
import feffery_antd_components as fac

from server import app

app.layout = html.Div(
    [fac.AntdAlert(message="示例", type="info")], style={"padding": 50}
)

if __name__ == "__main__":
    app.run()
