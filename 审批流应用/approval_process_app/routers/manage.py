# -*- encoding: utf-8 -*-
"""
@Date       : 2023/04/22
@Author     : xuzhanhong
@Description: 管理接口
"""
from fastapi import APIRouter

router = APIRouter()


@router.get('/test1')
def test1() -> str:

    return '这是管理接口中的test1接口'
