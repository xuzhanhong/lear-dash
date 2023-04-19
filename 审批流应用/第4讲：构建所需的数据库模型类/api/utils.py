import hashlib


def str2md5(raw_str: str) -> str:
    """对字符串进行md5加密

    Args:
        raw_str (str): 输入的待加密字符串

    Returns:
        str: 加密后的md5值
    """

    m = hashlib.md5()
    m.update(raw_str.encode('utf-8'))

    return m.hexdigest()
