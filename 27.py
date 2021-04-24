import re
import time

import bs4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
wait = WebDriverWait(browser, 10)


def get_index_page():
    url = 'https://srh.bankofchina.com/search/whpj/search_cn.jsp'
    browser.get(url)
    input_first = browser.find_element_by_css_selector('input.search_ipt[name="erectDate"]')
    # print(type(input_first))
    input_first.send_keys("2020-01-01")
    input_second = browser.find_element(By.CSS_SELECTOR, 'input.search_ipt[name="nothing"]')
    input_second.send_keys('2021-04-02')
    select = browser.find_element_by_tag_name('select')
    select.send_keys('美元')
    submit = browser.find_element(By.CSS_SELECTOR, 'form#historysearchform input.search_btn')
    submit.click()
    page_numbers_str = browser.find_element_by_css_selector('div.BOC_main.publish .turn_page li').text
    page_numbers = re.search(re.compile(r'\d+'), page_numbers_str).group()
    return page_numbers


def page_turning():
    yeshu = browser.find_element_by_css_selector('.turn_page li a.current').text
    next = int(yeshu) + 1
    browser.find_element_by_link_text(str(next)).click()
    # time.sleep(3)


def parse_page_source():
    html = browser.page_source
    soup = bs4.BeautifulSoup(html, 'lxml')
    a = soup.select('div.BOC_main.publish table tbody tr')
    for table in a:
        print()
        for cum in table:
            print(cum.string.replace('\n', ''), end='\t')


if __name__ == '__main__':
    page_number = get_index_page()
    # print(type(int(page_number)))
    for i in range(0, int(page_number)):
        # print("正在打印第\\s页" % i)
        parse_page_source()
        page_turning()
    # page_turning()
    browser.close()
