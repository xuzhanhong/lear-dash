# -*- encoding: utf-8 -*-
"""
@Date       : 2023/04/22
@Author     : xuzhanhong
@Description: 查询接口
"""
from fastapi import APIRouter

router = APIRouter()

@router.get('/test2')
def test1() -> str:

    return '这是查询接口中的test2接口'

