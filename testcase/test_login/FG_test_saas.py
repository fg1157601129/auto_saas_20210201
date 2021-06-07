from selenium import webdriver
import unittest
import time
import HTMLReport
from public.HttpRequests import HttpRequests
import logging

class MyTest(unittest.TestCase):
    def setUp(self):
        logging.info("test")
        self.driver_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        self.driver = webdriver.Chrome(self.driver_path)
        self.base_url = "https://power.medcloud.cn/login"
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        time.sleep(3)

    # def test_baidu(self):
    #     driver = self.driver
    #     driver.get(self.base_url + "/")
    #     driver.find_element_by_id("kw").clear()
    #     driver.find_element_by_id("kw").send_keys("unittest")
    #     driver.find_element_by_id("su").click()
    #     time.sleep(3)
    #     title = driver.title
    #     print("--------------------",title)
    #     self.assertEqual(title, "unittest_百度搜索")

    # def test_saas_login(self):
    #     driver = webdriver.Chrome(self.driver_path)
    #     driver.maximize_window()
    #     driver.implicitly_wait(5)
    #     # self.base_url = "http://www.baidu.com"
    #     base_url = "https://power.medcloud.cn/login"
    #     drive = driver
    #     drive.get(base_url)
    #     title = drive.title
    #     self.assertEqual(title,"北吉熊关系医疗赋能平台")
    #     raise

    def test_rejected(self):
        logging.info('测试用例标题：双12活动打开1个宝箱')
        base_url1 = 'https://pre.17kuxiu.com/user/getAnchorCoverAuditInfo'
        #base_url1 = "www.baidu.com"
        r =  HttpRequests().send_r('post', base_url1, None, None).json()
        # print("。。。。。。。。。。。。。。。。",r)
        # print("-------------------",r["retCode"])
        try:
            self.assertTrue(r['retCode'] == 200)
            self.assertTrue(r['data']['status'] == 2)
        except AssertionError as e:
            logging.error('失败：%s' % e)
            raise
    def tearDown(self):
        self.driver.quit()

# if __name__ == '__main__':
#     unittest.main()