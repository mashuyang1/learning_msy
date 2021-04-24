import time

from selenium import webdriver


browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
time.sleep(1)
browser.execute_script('window.scrollTo(document.body.scrollHeight, 0)')
browser.execute_script('alert("To Button")')
