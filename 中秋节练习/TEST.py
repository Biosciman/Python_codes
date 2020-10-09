from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://youhui.pinduoduo.com/')
key_word = '电脑'
getvalue = browser.find_element_by_class_name('search-bar-input')
getvalue = getvalue.find_element_by_xpath('..//div/*')
browser.execute_script('arguments[0].value = "电脑";', getvalue)
browser.find_element_by_class_name('search-bar-input').click()
browser.maximize_window()
