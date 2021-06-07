# -*- coding: utf-8 -*-
# @File    : Tool.py
# @Date    : 2019-03-25-18:01
# @Author  : FangGang
# @Version  : 1
import hashlib
import math
import random
import time
import uuid
from datetime import datetime
from io import BytesIO

import requests
from PIL import Image

# from config import *
from public.ProjectPath import ProjectPath


class Tool:
    """工具类"""

    def __init__(self):
        self.loginType = read_mobile_info()["loginType"]  # 登录端类型:0-安卓，1-IOS,2-web,3-inhouse
        self.mobileModel = read_mobile_info()["mobileModel"]  # 手机型号 h5指定为:web
        self.os = read_mobile_info()["os"]  # 操作系统(h5指定为:web)
        self.imei = read_mobile_info()["imei"]
        self.version = read_app_info()["version"]  # 版本号,不强更时做接口兼容用
        self.secretkey = read_app_info()["secretkey"]  # secretkey由服务端指定,固定值
        self.versionCode = read_app_info()["versionCode"]  # 游戏版本号
        self.userId = read_test_account()["userId"]  # 登录状态的用户ID
        self.password = self.md5(read_test_account()["password"])
        self.mobile = read_test_account()["mobile"]
        self.accessToken = read_token()["token1"]  # 登录状态的token
        self.timestamp = self.get_timestamp()  # 时间戳，毫秒级

    def requestId(self):
        """
        生成requestId,常规用
        :return: requestId
        """
        bri = ('%s%s%s%s%s' % (
            self.os, self.imei, self.userId, self.timestamp, self.secretkey))
        ri = self.md5(bri)
        return ri

    def requestId_login(self):
        """
        生成requestId,手机号登录时用
        :return: requestId
        """
        bril = ('%s%s%s%s' % (
            self.os, self.imei, self.timestamp, self.secretkey))
        ril = self.md5(bril)
        return ril

    def requestId_with_uId(self, userId):
        """拼接指定了userId的requestId，
        :param userId: 用户的uiserId
        :return:md5后requestId
        """
        s = ('%s%s%s%s%s' % (
            self.os, self.imei, userId, self.timestamp, self.secretkey))
        return self.md5(s)

    def md5(self, md5str=None):
        """
        :param md5str:需要加密的字符串
        :return: md5后的字符串（大写）
        """
        hl = hashlib.md5()  # 创建md5对象
        hl.update(md5str.encode(encoding='utf-8'))  # 生成加密字符串
        return hl.hexdigest().upper()

    def sgin(self):
        """
        常规签名，目前接口未校验该参数，可以不带
        签名拼接规则：sign=MD5(timestamp+para_string+timestamp+secretkey)
        :return:接口需要的sign参数
        """
        para_string = 'channel:1 password:%s mobile:%s' % (self.password, self.mobile)
        before_sign = self.timestamp + para_string + self.timestamp + self.secretkey
        sign = self.md5(before_sign)
        return sign

    def headers(self):
        """
        接口请求时，公共参数放在header里，如下
        loginType:登录来源:0-安卓,1-IOS,2-web
        mobileModel:手机型号
        os:系统版本,例如5.1.1
        imei:imei号,每个SIM卡插槽对应一个
        timestamp:时间戳
        version:客户端版本号
        requestId:由os + imei + userId + timestamp + secretkey拼接而成（手机号登录时没有userId）
        accessToken:登录状态的token,有效期7天,服务器下发
        :return: 接口需要的header参数
        """
        h = {"accessToken": self.accessToken, "imei": self.imei, "loginType": self.loginType,
             "mobileModel": self.mobileModel,
             "os": self.os, "requestId": self.requestId(), "timestamp": self.timestamp, "version": self.version,
             "versionCode": self.versionCode}
        return h

    def headers_special(self, uid, token):
        h = {"accessToken": token, "imei": self.imei, "loginType": self.loginType,
             "mobileModel": self.mobileModel,
             "os": self.os, "requestId": self.requestId_with_uId(uid), "timestamp": self.timestamp,
             "version": self.version,
             "versionCode": self.versionCode}
        return h

    def headers_login(self):
        """
        拼接登录时用的headers
        :return: 接口需要的header参数
        """
        h = {"imei": self.imei, "loginType": self.loginType,
             "mobileModel": self.mobileModel,
             "os": self.os, "requestId": self.requestId_login(), "timestamp": self.timestamp,
             "version": self.version,
             "versionCode": self.versionCode}
        return h

    def headers_with_uid(self, userId):
        """
        拼接指定userid的headers
        :return: 接口需要的header参数
        """
        h = {"accessToken": self.accessToken, "imei": self.imei, "loginType": self.loginType,
             "mobileModel": self.mobileModel,
             "os": self.os, "requestId": self.requestId_with_uId(userId), "timestamp": self.timestamp,
             "version": self.version,
             "versionCode": self.versionCode}
        return h

    def headers_login_by_token(self):
        """
        Token登录时的headers
        :return: headers
        """
        h = {"loginType": self.loginType, "mobileModel": self.mobileModel, "os": self.os, "imei": self.imei,
             "timestamp": self.timestamp,
             "version": self.version, 'requestId': self.requestId(),
             'accessToken': self.accessToken}
        return h

    @staticmethod
    def write_to_file(file_name, mode, file_content):
        """将内容写入指定的文件中，在report目录下
        :param file_name: 文件名带后缀
        :param mode: 写入模式
        :param file_content: 文件内容，一般是从接口获得的数据
        :return:True写入成功，False写入失败
        """
        if file_name is None or file_content is None:
            print("请确定指定了文件名称，并且有内容可以写入")
            return False
        else:
            try:
                os.chdir(ProjectPath().cf_path())
                cursor = open(file_name, mode=mode, encoding='utf-8')
                cursor.write(file_content)
                cursor.write('\n')
                cursor.close()
                return True
            except IOError:
                print(IOError)
                return False

    @property
    def get_uuid(self):
        """获取uuid，一般应用在送礼物时，客户端校验是否是礼物连送
        :return:uuid小写
        """
        s_uuid = str(uuid.uuid1())
        l_uuid = s_uuid.replace('-', '')  # 去掉uuid的-
        return l_uuid

    @property
    def get_uuid_upper(self):
        """获取uuid，一般应用在送礼物时，客户端校验是否是礼物连送，苹果端使用全大写
        :return:uuid大写
        """
        s_uuid = str(uuid.uuid1())
        l_uuid = s_uuid.replace('-', '')  # 去掉uuid的-
        return l_uuid.upper()

    @staticmethod
    def get_timestamp():
        """
        13位unix时间戳
        :return:
        """
        timestamp = '%d' % int(round(time.time() * 1000))
        return timestamp

    @property
    def get_weekday(self):
        today = datetime.now().weekday()
        return today

    @property
    def get_random_gps(self):
        """以公司所在经纬度为圆心，100公里为半径，随机产生一个经纬度"""
        radius_in_degrees = 100000 / 111300  # 半径100公里
        u = float(random.uniform(0.0, 1.0))
        v = float(random.uniform(0.0, 1.0))
        w = radius_in_degrees * math.sqrt(u)
        t = 2 * math.pi * v
        x = w * math.cos(t)
        y = w * math.sin(t)
        longitude = y + 121.516203  # 公司附近经度
        latitude = x + 31.069320  # 公司附近维度
        # 这里是想保留6位小数点
        log = '%.6f' % longitude
        lat = '%.6f' % latitude
        return log, lat

    def get_remote_pic_size(self, path):
        """
        获取图片大小
        :param path:图片url
        :return:图片大小image.size，size[0]：宽度，size[1]：长度
        """
        response = requests.get(path)
        image = Image.open(BytesIO(response.content), 'r')
        return image.size

    @staticmethod
    def have_duplicates(n_list):
        """
        判定列表中没有重复项目
        :param n_list: 列表
        :return: True/False
        """
        if len(n_list) != len(set(n_list)):
            return True  # 有重复项目
        else:
            return False  # 没有重复项目

#
# if __name__ == "__main__":
#     # Tool().__init__()
