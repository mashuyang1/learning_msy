import json

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
# with open('cookies.json', 'r', encoding='utf-8') as f:
#     txt = json.load(f)
# for i in txt:
#     print(i)
#     browser.add_cookie(cookie_dict=i)
wait = WebDriverWait(browser, 10)
KEYWORD = 'iPad'


def read_cookie():
    with open('cookies.json', 'r') as f:
        txt = json.load(f)
    return txt


def index_page(page):
    """
    抓取索引页
    :param page: 页码
    """
    print(' 正在爬取第 ', page, ' 页 ')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)
        txt = read_cookie()
        for i in txt:
            browser.add_cookie(i)
        browser.refresh()
        # 用来获取淘宝的cookies
        # txt = browser.get_cookies()
        # with open('cookies.json', 'w', encoding='utf-8') as f:
        #     json.dump(txt, f)
        if page > 1:
            input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form> input')))
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form> span.btn.J_Submit')))
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active> span'), str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_products()
        get_cookie()
    except TimeoutException:
        index_page(page)


from pyquery import PyQuery as pq


def get_products():
    """提取商品数据"""
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {'image': item.find('.pic .img').attr('data-src'),
                   'price': item.find('.price').text(),
                   'deal': item.find('.deal-cnt').text(),
                   'title': item.find('.title').text(),
                   'shop': item.find('.shop').text(),
                   'location': item.find('.location').text()}
        print(product)


def get_cookie():
    cookies = browser.get_cookies()
    with open('cookies.json', 'w') as f_cookie:
        json.dump(cookies, f_cookie, indent=2)


MAX_PAGE = 100


if __name__ == '__main__':

    """遍历每一页"""
    for i in range(1, MAX_PAGE + 1):
        index_page(i)
