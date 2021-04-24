from selenium import webdriver


browser = webdriver.Chrome()
url = 'https://srh.bankofchina.com/search/whpj/search_cn.jsp'
browser.get(url)
print(browser.page_source)