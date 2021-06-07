# -*- coding: utf-8 -*-
# @File    : common.py
# @Date    : 2019-09-03-17:24
# @Author  : FangGang
# @Version : 1
import random

from public.KuXiuEnum import KuXiuEnum
from public.HttpRequests import HttpRequests
from public.Tool import Tool


def send_verification_code(mobile_num=str, code_type=str):
    """
    发送验证码 验证码类型：1-注册，2-实名认证，3-重置密码,4-绑定手机,5-更换手机,6-库存预警,7-用户登录
    :param mobile_num: 手机号
    :param code_type: 验证码类型
    :return:
    """
    url = 'https://pre.17kuxiu.com/user/getVerificationCode?mobile=%s&type=%s&areaCode=86' % (mobile_num, code_type)
    r = HttpRequests().send_r('post', url, None, Tool().headers_login()).json()
    return True if 200 == r['retCode'] else False


def get_hot_live_list():
    """
    获取热门直播列表
    :return:list[anchorId]
    """
    anchor_list = []
    h_url = 'https://pre.17kuxiu.com/supplement/live/hot/list/v2?currentPage=1'
    r = HttpRequests().send_r(method='get', u=h_url, d=None, h=Tool().headers()).json()
    if 200 == r['retCode'] and [] != r['data']:
        for i in range(len(r['data'])):
            anchor_list.append(r['data'][i]['anchorId'])
        return anchor_list
    else:
        return None


def get_personal_dynamic_id():
    """
    获取个人动态
    :return: list[PubId]
    """
    d_list = []
    url = KuXiuEnum.URL_DYNAMIC.value + '/timeline'
    json_data = {
        "category": "PERSONAL",
        "userId": Tool().userId,
    }
    r = HttpRequests().send_json(method='post', u=url, d=None, j=json_data, h=Tool().headers()).json()
    if 200 == r['retCode']:
        length = len(r['data'])
        if length == 0:
            return None
        if length > 0:
            for i in range(len(r['data'])):
                d_list.append(r['data'][i]['id'])
            return d_list
    else:
        return None


def get_all_dynamic_id():
    """
    获取全部动态id（只20条）
    :return: list[PubId]
    """
    ids = get_personal_dynamic_id()[random.randint(0, 19)]
    d_list = []
    url = KuXiuEnum.URL_DYNAMIC.value + '/timeline'
    json_data = {
        "category": "ALL",
        "page": 1,
        "currentLastPubId": ids
    }
    print(json_data)
    r = HttpRequests().send_json(method='post', u=url, d=None, j=json_data, h=Tool().headers()).json()
    if 200 == r['retCode']:
        length = len(r['data'])
        if length == 0:
            return None
        if length > 0:
            for i in range(len(r['data'])):
                d_list.append(r['data'][i]['id'])
            return d_list
    else:
        return None


def get_album_photos(type):
    """
    获取个人相册中的图片，如果没有待审核的图片列表，则返回已经过审的图片列表。如果都没有，返回[]
    :return: list[id] 图片id列表
    """
    i_list1 = []
    i_list2 = []
    url = KuXiuEnum.URL_USER.value + "/getUserPhotoList"
    try:
        r = HttpRequests().send_r(method='get', u=url, d=None, h=Tool().headers()).json()
        for i in range(len(r['data'])):
            if 0 == r['data'][i]['auditStatus']:
                i_list1.append(r['data'][i]['id'])
            else:
                i_list2.append(r['data'][i]['id'])
        if len(i_list1) > 0 and 0 == type:
            return i_list1
        elif len(i_list2) > 0 and 1 == type:
            return i_list2
        else:
            return []
    except Exception as e:
        print(e)
    finally:
        return []


def play_happy_draw(beans):
    """
    玩转盘游戏
    :param beans:转盘选项 1金豆游戏=1  10金豆游戏=2  100金豆游戏=3
    :return:True/False
    """
    url = "https://pre.17kuxiu.com/supplement/playFootball?teamId={}&gameId=2".format(beans)
    r = HttpRequests().send_r('post', url, None, Tool().headers()).json()
    if 200 == r['retCode']:
        print("玩欢乐转盘成功")
        return True
    elif -300015 == r['retCode']:
        print('接口超时')
        return False
    else:
        print('其他错误')
        return False

if __name__ == "__main__":
    print(get_hot_live_list())