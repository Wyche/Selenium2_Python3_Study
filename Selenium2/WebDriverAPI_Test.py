'''
This file created for test webdriver API
'''
from selenium import webdriver
#for mouse event
from selenium.webdriver.common.action_chains import ActionChains
#for keyboard event
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import ctime
from time import sleep

driver = webdriver.Firefox()

#Browser Control
'''
driver.get("http://www.baidu.com")

print("Set browser")
#set browser size
#driver.set_window_size(480, 800)
driver.maximize_window()
'''

'''
first_url = "http://www.baidu.com"
print(first_url)
driver.get(first_url)

second_url = "http://news.baidu.com"
print(second_url)
driver.get(second_url)

print("back to %s" % first_url)
#back
driver.back()

print("forward to %s" % second_url)
#forward
driver.forward()

print("refresh browser")
#refresh
driver.refresh()
'''

#Simple elements operation
'''
driver.get("http://www.126.com")

#clear()
driver.find_element_by_id("idinput").clear()
#send_keys(*value)
driver.find_element_by_id("idinput").send_keys("username")
driver.find_element_by_id("pwdInput").clear()
driver.find_element_by_id("pwdInput").send_keys("password")
#click()
driver.find_element_by_id("loginBtn").click()
'''

'''
driver.get("http://www.youdao.com")

driver.find_element_by_css_selector("input#translateContent").send_keys("hello")
driver.find_element_by_css_selector("input#translateContent").submit()
'''

'''
driver.get("http://www.baidu.com")
size = driver.find_element_by_id('kw').size
print(size)

text = driver.find_element_by_id("cp").text
print(text)

attribute = driver.find_element_by_id('kw').get_attribute('type')
print(attribute)

result = driver.find_element_by_id('kw').is_displayed()
print(result)
'''

#Mouse Event
'''
driver.get("http://yunpan.360.cn")

#right click
right_click = driver.find_element_by_id("xx")
ActionChains(driver).context_click(right_click).perform()

#mouse hover
above = driver.find_element_by_id("id")
ActionChains(driver).move_to_element(above).perform()

#double click
doulbe_click = driver.find_element_by_id("xx")
ActionChains(driver).double_click(double_click).perform()

#drag and drop
element = driver.find_element_by_id("xx")#source element
target = driver.find_element_by_id("xx")#target element
ActionChains(driver).drag_and_drop(element, target).perform()
'''

#Keyboard Event
'''
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("seleniumm")
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys("教程")

# ctrl+a all select
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')
# ctrl+x cut
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')
# ctrl+v paste
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')

driver.find_element_by_id("su").send_keys(Keys.ENTER)
'''

#Get verification
'''
driver.get("http://www.126.com")
print("Before login=========================")

title = driver.title
print(title)

now_url = driver.current_url
print(now_url)
'''

#Time out
'''
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

try:
    print(ctime())
    driver.find_element_by_id("kw22").send_keys("selenium")
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime())
'''

#Alert process
'''
driver.get("http://www.baidu.com")

link = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(link).perform()

driver.find_element_by_link_text("搜索设置").click()
driver.find_element_by_class_name("prefpanelgo").click()

driver.switch_to_alert().accept()
'''

#Operate Cookies
'''
driver.get("http://www.youdao.com")

cookie = driver.get_cookies()
print(cookie)
'''

#Execute JavaScript
'''
driver.get("http://www.baidu.com")
driver.set_window_size(600, 600)

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(3)

js = "window.scrollTo(100,450);"
driver.execute_script(js)
sleep(3)
'''

#HTML5 <video>
'''
driver.get("http://videojs.com/")

video = driver.find_element_by_xpath("body/Setion[1]/div/video")

url = driver.execute_script("return arguments[0].currentSrc;", video)
print(url)

print("start")
driver.execute_script("return arguments[0].play()", video)

sleep(15)

print("stop")
driver.execute_script("arguments[0].pause()", video)
'''

#Screenshot
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys('selenium')
driver.find_element_by_id("su").click()
sleep(2)

driver.get_screenshot_as_file("D:\\video\\baidu_img.jpg")

driver.quit()

