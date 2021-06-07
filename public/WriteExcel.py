# -*- coding: utf-8 -*-
# @File    : WriteExcel.py
# @Date    : 2019-08-31-13:39
# @Author  : FangGang
# @Version : 1
import xlwt

from public.ProjectPath import ProjectPath

# 日志文件存放在report目录
log_path = ProjectPath().report_path


class WriteExcel():

    def __init__(self):
        self.wbk = xlwt.Workbook()

    def write(self, data):
        '''
        :param data: array 表格数据
        :param out_path: string 输出路径
        '''
        sheet = self.wbk.add_sheet('Sheet1', cell_overwrite_ok=True)
        for i in range(len(data)):
            for j in range(len(data[i])):
                sheet.write(i, j, data[i][j])

    def write2(self, data):
        '''
        :param data: array 表格数据
        :param out_path: string 输出路径
        '''
        sheet = self.wbk.add_sheet('Sheet1', cell_overwrite_ok=True)
        for i in range(len(data)):
            sheet.write(i, 0, data[i])

    def save(self, file_name=None):
        if file_name:
            self.wbk.save(log_path + file_name)
        else:
            self.wbk.save(log_path + '\\1.xlsx')


if __name__ == '__main__':
    xls_util = WriteExcel()
    xls_util.write(
        [[0, 123], [18800, 123]]
    )
    xls_util.save()

# [1.0, '海底世界', '1.mp4', '1.png', 'animal:动物', '神秘的海底世界', '免费'],
# [2.0, '沙滩上的一天', '2.mp4', '2.png', 'brown:棕色的', '沙滩，阳光，贝壳。', '免费'],
# [3.0, '沙滩，我来了！', '3.mp4', '3.png', 'beach:海滩', '炎炎夏日', '会员'],
# [4.0, '在度假中', '4.mp4', '4.png', 'beach:海滩', '度假时间到了', '会员']
