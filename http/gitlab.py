# coding = utf-8
import requests
import json
import redis


def getGitlabUser():
    '''
    获取Gitlab用户，全部数据，token进行脱敏
    '''
    page = 1
    gitLabUsers = []
    while True:
        r = requests.get(
            'https://gitlab.wallstcn.com/api/v4/users?private_token=xx&page=' +
            str(page))
        data_json = json.loads(r.text)
        if len(data_json) > 0:
            # 将json数据中email state username name 取出来
            for info in data_json:
                info_dict = {}
                info_dict['email'] = info['email']
                info_dict['state'] = info['state']
                info_dict['name'] = info['name']
                info_dict['username'] = info['username']
                info_dict['id'] = info['id']
                gitLabUsers.append(info_dict)
            page += 1
            continue
        break
    return gitLabUsers


def getToken():
    '''
    获取企业微信的token
    '''
    # E3cK6z_gHCiH51mocqMy2wQMTyuGXjpHgZFCXeUNxMTrf2PnE--13r0l0zVHplqjhlv2KoMzC8-bmggQ0_ZuNsotDCFjzjyJlDNho9OqKdSvOsG9vnUAI9VrCr0rALQNmrVkjByODRgGaLP0JnebDn9v1FbXhk9InR-tIklTVARJEGho0vt64qmsad0duY_OWysSb864T_nPcn36H07eXA
    pool = redis.ConnectionPool(
        host='redis', port=6379, decode_responses=True, password='xx', db=0)
    red = redis.Redis(connection_pool=pool)
    # 获取redis中的数据
    access_token = red.get('qywx:access:token')

    if access_token is None:
        r = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=435&corpsecret=xxx'
        )
        # print(r.text)
        # 应该缓存到redis中
        access_token = json.loads(r.text)['access_token']
        red.set('qywx:access:token', access_token, ex=7000)

    return access_token


def getUserList(access_token):
    '''获取公司所有的员工
    '''
    r = requests.get(
        "https://qyapi.weixin.qq.com/cgi-bin/user/list?access_token=" +
        access_token + "&department_id=1&fetch_child=1")
    user_list = json.loads(r.text)['userlist']

    users = []
    for user in user_list:
        if user['status'] == 1:
            users.append(user['email'])

    return users


def main():
    # 先进行微信的认证
    access_token = getToken()
    wx_users = getUserList(access_token)
    gitlab_users = getGitlabUser()

    print(wx_users)
    print('---------------\n')
    print(gitlab_users)


if __name__ == '__main__':
    main()
