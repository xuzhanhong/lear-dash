import dash
from flask_login import LoginManager, UserMixin

from models.auth import UserAccount

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    update_title=None
)

server = app.server

app.title = '微型项目课程1：具有用户登录功能的通用应用'

# 初始化登陆管理类
login_manager = LoginManager()

login_manager.login_view = '/'

# 配置密钥
app.server.secret_key = 'my dash app'

# 绑定纳入鉴权范围的flask实例
login_manager.init_app(server)


class User(UserMixin):
    pass


@login_manager.user_loader
def load_user(user_id):

    match_user_lst = list(
        UserAccount
        .select()
        .where(UserAccount.username == user_id)
        .dicts()
    )
    if not match_user_lst:
        return None
    match_user = match_user_lst[0]

    curr_user = User()
    curr_user.id = user_id
    curr_user.role = match_user['role']
    curr_user.gender = match_user['gender']
    curr_user.register_time = match_user['register_time']

    return curr_user
