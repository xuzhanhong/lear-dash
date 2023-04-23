import os
import sys
# 强制下列代码不会在代码格式化后自动排到导包部分的后面
try:
    sys.path.append('..')
    sys.path.append(os.getcwd())
except:
    pass

from config import PathConfig
from peewee import (
    SqliteDatabase,
    Model,
    CharField
)
from playhouse.sqlite_ext import JSONField

db = SqliteDatabase(
    os.path.join(PathConfig.ABS_ROOT_PATH, 'models', 'authority.db')
)


class UserAuthority(Model):

    # 用户名
    username = CharField(primary_key=True)

    # 可访问的子应用列表
    accessiable_apps = JSONField()

    class Meta:
        database = db
        table_name = 'user_authority'


db.create_tables([UserAuthority])

# 示例，针对用户feffery的权限设置
if UserAuthority.select().where(UserAuthority.username == 'feffery').count():
    (
        UserAuthority
        .update({
            UserAuthority.accessiable_apps: [
                f'sub-app{i}'
                for i in range(10, 16)
            ]
        })
        .where(UserAuthority.username == 'feffery')
        .execute()
    )

else:
    (
        UserAuthority
        .insert_many({
            'username': 'feffery',
            'accessiable_apps': [
                f'sub-app{i}'
                for i in range(10, 16)
            ]
        })
        .execute()
    )
