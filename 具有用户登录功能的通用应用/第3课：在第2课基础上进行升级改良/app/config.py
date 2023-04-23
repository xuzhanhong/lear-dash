import os


class PathConfig:

    # 项目绝对根目录
    ABS_ROOT_PATH = os.path.abspath(os.getcwd())


class RouterConfig:

    # 合法pathname列表
    VALID_PATHNAME = [
        '/', '/login'
    ]

    # 合法主页面侧边应用hash列表
    VALID_HASH = [
        '',
        *[
            f'sub-app{i}'
            for i in range(1, 25)
        ]
    ]
