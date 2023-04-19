from fastapi import APIRouter

router = APIRouter()

@router.get('/test2')
def test1() -> str:

    return '这是查询接口中的test2接口'