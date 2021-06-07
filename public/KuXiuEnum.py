# -*- coding: utf-8 -*-
# @File    : KuXiuEnum.py
# @Date    : 2019-11-26 14:35
# @Author  : FangGang
# @Version : 1
from enum import Enum


class KuXiuEnum(Enum):
    URL_LIVE_ROOM = 'http://pre.17kuxiu.com/liveroom'  # 直播间模块地址
    URL_DYNAMIC = 'https://pre.17kuxiu.com/dynamic'  # 动态模块地址
    URL_SUPPLEMENT = 'https://pre.17kuxiu.com/supplement'  # 补充服务模块地址
    URL_USER = 'https://pre.17kuxiu.com/user'  # 用户服务模块地址
    URL_GIFT = 'https://pre.17kuxiu.com/gift'  # 礼物服务模块地址
    URL_PAYMENT = 'https://pre.17kuxiu.com/payment'  # 支付服务模块地址
    URL_GAME = 'https://pre.17kuxiu.com/game'

    MOBILE_BALANCE_NOT_ENOUGH = "18612345621"  # 余额不足的手机号
    PASSWORD_BALANCE_NOT_ENOUGH = "123456"  # 余额不足的手机号密码
    MOBILE_NOT_ANCHOR = "18612345621"  # 余非主播手机号
    PASSWORD_NOT_ANCHOR = "123456"  # 余非主播密码
    MOBILE_NO_ALBUM = "14782376206"  # 未上传相册用户手机号
    PASSWORD_NO_ALBUM = "111111"  # 未上传相册用户密码
    UID_NOT_ANCHOR = 77777000120  # 非主播身份的uid
    MOBILE_NOT_AUTH = "14782376210"  # 主播实名审核被驳回的手机号
    PASSWORD_NOT_AUTH = "111111"  # 主播实名审核被驳回的密码

    CODE_SUCCESS = 200  # 访问成功
    CODE_SYSTEM_ERROR = -500  # 系统错误
    CODE_PARAM_EXCEPTION = -100000  # 参数异常
    CODE_TOKEN_BE_OVERDUE = -100007  # Token过期
    CODE_NOT_GUARD = -200009  # 您尚未开通该主播的守护~
    CODE_NOT_IN_BACKPACK = -200021  # 您的背包礼物数量不足
    CODE_MOBILE_NOT_REGISTER = -300025  # 该手机号未注册
    CODE_PASSWORD_ERROR = -300026   # 密码输入错误
    CODE_PARAM_ERROR = -300046  # 参数错误
    CODE_IMG_NOT_EXIST = -300089  # 相片的ID不存在
    CODE_NOT_ANCHOR = -500021  # 当前主播不存在或者不是主播
    CODE_BALANCE_NOT_ENOUGH = -903005  # 错误码，余额不足

    # 预设的开播标题
    LIVE_SLOGAN = ('今天萌萌哒', '初次见面，请多关照', '梦想是万般宠爱', '谁能守护我呢', '活捉一只小可爱',
                   '遇见你是最美的幸运', '很久没见大哥了呢', '有人陪我么', '新主播求守护', '来认识一下嘛',
                   '我的歌声只为你歌唱', '嘿！来谈个恋爱吧', '愿余生有你相陪', '打包求带走', '我在这儿等你回来')

    # 敏感词举例
    SENSITIVE_WORD = ('惩贪难', '通钢总经', '达毕业证', '姓忽悠', '代办发票', '手机跟')

    # 12生肖礼物名称
    CHINESE_ZODIACS = "子鼠丑牛寅虎卯兔辰龙巳蛇午马未羊申猴酉鸡戌狗亥猪"
