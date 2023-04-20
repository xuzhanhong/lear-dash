# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# Time       ：2023/4/19
# Author     ：xuzhanhong
# Description：关系型数据库数据模型
"""
from peewee import (
    MySQLDatabase, Model,
    CharField, IntegerField,
)


# 创建数据库关联对象
sql_db = MySQLDatabase(
    'approval_process',
    user='root',
    host='localhost',
    password='12345678'
)


class UserInfo(Model):
    """
    用户信息表
    """

    # 用户id，主键
    user_id = CharField(primary_key=True)

    # 用户名
    user_name = CharField()

    # 密码
    password = CharField()

    # md5加密密码，用作登陆鉴权时安全校验使用
    md5_password = CharField()

    # 性别
    gender = CharField()

    # 部门id
    department_id = IntegerField()

    # 职级id
    rank_id = IntegerField()

    @classmethod
    def check_user_auth(cls,
                        user_id: str,
                        md5_password: str) -> dict:
        """用户根据输入的user_id和md5_password进行鉴权

        Args:
            user_id (str): 用户登录id
            md5_password (str): 用户所填密码的md5加密值

        Returns:
            dict: 鉴权状态及附加信息
        """

        # 尝试根据输入的user_id查询用户信息记录
        with sql_db.atomic():
            match_records = (
                cls
                .select()
                .where(cls.user_id == user_id)
                .dicts()
            )

        # 判断当前用户是否存在
        if match_records:
            # 继续判断md5密码是否正确
            if match_records[0]['md5_password'] == md5_password:
                return {
                    'status': 'success',
                    'message': '当前用户鉴权通过',
                    'data': match_records[0]
                }

            return {
                'status': 'error',
                'message': '当前用户密码错误'
            }

        return {
            'status': 'error',
            'message': '当前用户不存在'
        }

    class Meta:

        database = sql_db
        table_name = 'user_info'


class RankInfo(Model):
    """
    职级信息表
    """

    # 职级id
    rank_id = IntegerField(primary_key=True)

    # 职级类型
    rank_type = CharField()

    # 职级名称
    rank_name = CharField()

    # 职级级别
    rank_level = CharField()

    class Meta:

        database = sql_db
        table_name = 'rank_info'


class DepartmentInfo(Model):
    """
    部门信息表
    """

    # 部门id
    department_id = IntegerField(primary_key=True)

    # 部门名称
    department_name = CharField()

    # 部门类型
    department_type = CharField()

    class Meta:

        database = sql_db
        table_name = 'department_info'


if __name__ == '__main__':
    # 若数据库中不存在相关表，则自动创建
    sql_db.create_tables([UserInfo, RankInfo, DepartmentInfo])
