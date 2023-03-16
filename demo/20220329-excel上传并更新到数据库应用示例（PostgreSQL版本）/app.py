import os
import dash
import pandas as pd
from dash import html
from flask import request
import feffery_antd_components as fac
from dash.dependencies import Input, Output, State

from models import DemoTable1, DemoTable2

app = dash.Dash(__name__)


@app.server.route('/upload/', methods=['POST'])
def upload():
    '''
    构建文件上传服务
    :return:
    '''

    # 获取上传id参数，用于指向保存路径
    uploadId = request.values.get('uploadId')

    # 获取上传的文件名称
    filename = request.files['file'].filename

    # 基于上传id，若本地不存在则会自动创建目录
    try:
        os.mkdir(os.path.join('caches', uploadId))
    except FileExistsError:
        pass

    # 流式写出文件到指定目录
    with open(os.path.join('caches', uploadId, filename), 'wb') as f:
        # 流式写出大型文件，这里的10代表10MB
        for chunk in iter(lambda: request.files['file'].read(1024 * 1024 * 10), b''):
            f.write(chunk)

    return {'filename': filename}


app.layout = html.Div(
    html.Div(
        [
            fac.AntdForm(
                [
                    fac.AntdFormItem(
                        fac.AntdSpace(
                            [
                                fac.AntdRadioGroup(
                                    id='table-select',
                                    options=[
                                        {
                                            'label': '订单表',
                                            'value': '订单表'
                                        },
                                        {
                                            'label': '部门任务表',
                                            'value': '部门任务表'
                                        }
                                    ],
                                    optionType='button',
                                    buttonStyle='solid',
                                    defaultValue='订单表'
                                ),
                                html.A(
                                    '上传表格模板下载',
                                    id='template-table-download'
                                )
                            ],
                            addSplitLine=True
                        ),
                        label='数据表选择'
                    ),

                    fac.AntdFormItem(
                        fac.AntdRadioGroup(
                            id='update-strategy',
                            options=[
                                {
                                    'label': '失败反馈',
                                    'value': '失败反馈'
                                },
                                {
                                    'label': '跳过冲突记录',
                                    'value': '跳过冲突记录'
                                },
                                {
                                    'label': '覆盖冲突记录',
                                    'value': '覆盖冲突记录'
                                }
                            ],
                            optionType='button',
                            buttonStyle='solid',
                            defaultValue='失败反馈'
                        ),
                        label='数据更新策略'
                    ),

                    fac.AntdFormItem(
                        fac.AntdUpload(
                            id='upload',
                            apiUrl='/upload/',
                            buttonContent='点击上传表格文件',
                            fileListMaxLength=1,
                            fileTypes=['xlsx', 'xls']
                        ),
                        label='数据上传',
                        tooltip='请上传xlsx或xls格式的数据文件'
                    )
                ]
            ),
            fac.AntdDivider(isDashed=True),
            html.Div(
                fac.AntdResult(
                    title='暂无新的数据上传',
                    subTitle='请在上方完成数据文件的上传'
                ),
                id='result-message-container'
            )
        ],
        style={
            'padding': '40px',
            'boxShadow': '0 6px 16px rgb(107 147 224 / 14%)',
            'borderRadius': '8px'
        }
    ),
    style={
        'padding': '100px'
    }
)


@app.callback(
    Output('template-table-download', 'href'),
    Input('table-select', 'value')
)
def change_template_table_download_link(value):
    '''
    根据表格选择情况更新模板表格文件下载链接
    '''
    return dash.get_asset_url(f'模板表格/{value}模板.xlsx')


