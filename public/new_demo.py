from time import sleep
from threading import Thread
import psutil
from selenium import webdriver
import time
import bar_chart_race as bcr
import pandas as pd
# global a
"""
    已验证 正确可行方案
"""

def async1(f):
    def wrapper(*args,**kwargs):
        thr = Thread(target=f,args=args,kwargs=kwargs)
        thr.start()
    return wrapper

@async1
def A():
    global a
    a = True
    for i in range(100):
        print(time.time(),"AAAAAA")
    a = False
    for r in range(100):
        print(time.time(),"AAAAAA")
@async1
def B():
    b = True
    while b:
        print(time.time(),"BBBBBB")
        b = a
A()
B()

# df = pd.read_csv("cpudata.csv")
# bcr.bar_chart_race(df.set_index("date"),"covid19_horiz.gif")
# print(type(df),df)
