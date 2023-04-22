# 用于复杂类型声明
from typing import Union, List
from fastapi import FastAPI
from pydantic import BaseModel

# 导入子路由
from routers import manage, query

# 实例化FastAPI应用对象
app = FastAPI()


@app.get('/sum-api')
def sum_api(a: int = 0, b: int = 0) -> dict:

    return {
        'result': a + b
    }


class PostDemo(BaseModel):

    # 声明输入参数input_list
    input_list: List[Union[int, float]]


@app.post('/post-demo')
def post_demo(params: PostDemo):

    return {
        'min': min(params.input_list),
        'max': max(params.input_list)
    }


# 并入管理接口
app.include_router(
    manage.router,
    prefix='/manage',
    tags=['管理接口']
)

# 并入查询接口
app.include_router(
    query.router,
    prefix='/query',
    tags=['查询接口']
)
