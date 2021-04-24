from selenium import webdriver
import time


browser = webdriver.Chrome()
browser.maximize_window()
browser.get('http://www.baidu.com')
browser.execute_script('window.open()')
browser.switch_to.window(browser.window_handles[1])
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to.window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(1)
browser.switch_to.window(browser.window_handles[2])
browser.get('https://www.python.org')
