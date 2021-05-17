#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# -------------------------------
# Author: SuphxLin
# CreateTime: 2021/04/25 13:21
# FileName: login_wechat_official_account
# Description: 
# Question:

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json


def login():
    # 调用谷歌浏览器驱动
    options = Options()
    options.binary_location = "../../chrome/chrome.exe"
    driver = webdriver.Chrome(chrome_options=options, executable_path="../../chrome/chromedriver.exe")
    driver.get("https://mp.weixin.qq.com/")  # 微信公众平台网址
    driver.find_element_by_link_text("使用帐号登录").click()  # 此行代码为2020.10.10新增，因为微信公众号页码原来默认直接为登录框， 现在默认为二维码，此行代码可以将二维码切换到登录框页面
    driver.find_element_by_name("account").clear()
    driver.find_element_by_name("account").send_keys("3097828351@qq.com")  # 自己的微信公众号
    time.sleep(2)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys("2017ljx20080816")  # 自己的微信公众号密码
    driver.find_element_by_class_name("icon_checkbox").click()

    time.sleep(2)
    driver.find_element_by_class_name("btn_login").click()
    time.sleep(5)
    is_login = input("Login Successfully ?(Y/n)")
    while is_login.lower() != "y" and is_login.lower() != "yes":
        is_login = input("Login Successfully ?(Y/n)")
    # 此时会弹出扫码页面，需要微信扫码
    cookies = driver.get_cookies()  # 获取登录后的cookies
    print(cookies)
    cookie = {}
    for items in cookies:
        cookie[items.get("name")] = items.get("value")
    # 将cookies写入到本地文件，供以后程序访问公众号时携带作为身份识别用
    with open('../../cookies.txt', "w") as file:
        #  写入转成字符串的字典
        file.write(json.dumps(cookie))


if __name__ == '__main__':
    login()