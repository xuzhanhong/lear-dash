import dash
from flask_login import LoginManager, UserMixin

from models.auth import UserAccount
from models.authority import UserAuthority

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

    match_user = list(
        UserAccount
        .select()
        .where(UserAccount.username == user_id)
        .dicts()
    )[0]

    # 查询权限控制表中当前用户的信息
    current_user_authority = list(
        UserAuthority
        .select()
        .where(UserAuthority.username == user_id)
        .dicts()
    )

    if current_user_authority:
        accessible_apps = current_user_authority[0]['accessiable_apps']

    else:
        accessible_apps = range(1, 25)

    curr_user = User()
    curr_user.id = user_id
    curr_user.role = match_user['role']
    curr_user.gender = match_user['gender']
    curr_user.register_time = match_user['register_time']
    curr_user.accessible_apps = accessible_apps

    return curr_user
