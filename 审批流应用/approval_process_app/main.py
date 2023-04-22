from fastapi import FastAPI

# 导入所需的数据库模型类
from models.nosql import ProcessMeta

# 实例化FastAPI应用对象
app = FastAPI()

# 实例化流程元信息表模型类
process_meta = ProcessMeta()


@app.get('/query-process-name-and-description')
def query_process_name_and_description(process_id: str) -> dict:
    print(process_id)
    try:

        # 尝试查询目标流程信息
        match_process = list(
            process_meta
            .collection
            .find(
                {
                    '流程id': process_id
                },
                {
                    '_id': 0,
                    '流程名称': 1,
                    '流程描述': 1
                }
            )
        )[0]

        return {
            'status': 'success',
            'data': match_process
        }

    except Exception as e:

        return {
            'status': 'error',
            'message': str(e)
        }
