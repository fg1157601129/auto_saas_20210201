# -*- coding: utf-8 -*-

# @File    : HttpRequests.py
# @Date    : 2019-05-14-18:10
# @Author  : FangGang
# @Version : 1
import requests
import logging


class HttpRequests:
    """封装get和post请求"""

    def send_r(self, method, u, d, h):
        """
        接口访问方式和数据
        :param method: post/get
        :param u: url
        :param d: body中的data
        :param h: headers中的多个公用参数
        :return result:未经处理的接口返回数据
        """
        result = None
        if method == 'post':
            result = self.send_p(u, d, h)
            logging.info('接口返回数据：%s' % result.text)
        elif method == 'get':
            result = self.send_g(u, d, h)
            logging.info('接口返回数据：%s' % result.text)
        else:
            logging.error('错误！！！')
        return result

    @staticmethod
    def send_p(u, d, h):
        """
        post请求
        :param u: url
        :param d: body中的data
        :param h: headers中的多个公用参数
        :return res: 未经处理的接口返回数据
        """
        if d is None:
            res = requests.post(url=u, headers=h)
            logging.info('post：%s' % u)
            logging.info('从请求到接口返回信息耗时：%s秒' % res.elapsed.total_seconds())
        else:
            res = requests.post(url=u, data=d, headers=h)
            logging.info('post：%s' % u)
            logging.info('body数据：%s' % d)
            logging.info('从请求到接口返回信息耗时：%s秒' % res.elapsed.total_seconds())
        return res

    @staticmethod
    def send_g(u, d, h):
        """
        get请求
        :param u: url
        :param d: body中的data
        :param h: headers中的多个公用参数
        :return res: 未经处理的接口返回数据
        """
        if d is None:
            res = requests.get(u, headers=h)
            logging.info('get：%s' % u)
            logging.info('从请求到接口返回信息耗时：%s秒' % res.elapsed.total_seconds())
        else:
            res = requests.get(u, data=d, headers=h)
            logging.info('get：%s' % u)
            logging.info('body数据：%s' % d)
            logging.info('从请求到接口返回信息耗时：%s秒' % res.elapsed.total_seconds())
        return res

    @staticmethod
    def send_json(method, u, d, j, h):
        if method == 'post':
            logging.info('post：%s' % u)
            logging.info('body数据：%s' % d)
            logging.info('json数据：%s' % j)
            res = requests.post(url=u, data=d, json=j, headers=h)
            logging.info('接口返回数据：%s' % res.text)
            logging.info('从请求到接口返回信息耗时：%s秒' % res.elapsed.total_seconds())
            return res
        elif method == 'get':
            logging.info('get：%s' % u)
            logging.info('body数据：%s' % d)
            logging.info('json数据：%s' % j)
            res = requests.get(url=u, data=d, json=j, headers=h)
            logging.info('接口返回数据：%s' % res.text)
            logging.info('从请求到接口返回信息耗时：%s秒' % res.elapsed.total_seconds())
            return res

    def send_delete(self, u, d, j, h):
        res = requests.delete(url=u, data=d, json=j, headers=h)
        logging.info('delete: %s,\n 从请求到接口返回信息耗时:%s秒' % (u, res.elapsed.total_seconds()))
        logging.info(res.text)
        return res
