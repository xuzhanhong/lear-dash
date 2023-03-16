import dash

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    update_title=None
)

app.title = '某供应商平台模板 - 玩转dash星球出品'

server = app.server
