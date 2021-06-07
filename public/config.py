# -*- coding: utf-8 -*-
# @File    : config.py
# @Date    : 2019-03-25-18:01
# @Author  : FangGang
import os
from typing import Union
import numpy as np
import yaml

proDir = os.path.split(os.path.realpath(__file__))[0]  # 当前文件所在的目录
#configPath: Union[bytes, str] = os.path.join(proDir, "config.yaml")
configPath: Union[bytes, str] = os.path.join(proDir, "data_case_demo.yaml")


def read_all(kwargs=None):
    if kwargs is None:
        with open(file=configPath, mode='r', encoding='utf-8') as fd:
            content = yaml.full_load(fd.read())
    else:
        with open(file=configPath, mode='r', encoding='utf-8') as fd:
            content = (yaml.full_load(fd.read()))[kwargs]
    return content


def read_test_account():
    testAccount = read_all()['TestAccount']
    return testAccount


def read_app_info():
    appInfo = read_all()['AppInfo']
    return appInfo


def read_mobile_info():
    mobileInfo = read_all()['MobileInfo']
    return mobileInfo


def read_token():
    mobileInfo = read_all()["AccessToken"]
    return mobileInfo





def init_config():
    d = dict(
        {
            "AccessToken": {
                "token1": ""
            },
            "AppInfo": {
                "secretkey": "792f28d6ff1f34ec702c08626d454b39",
                "version": "1.8.0",
                "versionCode": "20"
            },
            "MobileInfo": {
                "imei": "863389036925793",
                "loginType": "0",
                "mobileModel": "vivo+X7",
                "os": "5.1"
            },
            "TestAccount": {
                "mobile": "18616296324",
                "password": "123456",
                "userId": "77777009114"
            }
        }
    )
    with open(file=configPath, mode='w', encoding='utf-8') as fw:
        yaml.dump(data=d, stream=fw)

# if __name__ == "__main__":
#     result = read_all()
#     #result1 = read_all("test_login_demo")
#     print(type(result),result)
#     #print(type(result1), result1)
