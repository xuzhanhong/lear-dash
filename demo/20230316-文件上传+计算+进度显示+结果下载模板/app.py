import os
import time
import uuid
import dash
import shutil
from dash import html, dcc
from datetime import datetime
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State, ALL

from server import app
from models import db, Tasks

app.layout = html.Div(
    [
        # 用一组Store中转，从而记录必要信息
        # 待dash 2.9.0版本发布后，再计划改造成更简便的写法
        html.Div(
            [
                dcc.Store(
                    id={
                        'type': 'store-group',
                        'index': 'create-task'
                    },
                    clear_data=True
                ),
                dcc.Store(
                    id={
                        'type': 'store-group',
                        'index': 'confirm-task'
                    },
                    clear_data=True
                ),
                dcc.Store(
                    id={
                        'type': 'store-group',
                        'index': 'execute-task'
                    },
                    clear_data=True
                )
            ]
        ),

        fuc.FefferyDiv(
            [
                html.Div(
                    fac.AntdText(
                        'xxx在线计算工具',
                        strong=True,
                        style={
                            'fontSize': 48,
                            'color': 'white'
                        }
                    ),
                    style={
                        'textAlign': 'center',
                        'background': '#119dff',
                        'borderRadius': '6px 6px 0 0'
                    }
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdParagraph(
                                    '请上传要处理的文件',
                                    style={
                                        'fontSize': 20
                                    }
                                ),
                                fac.AntdDraggerUpload(
                                    id='task-file',
                                    apiUrl='/upload',
                                    text='上传需要进行处理的文件',
                                    hint='大小请不要超过100mb',
                                    fileMaxSize=100,
                                    fileListMaxLength=1
                                ),
                                fac.AntdButton(
                                    '开始计算',
                                    id='start-task',
                                    type='primary',
                                    block=True
                                )
                            ],
                            direction='vertical',
                            style={
                                'width': '100%'
                            }
                        )
                    ],
                    id='operation-container',
                    style={
                        'width': '60%',
                        'margin': '0 auto',
                        'paddingTop': 50
                    }
                )
            ],
            style={
                'borderRadius': 6,
                'border': '1px solid #e9ecef',
                'minHeight': 700,
                'width': '60vw',
                'margin': '0 auto'
            },
            shadow='always-shadow'
        )
    ],
    style={
        'paddingTop': 100
    }
)


@app.callback(
    Output(
        {
            'type': 'store-group',
            'index': 'confirm-task'
        },
        'data'
    ),
    # 随意选择Input，仅用于第二步页面内容加载后初始化触发任务执行使用
    Input('confirm-button', 'id'),
    State(
        {
            'type': 'store-group',
            'index': 'create-task'
        },
        'data'
    )
)
def confirm_task(nClicks):
    return {
        '支付成功': True
    }


@app.callback(
    Output('operation-container', 'children'),
    [
        Input(
            {
                'type': 'store-group',
                'index': 'create-task'
            },
            'data'
        ),
        Input(
            {
                'type': 'store-group',
                'index': 'execute-task'
            },
            'data'
        ),
        Input(
            {
                'type': 'store-group',
                'index': 'confirm-task'
            },
            'data'
        )
    ],
    prevent_initial_call=True
)
def render_operation_layout(create_task_info,
                            confirm_task_info,
                            done_task_info
                            ):
    '''负责监听每一步结果Store的更新，从而渲染新一步的页面元素'''

    if dash.ctx.triggered_id and create_task_info:
        # 若本次回调由第一步的目标Store触发
        if dash.ctx.triggered_id['index'] == 'create-task':

            # 返回第二步任务运行中相关内容
            return [
                # 轮询，用于触发当前任务进度查询
                dcc.Interval(
                    id='task-progress-query-trigger',
                    interval=1000
                ),

                fac.AntdSpace(
                    [
                        fac.AntdText(
                            create_task_info['upload_file_name'],
                            style={
                                'fontSize': 24
                            }
                        ),
                        fac.AntdText(
                            '创建时间：{}'.format(
                                create_task_info['create_datetime']
                            ),
                            type='secondary'
                        ),
                        fac.AntdProgress(
                            id='task-progress',
                            percent=create_task_info['task_progress'],
                            style={
                                'width': '100%'
                            }
                        )
                    ],
                    direction='vertical',
                    style={
                        'textAlign': 'center',
                        'width': '100%',
                        'paddingTop': 100
                    }
                )
            ]

        # 若本次回调由第一步的目标Store触发
        elif dash.ctx.triggered_id['index'] == 'execute-task':
            return fac.AntdCol(
                [
                    fac.AntdButton(
                        '确认计算',
                        id='confirm-button'
                    )
                ]
            )

        # 若本次回调由第二步的目标Store触发
        elif dash.ctx.triggered_id['index'] == 'confirm-task':

            return fac.AntdResult(
                status='success',
                title='任务计算完成',
                subTitle=[
                    fac.AntdParagraph(
                        [
                            '点击',
                            html.A(
                                '此处',
                                target='_blank',
                                href='/download?path={}&filename={}'.format(
                                    done_task_info['download_id'],
                                    done_task_info['upload_file_name']
                                )
                            ),
                            '下载结算结果'
                        ]
                    ),
                    fac.AntdButton(
                        '创建新任务',
                        href='/',
                        type='primary'
                    )
                ]
            )

    return dash.no_update


