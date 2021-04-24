import os
from hashlib import md5

import requests
from selenium import webdriver


def get_cookies(url):
    str = ''
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    browser.get(url)
    for i in browser.get_cookies():
        try:
            name = i.get('name')
            value = i.get('value')
            str = str + name + '=' + value + ';'
        except ValueError as e:
            print(e)
    return str


cookies = get_cookies('https://www.toutiao.com')
headers = {
    'cookie': cookies,
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/89.0.4389.82 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
}


def get_page(offset):
    params = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
    }
    url = 'https://www.toutiao.com/api/search/content/'
    try:
        while True:
            r = requests.get(url, params=params, headers=headers)
            if r.status_code == requests.codes.ok and r.json().get('count') != 0:  # request.codes.ok -> 200
                print(r.json())  # 打印网页代码
                break
            else:
                print('requests get_page error!')
        return r.json()
    except requests.ConnectionError:
        return None


def get_img(json):
    lis = []
    if json.get('data'):
        # print(json.get('data'))
        for item in json.get('data'):
            title = item.get('title')
            images = item.get('image_list')
            if images is not None:
                for image in images:
                    dic = {'image': image.get('url'), 'title': title}
                    lis.append(dic)
        print(lis)
        return lis


def save_image(item):
    img_path = 'img' + os.path.sep + item.get('title')
    if not os.path.exists(img_path):
        os.makedirs(img_path)
        try:
            response = requests.get(item.get('image'))
            if response.status_code == 200:
                file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(),
                                                 'jpg')
                if not os.path.exists(file_path):
                    with open(file_path, 'wb') as f:
                        f.write(response.content)
                else:
                    print('Already Download', file_path)
        except requests.ConnectionError:
            print('failed to save image')


def main(offset):
    json = get_page(offset)
    for item in get_img(json):
        save_image(item)


if __name__ == '__main__':
    main(0)
