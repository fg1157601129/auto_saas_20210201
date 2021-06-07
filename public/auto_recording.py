from selenium import webdriver
from threading import Thread
import pyautogui
import psutil
import time
from PIL import ImageGrab
from matplotlib import pyplot as plt
import unittest
import HTMLReport
from public.HttpRequests import HttpRequests
import logging

from selenium.webdriver.support.select import Select
from threading import Timer
import schedule
import datetime



"""
本脚本适用于，web页面自动化
【强制刷新】实现方案：
打开devtools后，强制访问url，并截图记录待测信息

【切换页面】实现方案：
切换到其他页面利用快捷键 F12 关闭devtools，重新打开devtools后，切换至待测页面，截图并记录待测信息

"""





driver_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
cpu_list = []
time_tag = []
#
# options = webdriver.ChromeOptions()
# options.add_argument("--auto-open-devtools-for-tabs")
# driver = webdriver.Chrome(driver_path,chrome_options=options)
driver = webdriver.Chrome(driver_path)
driver.maximize_window()
time.sleep(1)

def cpu_trend_chart(x,y,page):
    plt.title("Matplotlib demo")
    plt.xlabel("time")
    plt.ylabel("CPU")
    plt.plot(x, y)
    plt.savefig(fr"D:\auto_saas_20210201\public\image_0305\Home_page_{page}.png")



# 异步执行函数 装饰器
def async_decorator(f):
    def wrapper(*args,**kwargs):
        thr = Thread(target=f,args = args,kwargs=kwargs)
        thr.start()
    return wrapper

@async_decorator
def get_cpu_info():

    notice_tag = True

    while notice_tag:
        cpu_percent = psutil.cpu_percent(interval=1,percpu=False)   # interval指定的是计算cpu使用率的时间间隔，percpu则指定是选择总的使用率还是每个cpu的使用率
        cpu_info = f"CPU使用率：{cpu_percent}"
        print(cpu_info)     # 绘制图表
        # return cpu_percent
        cpu_list.append(cpu_percent)
        time_tag.append(time.strftime('%M:%S'))

        notice_tag = start_notice_tag
def get_memory_info():
    virtual_memory = psutil.virtual_memory()
    used_memory = virtual_memory.used/1024/1024/1024
    free_memory = virtual_memory.free/1024/1024/1024
    memory_percent = virtual_memory.percent
    memory_info = "内存使用：%0.2fG，使用率%0.1f%%，剩余内存：%0.2fG\n" % (used_memory, memory_percent, free_memory)
    print(memory_info)
    return used_memory

@async_decorator
def auto_ui():
    # global cpu_list
    # global time_tag
    global start_notice_tag
    start_notice_tag = True
    # cpu_list = []
    # time_tag = []
    pyautogui.press('f12')
    time.sleep(1)
    for i in range(3):
        pyautogui.hotkey("Ctrl", "]")
    pyautogui.hotkey("Ctrl","-")
    pyautogui.hotkey("Ctrl","-")

    # 登录到首页1
    base_url = "https://power.medcloud.cn/login"
    driver.get(base_url)

    mC = driver.find_element_by_id("memberCode")
    uN = driver.find_element_by_id("username")
    pD = driver.find_element_by_id("password")
    # mC = driver.find_element(by=id("memberCode"))
    # uN = driver.find_element(by=id("username"))
    # pD = driver.find_element(by=id("password"))


    mC.send_keys("李俊测试连锁机构")
    uN.send_keys("13167172396")
    pD.send_keys("123456")

    # 点击【切换机构】下拉框
    box_css_1 = driver.find_element_by_css_selector(".ant-select-selection-item .text__3rSDb")
    box_css_1.click()

    # 选中并点击【下拉框】中的某个机构
    box_css_2 = driver.find_element_by_css_selector(".ant-select-tree-treenode:nth-child(4) .text__3rSDb")
    box_css_2.click()

    # 点击登录按钮
    login_button = driver.find_element_by_css_selector(".btnDental__gSn_P")
    login_button.click()

    time.sleep(10)

    # 强制刷新
    pyautogui.press('f5')
    # 强制等待页面加载完成，截图记录network信息，并保存截图
    time.sleep(10)
    ImageGrab.grab().save(r'D:\auto_saas_20210201\public\image_0305\Home_page_1.png')
    #im_1.save(r'D:\auto_saas_20210201\public\image_0305\Home_page_1.png')

    cpu_trend_chart(time_tag,cpu_list,3)

    cpu_list.clear()
    time_tag.clear()

    # 切换到【医疗业务】页面 再 切换至 【首页】。截图记录network信息，并保存截图
    medical_business = driver.find_element_by_xpath('//*[@id="main-app"]/section/header/div/div[1]/div[2]/div[2]/p')
    medical_business.click()
    time.sleep(5)
    # 利用快捷键 F12
    pyautogui.press('f12')
    time.sleep(5)
    pyautogui.press('f12')
    time.sleep(5)
    # 从【医疗业务】页面  切换至 【首页】。截图记录network信息，并保存截图
    home_page = driver.find_element_by_xpath('//*[@id="main-app"]/section/header/div/div[1]/div[2]/div[1]/p')
    home_page.click()
    # 切换页面等待加载完成，截图记录network信息，并保存截图
    time.sleep(10)
    ImageGrab.grab().save(r'D:\auto_saas_20210201\public\image_0305\Home_page_2.png')

    cpu_trend_chart(time_tag,cpu_list,4)
    # # 预约视图2
    # home_page_url = "https://power.medcloud.cn/dpms_dental/appointment/appointment-view"
    # driver.get(home_page_url)
    # time.sleep(5)
    # ImageGrab.grab().save(r'D:\auto_saas_20210201\public\image_0305\view_2.png')
    # # im_2 = ImageGrab.grab()
    # # im_2.save(r'D:\auto_saas_20210201\public\image_0305\view_2.png')


    start_notice_tag = False





