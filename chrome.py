# -*- coding:utf-8 -*-

from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
time.sleep(2)
browser.find_element_by_link_text("登录").click()
browser.find_element_by_name("userName").clear()
browser.find_element_by_name("userName").send_keys("Elena_Gao")
browser.find_element_by_id("TANGRAM__PSP_8__password").clear()
browser.find_element_by_id("TANGRAM__PSP_8__password").send_keys("huimin99")
time.sleep(2)
browser.quit()
