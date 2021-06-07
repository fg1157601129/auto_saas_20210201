# -*- coding: utf-8 -*-
# @File    : PhoneLogin.py
# @Date    : 2019-05-07-19:43
# @Author  : FangGang
# @Version : 1
# from config import read_all
from public.HttpRequests import HttpRequests
from public.ProjectPath import ProjectPath
from public.Tool import Tool
import yaml


class PhoneLogin:
    """手机号登录接口"""

    def __init__(self):
        self.mobile = Tool().mobile  # 从配置文件获取mobile
        self.password = Tool().password  # 对密码md5加密
        self.baseurl = 'http://pre.17kuxiu.com/user/login?sign={}'
        self.data = {'mobile': self.mobile,
                     "password": self.password,
                     'channel': '1',
                     'areaCode': '86'}

    def do_login(self):
        """读取配置文件中的用户名和密码登录
        :return:userId
        """
        url = self.baseurl.format(Tool().sgin())
        res = HttpRequests().send_r(method='post', u=url, d=self.data, h=Tool().headers_login())
        if res.status_code == 200:
            r = res.json()
            if 200 == r['retCode']:
                s = read_all()
                s["AccessToken"]["token1"] = r['data']['accessToken']
                s["TestAccount"]["userId"] = r['data']['userId']
                with open(file=ProjectPath().config_path, mode='w', encoding='utf-8') as fw:
                    yaml.dump(data=s, stream=fw)
                return r
            else:
                print('登录失败')
        else:
            print('接口访问出错')

    def do_login_with_phone(self, mobile, psw):
        """使用指定用户名密码登录
        :return:userId
        """
        data = dict(mobile=mobile, password=Tool().md5(psw), channel='1', areaCode='86')
        url = self.baseurl.format(Tool().sgin())
        res = HttpRequests().send_r(method='post', u=url, d=data, h=Tool().headers_login())
        if res.status_code == 200:
            r = res.json()
            if 200 == r['retCode']:
                uid = str(r['data']['userId'])
                token = str(r['data']['accessToken'])
                return uid, token
            else:
                print('登录失败')
        else:
            print('接口访问出错')


if __name__ == '__main__':
    print(PhoneLogin().do_login())
    # print(PhoneLogin().do_login_with_phone(mobile='14782376210', psw='111111'))
    # print(PhoneLogin().do_login_with_phone('18616296325', '123456'))
