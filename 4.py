from selenium import webdriver
import time


browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_word = browser.find_element_by_id('q')
input_word.send_keys('iphone')
time.sleep(1)
input_word.clear()
input_word.send_keys('ipad')
button = browser.find_element_by_class_name('btn-search')
button.click()