# -*- coding: utf-8 -*-

# @File    : MyLog.py
# @Date    : 2019-06-24-13:02
# @Author  : FangGang
# @Version : 1
import logging.handlers
import logging
from public.ProjectPath import ProjectPath
import os
import time

# 日志文件存放在report目录
log_path = ProjectPath().report_path
# 如果不存在report文件夹，就自动创建report文件夹
if not os.path.exists(log_path): os.mkdir(log_path)


class MyLog:
    logger = None

    def __init__(self):
        self.log_level = logging.DEBUG
        # 日志输出格式，形如20190813203714.log
        self.log_file = log_path + ('\\%s.log' % time.strftime('%Y%m%d%H%M%S'))
        self.log_max_byte = 10 * 1024 * 1024
        self.log_backup_count = 10

    def get_logger(self):
        if MyLog.logger is not None:
            return MyLog.logger

        MyLog.logger = logging.Logger("Logger")
        log_handler = logging.handlers.RotatingFileHandler(filename=self.log_file,
                                                           maxBytes=self.log_max_byte,
                                                           backupCount=self.log_backup_count,
                                                           encoding='utf-8')
        log_fmt = logging.Formatter("[%(levelname)s][%(funcName)s][%(asctime)s]%(message)s")
        log_handler.setFormatter(log_fmt)
        MyLog.logger.addHandler(log_handler)
        MyLog.logger.setLevel(self.log_level)

        # 创建一个StreamHandler,用于输出到控制台
        console = logging.StreamHandler()
        console.setLevel(self.log_level)
        console.setFormatter(log_fmt)
        self.logger.addHandler(console)

        return MyLog.logger


if __name__ == '__main__':
    MyLog().get_logging