# # 强制刷新后，延迟2s记录cpu内存信息
# time.sleep(2)
# print("【首页】强制刷新：After物理资源消耗：-------")
# after_cpu_1 = get_cpu_info()
# after_memory_1 = get_memory_info()
#
# # 强制等待页面加载完成，截图记录network信息，并保存截图
# time.sleep(7)
# #data_bbox=(0,0,1920,1080)
# # pyautogui.size()  # 获取屏幕分辨率
# im_1 = ImageGrab.grab()
# im_1.save(r'D:\auto_saas_20210201\public\image_0305\Home_page_1.png')
# # im_1 = pyautogui.screenshot('my_screenshot.png')
#
# # 切换页面记录相关信息
# # 预约视图2
# time.sleep(6)
# print("【预约中心】：Before物理资源消耗：-------")
# befor_cpu_2 = get_cpu_info()
# befor_memory_2 = get_memory_info()
#
# home_page_url = "https://power.medcloud.cn/dpms_dental/appointment/appointment-view"
# driver.get(home_page_url)
# time.sleep(2)
# win32api.keybd_event(116, 0, 0, 0)
# win32api.keybd_event(116,0,win32con.KEYEVENTF_KEYUP,0)
# time.sleep(5)
# print("【预约中心】：After物理资源消耗：-------")
# after_cpu_2 = get_cpu_info()
# after_memory_2 = get_memory_info()
#
# time.sleep(8)
# im_2 = ImageGrab.grab()
# im_2.save(r'D:\auto_saas_20210201\public\image_0305\view_2.png')
#
# # 医疗业务3
# time.sleep(6)
# print("【医疗业务】：Before物理资源消耗：-------")
# befor_cpu_3 = get_cpu_info()
# befor_memory_3 = get_memory_info()
#
# business_url = "https://power.medcloud.cn/dpms_dental/patient-center/patient-manage/patient-list"
# driver.get(business_url)
# time.sleep(2)
# win32api.keybd_event(116, 0, 0, 0)
# win32api.keybd_event(116,0,win32con.KEYEVENTF_KEYUP,0)
# time.sleep(3)
# print("【医疗业务】：After物理资源消耗：-------")
# after_cpu_3 = get_cpu_info()
# after_memory_3 = get_memory_info()
# time.sleep(10)
#
# time.sleep(3)
# im_3 = ImageGrab.grab()
# im_3.save(r'D:\auto_saas_20210201\public\image_0305\business_3.png')
#
# #  病历管理     //*[@id="main-app"]/section/section/aside/div/ul/li[2]/a
# #  患者管理 → 所有患者   //*[@id="main-app"]/section/section/aside/div/ul/li[1]/ul/li[1]
# time.sleep(2)
# print("【病历管理】：Before物理资源消耗：-------")
#
# # 利用快捷键 ctrl + shift + i
# win32api.keybd_event(17, 0, 0, 0)
# win32api.keybd_event(16, 0, 0, 0)
# win32api.keybd_event(73, 0, 0, 0)  # I
#
# # Record_management = driver.find_element_by_xpath('//*[@id="main-app"]/section/section/aside/div/ul/li[2]/a')
# Patient_management = driver.find_element_by_xpath('//*[@id="main-app"]/section/section/aside/div/ul/li[1]/ul/li[1]')
# Patient_archive = driver.find_element_by_xpath('//*[@id="main-app"]/section/section/aside/div/ul/li[1]/ul/li[2]')
# #Record_management.click()
# Patient_archive.click()
# print("切换至【归档患者】之前 Before物理资源消耗：-------",)
# time.sleep(8)
#
# switch_before_cpu_1 = get_cpu_info()
# switch_before_memory_1 = get_memory_info()
#
# time.sleep(2)
# # 利用快捷键 ctrl + shift + i
# win32api.keybd_event(17, 0, 0, 0)
# win32api.keybd_event(16, 0, 0, 0)
# win32api.keybd_event(73, 0, 0, 0)  # I
#
# time.sleep(2)
#
# Patient_management.click()
#
# time.sleep(2)
# switch_after_cpu_1 = get_cpu_info()
# switch_after_memory_1 = get_memory_info()
# time.sleep(2)
# im_switch_1 = ImageGrab.grab()
# im_switch_1.save(r'D:\auto_saas_20210201\public\image_0305\im_switch_1.png')


