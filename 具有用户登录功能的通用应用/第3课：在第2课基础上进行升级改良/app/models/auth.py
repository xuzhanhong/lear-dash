import os
import sys
# 强制下列代码不会在代码格式化后自动排到导包部分的后面
try:
    sys.path.append('..')
    sys.path.append(os.getcwd())
except:
    pass

from config import PathConfig
from utils import str2md5
from peewee import (
    SqliteDatabase,
    Model,
    CharField,
    DateTimeField,
    OperationalError
)
from datetime import datetime


db = SqliteDatabase(
    os.path.join(PathConfig.ABS_ROOT_PATH, 'models', 'auth.db')
)


class UserAccount(Model):

    # 用户名
    username = CharField(primary_key=True)

    # 用户性别：男、女
    gender = CharField()

    # 用户角色：普通用户、管理员
    role = CharField()

    # 明文密码
    password = CharField()

    # 加密密码
    password_md5 = CharField()

    # 注册时间
    register_time = DateTimeField()

    class Meta:
        database = db
        table_name = 'user_account'

    @classmethod
    def check_user_exists(cls, username: str):
        '''
        检查指定的用户名是否在库中已经存在
        '''

        try:
            _ = (
                cls
                .select()
                .where(cls.username == username)
                .get()
            )

            return {
                'status': 'success',
                'message': '用户已存在'
            }

        except cls.DoesNotExist:

            return {
                'status': 'success',
                'message': '用户不存在'
            }

    @classmethod
    def check_user_password(cls,
                            username: str,
                            password: str = None,
                            password_md5: str = None,
                            mode: str = 'default'):
        '''
        检查指定的用户名与密码是否匹配，具有明文密码与加密密码两种检查模式
        '''

        if mode == 'default':
            # 检查用户名与明文密码是否匹配
            try:
                _ = (
                    cls
                    .select()
                    .where(
                        (cls.username == username) &
                        (cls.password == password)
                    )
                    .get()
                )

                return {
                    'status': 'success',
                    'message': '密码正确'
                }

            except cls.DoesNotExist:

                return {
                    'status': 'success',
                    'message': '密码错误'
                }

        elif mode == 'md5':

            # 检查用户名与明文密码是否匹配
            try:
                _ = (
                    cls
                    .select()
                    .where(
                        (cls.username == username) &
                        (cls.password_md5 == password_md5)
                    )
                    .get()
                )

                return {
                    'status': 'success',
                    'message': '密码正确'
                }

            except cls.DoesNotExist:

                return {
                    'status': 'success',
                    'message': '密码错误'
                }

        return {
            'status': 'fail',
            'message': 'mode参数非法'
        }

    @classmethod
    def reset(cls):

        try:
            cls._meta.database.drop_tables(cls)
            print('用户账户信息表重置完成')
        except OperationalError:
            print('删除失败：用户账户信息表不存在')


db.create_tables([UserAccount])

if __name__ == '__main__':

    from faker import Faker

    fake_generator = Faker(locale='zh_CN')

    # 项目初始化时执行
    # 初始化数据库
    UserAccount.reset()

    # 重置表
    db.create_tables([UserAccount])

    # 插入测试用管理员账号
    UserAccount.create(
        username='admin',
        gender='男',
        role='管理员',
        password='admin123',
        password_md5=str2md5('admin123'),
        register_time=datetime.now()
    )

    # 插入测试普通用户账号
    for i in range(100):
        UserAccount.create(
            username=fake_generator.name()+str(i),
            gender=['男', '女'][i % 2 == 0],
            role='普通用户',
            password='dashdash',
            password_md5=str2md5('dashdash'),
            register_time=datetime.now()
        )
