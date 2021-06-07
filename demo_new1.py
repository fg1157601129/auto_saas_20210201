from time import sleep
from threading import Thread
import psutil
from selenium import webdriver
import time

global a
a = True
def async1(f):
    def wrapper(*args,**kwargs):
        thr = Thread(target=f,args=args,kwargs=kwargs)
        thr.start()
    return wrapper

@async1
def A():

    for i in range(100):
        print(time.time(),"AAAAAA")
    a = False
@async1
def B():
    while a:
        print(time.time(),"BBBBBB")
A()
B()