# # 患者个人信息4
# time.sleep(6)
# print("【医疗业务_个人信息】：Before物理资源消耗：-------")
# befor_cpu_4 = get_cpu_info()
# befor_memory_4 = get_memory_info()
# business_personal_url = "https://power.medcloud.cn/dpms_dental/patient-center/patient-manage/patient-list/patient-detail/detailed-infos?patientId=248416"
# driver.get(business_personal_url)
# time.sleep(3)
# # 刷新
# win32api.keybd_event(116, 0, 0, 0)
# win32api.keybd_event(116,0,win32con.KEYEVENTF_KEYUP,0)
# time.sleep(4)
# print("【医疗业务_个人信息】：After物理资源消耗：-------")
# after_cpu_4 = get_cpu_info()
# after_memory_4 = get_memory_info()
# time.sleep(11)
# im_4 = ImageGrab.grab()
# im_4.save(r'D:\auto_saas_20210201\public\image_0305\business_personal_4.png')
#
#
# # 患者收费5
# time.sleep(6)
# print("【医疗业务_收费】：Before物理资源消耗：-------")
# befor_cpu_5 = get_cpu_info()
# befor_memory_5 = get_memory_info()
# charge_url = "https://power.medcloud.cn/dpms_dental/patient-center/patient-manage/patient-list/patient-detail/billing-tab?patientId=260256"
# driver.get(charge_url)
# time.sleep(2)
# win32api.keybd_event(116, 0, 0, 0)
# win32api.keybd_event(116,0,win32con.KEYEVENTF_KEYUP,0)
# time.sleep(4)
# print("【医疗业务_收费】：After物理资源消耗：-------")
# after_cpu_5 = get_cpu_info()
# after_memory_5 = get_memory_info()
# time.sleep(13)
# im_5 = ImageGrab.grab()
# im_5.save(r'D:\auto_saas_20210201\public\image_0305\charge_5.png')
#
#
# # 病历管理6
# time.sleep(6)
# print("【病历管理】：Before物理资源消耗：-------")
# befor_cpu_6 = get_cpu_info()
# befor_memory_6 = get_memory_info()
# medical_records_url = "https://power.medcloud.cn/dpms_dental/patient-center/medical-records-management"
# driver.get(medical_records_url)
# time.sleep(2)
# win32api.keybd_event(116, 0, 0, 0)
# win32api.keybd_event(116,0,win32con.KEYEVENTF_KEYUP,0)
# time.sleep(4)
# print("【病历管理】：After物理资源消耗：-------")
# after_cpu_6 = get_cpu_info()
# after_memory_6 = get_memory_info()
# time.sleep(6)
# im_6 = ImageGrab.grab()
# im_6.save(r'D:\auto_saas_20210201\public\image_0305\medical_records_6.png')
#
#
# result_cpu_1 = after_cpu_1 - befor_cpu_1
# result_memory_1 = after_memory_1 - befor_memory_1
# print("【首页】：物理资源消耗：-------CPU:",result_cpu_1)
# print("【首页】：物理资源消耗：-------内存:",result_memory_1)
#
# result_cpu_2 = after_cpu_2 - befor_cpu_2
# result_memory_2 = after_memory_2 - befor_memory_2
# print("【预约中心】：物理资源消耗：-------CPU:",result_cpu_2)
# print("【预约中心】：物理资源消耗：-------内存:",result_memory_2)
#
# result_cpu_3 = after_cpu_3 - befor_cpu_3
# result_memory_3 = after_memory_3 - befor_memory_3
# print("【医疗业务】：物理资源消耗：-------CPU:",result_cpu_3)
# print("【医疗业务】：物理资源消耗：-------内存:",result_memory_3)
#
# result_cpu_4 = after_cpu_4 - befor_cpu_4
# result_memory_4 = after_memory_4 - befor_memory_4
# print("【医疗业务_个人信息】：物理资源消耗：-------CPU:",result_cpu_4)
# print("【医疗业务_个人信息】：物理资源消耗：-------内存:",result_memory_4)
#
#
# result_cpu_5 = after_cpu_5 - befor_cpu_5
# result_memory_5 = after_memory_5 - befor_memory_5
# print("【医疗业务_收费】：物理资源消耗：-------CPU:",result_cpu_5)
# print("【医疗业务_收费】：物理资源消耗：-------内存:",result_memory_5)
#
# result_cpu_6 = after_cpu_6 - befor_cpu_6
# result_memory_6 = after_memory_6 - befor_memory_6
# print("【病历管理】：物理资源消耗：-------CPU:",result_cpu_6)
# print("【病历管理】：物理资源消耗：-------内存:",result_memory_6)
#
# win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
# win32api.keybd_event(16,0,win32con.KEYEVENTF_KEYUP,0)
#
#





# try:
#     result_png = driver.get_screenshot_as_file(r"D:\auto_saas_20210201\public\1.png")
# except IOError as e:
#     print(e)



auto_ui()
get_cpu_info()