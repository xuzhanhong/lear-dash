import dash
from flask_login import LoginManager, UserMixin
from datetime import timedelta, datetime

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True
)

server = app.server

# server.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=7)

# 初始化登陆管理类
login_manager = LoginManager()

# 配置密钥
server.secret_key = 'my dash app'

# 绑定纳入鉴权范围的flask实例
login_manager.init_app(server)


class User(UserMixin):
    pass


@login_manager.user_loader
def load_user(user_id):

    new_user = User()
    new_user.id = user_id

    return new_user
