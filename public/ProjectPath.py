# -*- coding: utf-8 -*-
# @File    : ProjectPath.py
# @Date    : 2019-05-07-19:26
# @Author  : FangGang
# @Version : 1
import os


class ProjectPath:
    """项目路径"""

    def __init__(self):
        self.basedir = os.path.abspath(
            os.path.dirname(os.path.dirname(__file__)))
        self.case_path = self.get_path('testcase')  # 测试用例路径
        self.case_file_path = self.get_path('testcasefile')  # 测试文件路径
        self.report_path = self.get_path('report')  # 测试报告路径
        self.config_path = self.get_path('config.yaml')  # 配置文件路径

    def get_path(self, path=None):
        """
        文件所在的路径
        :param path:
        :return: 文件所在路径
        """
        if path is None:
            return self.basedir
        else:
            return os.path.join(self.basedir, path)

    def cf_path(self, path=None):
        if path is None:
            return self.case_file_path
        else:
            return os.path.join(self.case_file_path, path)

    @staticmethod
    def get_join_path(path1=None, path2=None, path3=None):
        if path3 is None:
            return os.path.join(path1, path2)
        else:
            return os.path.join(os.path.join(path1, path2), path3)


# if __name__ == '__main__':
#     print(ProjectPath().basedir)
