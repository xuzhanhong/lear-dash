import dash

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    update_title=None,
    compress=True
)

app.title = '20220827-仪表盘界面模板'

server = app.server