@app.callback(
    Output('result-message-container', 'children'),
    Input('upload', 'lastUploadTaskRecord'),
    [State('table-select', 'value'),
     State('update-strategy', 'value')],
    prevent_initial_call=True
)
def uploaded_table_to_database(lastUploadTaskRecord, table_name, update_strategy):
    if table_name == '订单表':
        # 从本地文件读入触发本次回调所上传的数据表格
        uploaded_table = pd.read_excel(os.path.join('caches',
                                                    lastUploadTaskRecord['taskId'],
                                                    lastUploadTaskRecord['fileName']))

        # 这里可以根据你的需要写多条条件分支检查数据合法性，以字段名为例
        try:
            uploaded_table = (
                uploaded_table
                    .rename(columns={
                    '订单编号': 'order_id',
                    '商品名称': 'item_name',
                    '商品数量': 'amount',
                    '商品单价': 'unit_price'
                })
                [['order_id', 'item_name', 'amount', 'unit_price']]
            )
        except:
            return fac.AntdResult(
                title='数据入库失败',
                subTitle='请检查字段名是否与模板表要求一致',
                status='error'
            )

        # 根据不同的策略处理数据更新
        if update_strategy == '失败反馈':

            try:
                # 尝试推送数据到数据库
                query = (
                    DemoTable1
                        .insert_many(uploaded_table.to_dict('records'))
                        .execute()
                )
            except Exception as e:
                return fac.AntdResult(
                    title='数据入库失败',
                    subTitle=str(e),
                    status='error'
                )

        elif update_strategy == '跳过冲突记录':
            try:
                # 尝试推送数据到数据库
                query = (
                    DemoTable1
                        .insert_many(uploaded_table.to_dict('records'))
                        .on_conflict_ignore()
                        .execute()
                )
            except Exception as e:
                return fac.AntdResult(
                    title='数据入库失败',
                    subTitle=str(e),
                    status='error'
                )

        else:
            try:
                # 尝试推送数据到数据库
                query = (
                    DemoTable1
                        .insert_many(uploaded_table.to_dict('records'))
                        .on_conflict(conflict_target=[DemoTable1.order_id],
                                     preserve=[DemoTable1.item_name,
                                               DemoTable1.amount,
                                               DemoTable1.unit_price])
                        .execute()
                )
            except Exception as e:
                return fac.AntdResult(
                    title='数据入库失败',
                    subTitle=str(e),
                    status='error'
                )

        return fac.AntdResult(
            title='【订单表】数据入库成功',
            status='success'
        )

    elif table_name == '部门任务表':
        # 从本地文件读入触发本次回调所上传的数据表格
        uploaded_table = pd.read_excel(os.path.join('caches',
                                                    lastUploadTaskRecord['taskId'],
                                                    lastUploadTaskRecord['fileName']))

        # 这里可以根据你的需要写多条条件分支检查数据合法性，以字段名为例
        try:
            uploaded_table = (
                uploaded_table
                    .rename(columns={
                    '部门': 'apartment',
                    '部门任务序号': 'task_id',
                    '任务开始时间': 'task_start_datetime',
                    '任务结束时间': 'task_end_datetime',
                    '任务内容描述': 'task_description'
                })
                [['apartment', 'task_id', 'task_start_datetime', 'task_end_datetime', 'task_description']]
            )
        except:
            return fac.AntdResult(
                title='数据入库失败',
                subTitle='请检查字段名是否与模板表要求一致',
                status='error'
            )

        # 根据不同的策略处理数据更新
        if update_strategy == '失败反馈':

            try:
                # 尝试推送数据到数据库
                query = (
                    DemoTable2
                        .insert_many(uploaded_table.to_dict('records'))
                        .execute()
                )
            except Exception as e:
                return fac.AntdResult(
                    title='数据入库失败',
                    subTitle=str(e),
                    status='error'
                )

        elif update_strategy == '跳过冲突记录':
            try:
                # 尝试推送数据到数据库
                query = (
                    DemoTable2
                        .insert_many(uploaded_table.to_dict('records'))
                        .on_conflict_ignore()
                        .execute()
                )
            except Exception as e:
                return fac.AntdResult(
                    title='数据入库失败',
                    subTitle=str(e),
                    status='error'
                )

        else:
            try:
                # 尝试推送数据到数据库
                query = (
                    DemoTable2
                        .insert_many(uploaded_table.to_dict('records'))
                        .on_conflict(conflict_target=[DemoTable2.apartment,
                                                      DemoTable2.task_id],
                                     preserve=[DemoTable1.task_start_datetime,
                                               DemoTable1.task_end_datetime,
                                               DemoTable1.task_description])
                        .execute()
                )
            except Exception as e:
                return fac.AntdResult(
                    title='数据入库失败',
                    subTitle=str(e),
                    status='error'
                )

        return fac.AntdResult(
            title='【部门任务表】数据入库成功',
            status='success'
        )

    return dash.no_update


if __name__ == '__main__':
    app.run_server(debug=True)
