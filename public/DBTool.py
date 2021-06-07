# -*- coding: utf-8 -*-

# @File    : DBTool.py
# @Date    : 2019-08-08-19:48
# @Author  : FangGang
# @Version : 1
import pymysql


class MysqlUtil():
    """
    数据库相关操作类
    连接数据库信息：默认连接酷秀的kuxiu_supplement数据
    查询某个字段对应的字符串：mysql_get_string
    查询一组数据：mysql_get_rows
    创建游标：mysql_execute
    关闭 mysql 连接：mysql_close
    """

    def __init__(self):
        self.connection = pymysql.connect(host='106.14.7.214', port=13306, user='readonly', password='readonly',
                                          database='kuxiu_supplement', connect_timeout=30)
        if not self.connection:
            self.connection = self.reConndb()

    # def mysql_execute(self, sql):
    #     """执行 sql 语句写入"""
    #     cur = self.connection.cursor()
    #     try:
    #         cur.execute(sql)
    #     except Exception as a:
    #         self.connection.rollback()  # sql 执行异常后回滚
    #         print("执行 SQL 语句出现异常：%s" % a)
    #     else:
    #         cur.close()
    #         self.connection.commit()  # sql 无异常时提交

    def mysql_get_rows(self, sql):
        """返回查询结果"""
        cur = self.connection.cursor()
        try:
            cur.execute(sql)
        except Exception as a:
            print("执行 SQL 语句出现异常：%s" % a)
        else:
            rows = cur.fetchall()
            cur.close()
            return rows

    def mysql_get_string(self, sql):
        """查询某个字段的对应值"""
        rows = self.mysql_get_rows(sql)
        if rows is not None:
            for row in rows:
                for i in row:
                    return i

    def mysql_close(self):
        """关闭 close mysql"""
        try:
            self.connection.close()
        except Exception as a:
            print("数据库关闭时异常：%s" % a)

    def reConndb(self):
        # 数据库连接重试功能和连接超时功能的DB连接
        _conn_status = True
        _max_retries_count = 100  # 设置最大重试次数
        _conn_retries_count = 0  # 初始重试次数
        _conn_timeout = 3  # 连接超时时间为3秒
        while _conn_status and _conn_retries_count <= _max_retries_count:
            try:
                print('连接数据库中..')
                conn = pymysql.connect(host='', port=13306, user='', password='',
                                       database='', connect_timeout=_conn_timeout)
                _conn_status = False  # 如果conn成功则_status为设置为False则退出循环，返回db连接对象
                return conn
            except:
                _conn_retries_count += 1
                print(_conn_retries_count)
            print('connect db is error!!')
            continue



    # MySQLdb.connect() 建立数据库连接
    # cur = connection.cursor() #通过获取到的数据库连接 conn 下的 cursor()方法来创建游标。
    # cur.execute() #过游标 cur 操作 execute()方法可以写入纯 sql 语句。通过execute()方法中写如sql语句来对数据进行操作
    # cur.close() # cur.close() 关闭游标
    # connection.commit() # 在提交事物，在向数据库插入(或update)一条数据时必须要有这个方法，否则数据不会被真正的插入
    # connection.rollback() # 发生错误时候回滚
    # connection.close() # connection.close()关闭数据库连接

# if __name__ == "__main__":
#     s_sql = 'SELECT code FROM kuxiu_supplement.t_supplement_sms WHERE mobile_num = 8618616296326 ORDER BY create_time ' \
#             'DESC '
#     s = MysqlUtil().mysql_get_string(s_sql)
#     print(s)
#     MysqlUtil().mysql_close()
