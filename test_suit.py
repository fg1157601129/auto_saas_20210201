# -*- coding: utf-8 -*-
# @File    : test_suit.py
# @Date    : 2019-04-24-20:26
# @Author  : FangGang
import unittest
import HTMLReport
from public.ProjectPath import ProjectPath
from public.PhoneLogin import PhoneLogin
import time
import datetime

# PhoneLogin().do_login()

# test_file_list = []

if __name__ == '__main__':
    case_path = ProjectPath().get_path('testcase')
    rep_path = ProjectPath().report_path
    # suite = unittest.TestSuite()  # 实例化测试套件
    # loader = unittest.TestLoader()  # 实例化测试用例加载器
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern='test*.py',  # 运行Test_case文件夹下所有以test开头的python文件
                                                   top_level_dir=None)  # 测试模块的顶层目录，如果没有顶层目录，默认为None
    # 测试用例执行器
    runner = HTMLReport.TestRunner(report_file_name='zeyi_Interface_' + datetime.datetime.now().strftime("%Y%m%d%H%M"),
                                   output_path=rep_path,
                                   title='泽怡接口测试报告',
                                   description='自动化接口测试',
                                   thread_count=2,
                                   thread_start_wait=1,
                                   sequential_execution=True,
                                   lang='cn')
    runner.run(discover)  # run()方法是运行测试套件的测试用例，入参为suite测试套件
