import os
import dash
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Input, Output, State, ALL

# 导入flask中的相关功能
from flask import request, send_from_directory

app = dash.Dash(__name__)

server = app.server


@server.route('/upload/', methods=['POST'])
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


@server.route('/download')
def download():
    '''
    构建文件上传服务
    :return:
    '''

    # 提取文件路径参数
    path = request.values.get('path'),

    # 提取文件名称参数
    file = request.values.get('file')

    return send_from_directory(os.path.join('caches', path[0]), file)


app.layout = html.Div(
    [
        html.Div(
            [
                fac.AntdUpload(
                    id='upload',
                    apiUrl='/upload/',
                    uploadId='my-files',
                    fileListMaxLength=1
                ),
                fac.AntdDivider(
                    '已上传文件列表',
                    isDashed=True
                ),
                fac.AntdSpace(
                    id='uploaded-file-list',
                    direction='vertical',
                    style={
                        'width': '100%'
                    }
                )
            ],
            style={
                'minHeight': '300px',
                'boxShadow': '0 6px 16px rgb(107 147 224 / 14%)',
                'borderRadius': '12px',
                'padding': '25px'
            }
        )
    ],
    style={
        'padding': '50px 100px'
    }
)


@app.callback(
    Output('uploaded-file-list', 'children'),
    [Input('upload', 'lastUploadTaskRecord'),
     Input({'type': 'delete-confirm', 'index': ALL}, 'confirmCounts')],
    State('uploaded-file-list', 'children')
)
def render_uploaded_file_list(lastUploadTaskRecord, confirmCounts, children):
    triggered_id = dash.callback_context.triggered[0]['prop_id']

    if '.confirmCounts' in triggered_id:
        should_delete_file = eval(triggered_id.replace('.confirmCounts', ''))['index']

        # 尝试删除指定文件
        os.remove(os.path.join('caches/my-files',
                               should_delete_file))

        new_file_list = [file for file in children if
                         file['props']['children'][1]['props']['children'] != should_delete_file]

        return new_file_list or fac.AntdEmpty(
            description='目录下暂无文件'
        )

    # 获取当前状态下caches目录下设定的目录中所有文件名称
    file_list = os.listdir('caches/my-files')

    if not file_list:
        return fac.AntdEmpty(
            description='目录下暂无文件'
        )

    return [
        fac.AntdSpace(
            [
                fac.AntdIcon(icon='fc-file'),
                html.A(
                    file,
                    href='/download?path={}&file={}'.format('my-files', file),
                    target='_blank'
                ),
                fac.AntdPopconfirm(
                    fac.AntdIcon(
                        icon='antd-delete',
                        style={
                            'color': '#ff4d4f',
                            'cursor': 'pointer'
                        }
                    ),
                    id={
                        'type': 'delete-confirm',
                        'index': file
                    },
                    title='删除文件'
                )
            ]
        )
        for i, file in enumerate(file_list)
    ]


if __name__ == '__main__':
    app.run_server(debug=True)
