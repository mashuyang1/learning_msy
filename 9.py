from selenium import webdriver


browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('https://www.zhihu.com/explore')
input_ = browser.find_element_by_class_name('zu-top-add-question')
print(input_)
browser.close()