@app.callback(
    Output('start-task', 'disabled'),
    Input('task-file', 'listUploadTaskRecord')
)
def sync_start_task_disabled(listUploadTaskRecord):
    '''负责在有合法文件上传后解除按钮的禁用状态'''

    return not bool(listUploadTaskRecord)


@app.callback(
    Output(
        {
            'type': 'store-group',
            'index': 'create-task'
        },
        'data'
    ),
    Input('start-task', 'nClicks'),
    State('task-file', 'lastUploadTaskRecord'),
    prevent_initial_call=True
)
def update_first_step_store(nClicks,
                            lastUploadTaskRecord):
    '''处理新任务的创建，将任务信息存入第一步的Store中'''

    new_task_info = {
        'task_id': str(uuid.uuid4()),
        'upload_id': lastUploadTaskRecord['taskId'],
        'upload_file_name': lastUploadTaskRecord['fileName'],
        'create_datetime': datetime.now(),
        'task_progress': 0
    }

    with db.atomic():

        (
            Tasks
            .insert(**new_task_info)
            .execute()
        )

    return new_task_info


@app.callback(
    Output(
        {
            'type': 'store-group',
            'index': 'execute-task'
        },
        'data'
    ),
    # 随意选择Input，仅用于第二步页面内容加载后初始化触发任务执行使用
    Input('task-progress-query-trigger', 'id'),
    State(
        {
            'type': 'store-group',
            'index': 'create-task'
        },
        'data'
    )
)
def trigger_task_execute(_, task_info):
    '''模拟耗时计算任务'''

    # 为方便演示，模拟任务执行，实际生产项目中请换做celery之类的异步任务中执行
    for i in range(10):
        # 更新任务进度
        with db.atomic():
            (
                Tasks
                .update(
                    {
                        Tasks.task_progress: (i + 1) / 10
                    }
                )
                .where(
                    Tasks.task_id == task_info['task_id']
                )
                .execute()
            )

        time.sleep(1)

    # 以复制任务文件到下载路径下来模拟真实任务结果的导出
    download_id = str(uuid.uuid4())

    os.mkdir(os.path.join('results', download_id))

    shutil.copyfile(
        os.path.join(
            'caches',
            task_info['upload_id'],
            task_info['upload_file_name']
        ),
        os.path.join(
            'results',
            download_id,
            task_info['upload_file_name']
        )
    )

    # 更新任务完成时间等信息
    with db.atomic():
        (
            Tasks
            .update(
                {
                    Tasks.task_progress: 1,
                    Tasks.complete_datetime: datetime.now(),
                    Tasks.download_id: download_id
                }
            )
            .where(
                Tasks.task_id == task_info['task_id']
            )
            .execute()
        )

    # 查询当前任务全部信息
    with db.atomic():
        done_task_info = list(
            Tasks
            .select()
            .where(
                Tasks.task_id == task_info['task_id']
            )
            .dicts()
        )[0]

    # 返回当前已完成任务相关信息
    return done_task_info


@app.callback(
    Output('task-progress', 'percent'),
    Input('task-progress-query-trigger', 'n_intervals'),
    State(
        {
            'type': 'store-group',
            'index': 'create-task'
        },
        'data'
    )
)
def update_running_task_progress(_, task_info):
    '''基于轮询查询最新任务进度并输出到页面进度条中'''

    # 查询目标任务最新进度
    with db.atomic():
        task_progress = list(
            Tasks
            .select(Tasks.task_progress)
            .where(
                Tasks.task_id == task_info['task_id']
            )
            .dicts()
        )[0]['task_progress']

    return round(task_progress * 100, 1)


if __name__ == '__main__':
    app.run(debug=True)
