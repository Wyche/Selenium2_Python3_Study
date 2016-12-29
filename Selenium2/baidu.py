# coding=utf-8
#python3.51 selenium2.53.6 firefox45
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")

driver.find_element_by_id("kw").send_keys("Selenium2")
driver.find_element_by_id("su").click()
driver.quit()
