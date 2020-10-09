from selenium import webdriver
import time

# 搜索商品
def search_product(key_word):
    # 定位输入框
    browser.find_element_by_id('q').send_keys(key_word)
    # 定义点击按钮，并点击。淘宝网的网页源代码:
    # <div class="search-button">
    # <button class="btn-search tb-bg" type="submit" data-spm-click="gostr=/tbindex;locaid=d13">搜索</button></div>
    browser.find_element_by_class_name('search-button').click()
    # 最大化窗口
    browser.maximize_window()
    # 等待15秒
    time.sleep(15)

def main():
    browser.get('https://www.taobao.com/')
    search_product(key_word)

if __name__ == '__main__':
    key_word = input('请输入你要搜索的商品：')
    browser = webdriver.Chrome()
    main()