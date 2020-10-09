from selenium import webdriver
import time

# 创建浏览器对象，该操作会自动帮我们打开Google浏览器窗口
browser = webdriver.Chrome()

# 调用浏览器对象，向服务器发送请求。该操作会打开Google浏览器，并跳转到“百度”首页
browser.get('https://www.baidu.com')

# 刷新浏览器
browser.refresh()

# 最大化窗口
browser.maximize_window()

# 定位"抗击肺炎"链接内容
element = browser.find_element_by_id('kw')
element.send_keys('hhhh')
element = browser.find_element_by_id('su')
element.click()
# browser.refresh()