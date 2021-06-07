from time import sleep
from threading import Thread
import psutil
from selenium import webdriver
import time


def async1(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper

class demo_de():
    def __init__(self):
       self.a = True

    @async1
    def A(slef):    # UI自动化执行函数
        print(time.time(), "\nfun:AAAAAAAAAAAAAAAAAA\n")
        slef.a = False

    @async1
    def B(self):   # 假设这个是持续检测cpu、内存函数
        while self.a:
            print(time.time(), "\nfun:BBBBBBBBBBBBBBBBBB\n")

if __name__ == "__main__":
    demo_de().A()
    demo_de().B()

    # cpu_percent = psutil.cpu_percent(interval=1)
    # cpu_info = "CPU使用率：%i%%" % cpu_percent
    # print(cpu_info)
    # return cpu_percent



    # driver_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    # driver = webdriver.Chrome(driver_path)
    # driver.maximize_window()




# from threading import Thread
# import psutil
# import numpy as np
# import matplotlib.pyplot as plt
# from selenium import webdriver
# import unittest
# import time
# import HTMLReport
# from public.HttpRequests import HttpRequests
# import logging
# # from airtest.core.api import *
# import win32api,win32con
# from PIL import ImageGrab
# import pyautogui
# from selenium.webdriver.support.select import Select
# from threading import Timer
# import schedule
# import datetime
#
# cpu_percent_list = []
#
# # 异步执行函数 装饰器
# def async_decorator(f):
#     def wrapper(*args,**kwargs):
#         thr = Thread(target=f,args = args,kwargs=kwargs)
#         thr.start()
#     return wrapper
#
# @async_decorator
# def get_cpu_info():
#     while True:
#         cpu_percent = psutil.cpu_percent(interval=1,percpu=False)   # interval指定的是计算cpu使用率的时间间隔，percpu则指定是选择总的使用率还是每个cpu的使用率
#         cpu_info = "CPU使用率：%i%%" % cpu_percent
#         print(cpu_info)
#
#         virtual_memory = psutil.virtual_memory()
#         used_memory = virtual_memory.used / 1024 / 1024 / 1024
#         free_memory = virtual_memory.free / 1024 / 1024 / 1024
#         memory_percent = virtual_memory.percent
#         memory_info = "内存使用：%0.2fG，使用率%0.1f%%，剩余内存：%0.2fG\n" % (used_memory, memory_percent, free_memory)
#         print(memory_info)
#         #return used_memory
#
#         return cpu_percent
#
#         #time_y = time.time()
#         # plt.plot(cpu_percent,time_y)
#         # plt.show()
# def get_memory_info():
#     virtual_memory = psutil.virtual_memory()
#     used_memory = virtual_memory.used/1024/1024/1024
#     free_memory = virtual_memory.free/1024/1024/1024
#     memory_percent = virtual_memory.percent
#     memory_info = "内存使用：%0.2fG，使用率%0.1f%%，剩余内存：%0.2fG\n" % (used_memory, memory_percent, free_memory)
#     print(memory_info)
#     return used_memory

# get_cpu_info()