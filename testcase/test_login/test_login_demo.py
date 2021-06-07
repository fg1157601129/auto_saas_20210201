from time import sleep
from selenium import webdriver
import unittest
from parameterized import parameterized
import logging
# from HTMLReport import ddt,retry,TestRunner,addImage,no_retry
import ddt
from public.config import read_all


parameter_data = read_all("test_login_demo")

@ddt.ddt()
class LoginDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        cls.driver = webdriver.Chrome(cls.driver_path)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def login(self, username, password):
        self.driver.get("http://mail.163.com")
        # self.driver.find_element_by_link_text("密码登录").click()
        login_frame = self.driver.find_element_by_css_selector('iframe[id^="x-URS-iframe"]')
        self.driver.switch_to.frame(login_frame)
        self.driver.find_element_by_class_name('j-inputtext.dlemail.j-nameforslide').clear()
        self.driver.find_element_by_class_name('j-inputtext.dlemail.j-nameforslide').send_keys(username)
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_id('dologin').click()
        sleep(4)

    def logout(self):
        self.driver.find_element_by_link_text("退出").click()

    #parameterized 数据驱动方法
    # @parameterized.expand([
    #     ("case1", "xyuer1019", "123456"),
    #     ("case2", "", "123456"),
    #     ("case3", "xyuer", ""),
    #     ("case4", "error", "error"),
    # ])


# from parameterized import parameterized   # 引入parameterized模块
# import pandas as pa
# import requests
# list = pa.read_excel('E:\桌面\参数化.xls',)
# a=list.iloc[:,4:6].values
# b = a.tolist()
#
#
# class testsearch(unittest.TestCase):
#
#
#     @parameterized.expand(b)
#     def test01(self, a1, b1):
#         url = 'http://127.0.0.1:8000/api/get_event_list/'
#         a1 = eval(a1)  # 注意将字符串转化成字典在进行请求
#         r = requests.get(url, params= a1)
#         self.result = r.json()
#         print(self.result['status'])
#         self.assertEqual(self.result['status'], b1)
#
#
# if __name__ == '__main__':
#     unittest.main()



    # ddt非外部文件数据驱动方法
    # @ddt.data(("case1", "xyuer1019", "123456"),
    #           ("case2", "", "123456"),
    #           ("case3", "xyuer", ""),
    #           ("case4", "error", "error"),)




    #@ddt.file_data(r"D:\auto_saas_20210201\testcasefile\testcaseconfig.yaml")
    #@ddt.ddt(*parameter_data)
    #@ddt.unpack

    @ddt.file_data(r"D:\auto_saas_20210201\testcasefile\testcaseconfig.yaml")
    @ddt.unpack

    # 失败重试
    # 测试方法前加入装饰器 @ retry @ no_retry，用于重试与不重试
    def test_login(self, case, username, password):
        self.login(username, password)
        self.logout()
    # def test_login(self):
    #     self.login(case_data["username"],case_data["password"] )
    #     self.logout()

    @classmethod
    def tearDownClass(cls):
    #   cls.driver.quit()
        LoginDemo().driver.quit()



if __name__ == '__main__':
    unittest.main(verbosity=2)






