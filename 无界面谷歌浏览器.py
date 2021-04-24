from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
browser.get('http://www.baidu.com')
bsObj = BeautifulSoup(browser.page_source, 'lxml')
print(bsObj.prettify())
'https://raw.githubusercontent.com/Python3WebSpider/TestTess/master/image.png'
https://docs.python.org/3/library/urllib.request.html
