import hashlib

def md5_token(str_):
    hash = hashlib.md5()
    hash.update(str_.encode('utf-8'))
    return hash.hexdigest()

def get_token(p_dict):
    """
    获取家长端token
    :param kwg:
    :return:
    """
    empty_list = []
    for k, v in p_dict.items():
        content_temp = '{}={}'.format(k, v)
        empty_list.append(content_temp)
    # 按ascii码排序
    empty_list.sort()
    md5_content_args = '&'.join(empty_list)
    # wilson-新增MD5加密

    # 第一次加密
    content = md5_token(md5_content_args)
    # 第二次加密
    token = md5_token(content + 'kobe')
    return token

print(get_token({"studentId":138079,"parentId":138145}))