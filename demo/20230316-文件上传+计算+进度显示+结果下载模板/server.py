import os
import dash
from flask import request, send_from_directory

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    update_title=None
)


@app.server.route('/upload', methods=['POST'])
def upload():

    uploadId = request.values.get('uploadId')
    filename = request.files['file'].filename

    try:
        os.mkdir(os.path.join('caches', uploadId))
    except FileExistsError:
        pass
    with open(os.path.join('caches', uploadId, filename), 'wb') as f:
        for chunk in iter(lambda: request.files['file'].read(1024 * 1024 * 10), b''):
            f.write(chunk)

    return {'filename': filename}


@app.server.route('/download')
def download():

    path = request.args.get('path')
    filename = request.args.get('filename')

    return send_from_directory(
        os.path.join('results', path),
        filename
    )
