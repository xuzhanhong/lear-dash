import os
import dash
import time
import shutil
import tempfile
from dash import html
from datetime import datetime
import feffery_antd_components as fac
import feffery_utils_components as fuc
from flask import request, send_from_directory
from dash.dependencies import Input, Output, State

# 目标路径示例，请自行修改为你本机的某个地址
TARGET_PATH = r'C:\Users\CNFeffery\Desktop\知识星球课程\我们谈论数据科学\「实用主义Git教程」\压缩包'

# 为当前项目创建下载文件存放目录
if not os.path.exists('./download'):
    os.mkdir('./download')

app = dash.Dash(__name__)


@app.server.route('/download')
def download_api():
    '''示例下载服务'''

    file_name = request.args.get('file_name')

    return send_from_directory(
        './download',
        file_name
    )


app.layout = html.Div(
    [
        fac.AntdButton(
            '点击下载',
            id='download-selected-files',
            type='primary',
            autoSpin=True,
            loadingChildren='打包中',
            disabled=True
        ),
        fuc.FefferyExecuteJs(
            id='access-download-url'
        ),
        fac.AntdDivider(isDashed=True),

        # 垂直显示
        fuc.FefferyStyle(
            rawStyle='''
#file-list .ant-checkbox-wrapper {
    display: flex;
}
'''
        ),
        fac.AntdSpace(
            [
                fac.AntdCheckbox(
                    id='file-list-select-all',
                    label='全选',
                    checked=False
                ),
                fac.AntdCheckboxGroup(
                    id='file-list',
                    value=[]
                )
            ],
            size=0,
            direction='vertical',
            style={
                'width': '100%'
            }
        )
    ],
    style={
        'padding': '50px 100px'
    }
)


@app.callback(
    Output('file-list', 'options'),
    Input('file-list', 'id')
)
def render_file_list(_):
    '''初始化文件列表'''

    return [
        {
            'label': file,
            'value': file
        }
        for file in os.listdir(TARGET_PATH)
    ]


@app.callback(
    [Output('file-list-select-all', 'checked'),
     Output('file-list', 'value'),
     Output('file-list-select-all', 'indeterminate')],
    [Input('file-list-select-all', 'checked'),
     Input('file-list', 'value')],
    State('file-list', 'options'),
    prevent_initial_call=True
)
def handle_select(select_all, selected_files, file_list):
    '''控制全选与子项选择之间的状态及样式刷新'''

    if dash.ctx.triggered_id == 'file-list-select-all':
        if select_all:
            return [
                dash.no_update,
                [item['value'] for item in file_list],
                False
            ]

        return [
            dash.no_update,
            [],
            False
        ]

    elif dash.ctx.triggered_id == 'file-list':
        if len(selected_files) == len(file_list):
            return [
                True,
                dash.no_update,
                False
            ]

        elif len(selected_files) == 0:
            return [
                False,
                dash.no_update,
                False
            ]

        return [
            False,
            dash.no_update,
            True
        ]


@app.callback(
    Output('download-selected-files', 'disabled'),
    Input('file-list', 'value'),
    prevent_initial_call=True
)
def update_download_button_disabled(value):
    '''在未选中文件时禁用按钮'''

    return not bool(value)


@app.callback(
    [Output('access-download-url', 'jsString'),
     Output('download-selected-files', 'loading')],
    Input('download-selected-files', 'nClicks'),
    State('file-list', 'value'),
    prevent_initial_call=True
)
def handle_download(nClicks, file_list):
    '''处理文件打包下载过程'''

    if nClicks and file_list:

        time.sleep(0.5)

        with tempfile.TemporaryDirectory() as p:

            for file in file_list:
                shutil.copy(
                    os.path.join(TARGET_PATH, file),
                    p
                )

            zip_file_name = '打包下载{}'.format(
                datetime.now().strftime(
                    '%Y%m%d%H%M%S'
                )
            )

            shutil.make_archive(
                os.path.join('./download', zip_file_name),
                'zip',
                p
            )

        return [
            'window.open("{}")'.format(
                f'/download?file_name={zip_file_name}.zip'
            ),
            False
        ]


if __name__ == '__main__':
    app.run(debug=True)
