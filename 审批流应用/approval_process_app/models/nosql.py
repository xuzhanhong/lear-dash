# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# Time       ：2023/4/19
# Author     ：xuzhanhong
# Description：非关系型数据库数据模型
"""
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

# 连接或创建approval_process数据库
nosql_db = client['approval_process']


class ProcessMeta:
    """
    流程元信息表
    """

    def __init__(self) -> None:

        # 取得process_meta对应集合
        self.collection = nosql_db['process_meta']

    @staticmethod
    def init_collection() -> None:
        """慎用，用于强制初始化process_meta表，执行后会首先清除process_meta表，再创建process_meta表"""

        # 清除process_meta表
        nosql_db.drop_collection('process_meta')

        # 创建process_meta表
        nosql_db.create_collection(
            'process_meta',
            validator={
                '$jsonSchema': {
                    'bsonType': 'object',
                    'required': [
                        '流程id', '流程名称', '流程描述', '流程类型',
                        '可发起部门', '流程表单结构', '审批步骤'
                    ],
                    'properties': {
                        '流程id': {
                            'bsonType': 'string',
                            'description': '用于存储当前元信息对应流程的唯一标识'
                        },
                        '流程名称': {
                            'bsonType': 'string',
                            'description': '用于存储当前元信息对应流程的名称'
                        },
                        '流程描述': {
                            'bsonType': 'string',
                            'description': '用于存储当前元信息对应流程的描述'
                        },
                        '流程类型': {
                            'bsonType': 'string',
                            'description': '用于存储当前元信息对应流程的类型'
                        },
                        '可发起部门': {
                            'bsonType': 'array',
                            'description': '用于存储当前元信息对应流程的可发起部门，当存在“全部”项时，用于表示当前流程可由全部部门发起',
                            'items': {
                                'bsonType': 'string'
                            }
                        },
                        '流程表单结构': {
                            'bsonType': 'array',
                            'description': '用于存储当前元信息对应流程的需填写表单结构',
                            'items': {
                                'bsonType': 'object',
                                'required': [
                                    '字段名', '字段描述', '类型', '是否必填'
                                ],
                                'properties': {
                                    '字段名': {
                                        'bsonType': 'string',
                                        'description': '声明当前表单项的字段名'
                                    },
                                    '字段描述': {
                                        'bsonType': 'string',
                                        'description': '声明当前表单项的字段描述'
                                    },
                                    '类型': {
                                        'bsonType': 'string',
                                        'description': '声明当前表单项的类型，可选的有字符型、整型、浮点型、年份型、年月型、日期型、日期时间型及时间型'
                                    },
                                    '是否必填': {
                                        'bsonType': 'bool',
                                        'description': '声明当前表单项是否必填'
                                    },
                                    '约束条件': {
                                        'bsonType': 'object',
                                        'description': '声明当前表单项的约束条件',
                                        'required': ['约束类型'],
                                        'properties': {
                                            '约束类型': {
                                                'bsonType': 'string',
                                                'description': '声明当前表单项的约束类型，可选的范围约束、枚举约束'
                                            },
                                            '枚举范围': {
                                                'bsonType': 'array',
                                                'description': '声明当前表单项的枚举范围，如[a, b, c]',
                                                'items': {
                                                    'bsonType': 'string'
                                                }
                                            },
                                            '下限': {
                                                'bsonType': ['int', 'number', 'string'],
                                                'description': '声明当前表单项的下限'
                                            },
                                            '上限': {
                                                'bsonType': ['int', 'number', 'string'],
                                                'description': '声明当前表单项的上限'
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        '审批步骤': {
                            'bsonType': 'array',
                            'description': '用于存储当前元信息对应流程的审批步骤规则',
                            'items': {
                                'bsonType': 'object',
                                'required': [
                                    '步骤名称', '步骤描述', '步骤次序', '是否允许跳过',
                                    '是否为末尾节点', '审批人规则'
                                ],
                                'properties': {
                                    '步骤名称': {
                                        'bsonType': 'string',
                                        'description': '声明当前步骤的名称'
                                    },
                                    '步骤描述': {
                                        'bsonType': 'string',
                                        'description': '声明当前步骤的描述'
                                    },
                                    '步骤次序': {
                                        'bsonType': 'int',
                                        'description': '声明当前步骤的次序'
                                    },
                                    '是否允许跳过': {
                                        'bsonType': 'bool',
                                        'description': '声明当前步骤是否允许跳过'
                                    },
                                    '是否为末尾节点': {
                                        'bsonType': 'bool',
                                        'description': '声明当前步骤是否为末尾节点'
                                    },
                                    '审批人规则': {
                                        'bsonType': 'object',
                                        'description': '声明当前步骤的审批人规则',
                                        'required': [
                                            '规则类型'
                                        ],
                                        'properties': {
                                            '规则类型': {
                                                'bsonType': 'string',
                                                'description': '声明当前步骤的审批人规则类型，可选的有自定义审批人、相对职级审批人、特定审批人'
                                            },
                                            '规则目标': {
                                                'bsonType': 'string',
                                                'description': '声明当前步骤的审批人规则目标，规则类型为特定审批人时传入对应的用户idF，规则类型为相对职级审批人时可选项有部门副职、部门正职、公司副职、公司正职'
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        )

        # 取得已重置的collection
        process_meta_collection = nosql_db['process_meta']

        # 构建针对流程id的唯一值索引约束
        process_meta_collection.create_index(
            '流程id',
            unique=True,
            background=True
        )

        # 构建针对流程名称的唯一值索引约束
        process_meta_collection.create_index(
            '流程名称',
            unique=True,
            background=True
        )


def init_db(init_process_meta: bool = False):
    """慎用，用于强制重置数据库用

    Args:
        init_process_meta (bool, optional): 设置是否针对process_meta进行重置. Defaults to False.
    """

    if init_process_meta:
        ProcessMeta.init_collection()
        print('集合process_meta重置成功')
