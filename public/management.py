# -*- coding: utf-8 -*-

# @File    : managementLogin.py
# @Date    : 2019-09-25-17:43
# @Author  : FangGang
# @Version : 1
from public.HttpRequests import HttpRequests


def management_login():
    """
    后台登录
    :return: token, userId
    """
    url = 'http://pre.17kuxiu.com/mgmt/user/login?userName=testforinterface&pwd=123456&loginType=9'
    r = HttpRequests().send_r('post', u=url, d=None, h=None).json()
    if 200 == r['retCode']:
        accessToken = r['data']['accessToken']
        return accessToken
    else:
        return False


def get_magic_draw_pool(accessToken):
    """
    后台查询魔法转盘库存值
    :return:魔法转盘库存值
    """
    url = 'http://pre.17kuxiu.com/mgmt/supplement/getGameMiscConfig?gameId=4'
    r = HttpRequests().send_r('get', u=url, d=None, h={'accessToken': accessToken}).json()
    if 200 == r['retCode']:
        return r['data']['coinPool']
    else:
        return False

# management_login()
