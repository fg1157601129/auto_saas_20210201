# -*- coding: utf-8 -*-
# @File    : ReadExcel.py
# @Date    : 2019-05-13-17:28
# @Author  : FangGang
# @Version : 1

import xlrd


class ReadExcel(object):
    def __init__(self, path):
        self.path = path
        # self.pat1 = r'?'

    @property
    def get_sheet(self):
        """
        :return:获取索引值，从0开始，这里我们只有1个sheet
        """
        xl = xlrd.open_workbook(self.path)
        sheet = xl.sheet_by_index(0)
        return sheet

    @property
    def get_rows(self):
        """
        :return: 行数
        """
        rows = self.get_sheet.nrows
        return rows

    @property
    def get_col(self):
        """
        :return: 列数
        """
        cols = self.get_sheet.ncols
        return cols

    @property
    def get_case_num(self):
        """
        :return: 测试用例编号列表
        """
        case_num = []
        for i in range(1, self.get_rows):
            case_num.append(self.get_sheet.cell_value(i, 0))
        return case_num

    # 以下是分别获取每一列的数值
    @property
    def get_name(self):
        """
        :return: 接口名称列表
        """
        name = []
        for i in range(1, self.get_rows):
            name.append(self.get_sheet.cell_value(i, 1))
        return name

    @property
    def get_title(self):
        """
        :return: 用例标题列表
        """
        title = []
        for i in range(1, self.get_rows):
            title.append(self.get_sheet.cell_value(i, 2))
        return title

    @property
    def get_method(self):
        """
        :return: 请求类型列表
        """
        method = []
        for i in range(1, self.get_rows):
            method.append(self.get_sheet.cell_value(i, 3))
        return method

    @property
    def get_url(self):
        """
        :return: 接口地址列表
        """
        url = []
        for i in range(1, self.get_rows):
            s = self.get_sheet.cell_value(i, 4)
            url.append(s)
            # if re.search(self.pat1, str(s)):
            #     s += 'sign=%s' % Tool().sgin()
            #     print(s)
            #     url.append(s)
            # else:
            #     s += '?sign=%s' % Tool().sgin()
            #     print(s)
            #     url.append(s)
        return url

    @property
    def get_data(self):
        """
        :return: 接口body中的数据列表
        """
        data = []
        for i in range(1, self.get_rows):
            data.append(self.get_sheet.cell_value(i, 5))
        return data

    @property
    def get_expected(self):
        """
        :return: 期望结果列表
        """
        expected = []
        for i in range(1, self.get_rows):
            expected.append(self.get_sheet.cell_value(i, 6))
        return expected
