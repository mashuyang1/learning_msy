import requests
from pyquery import PyQuery as pq

url = "https://www.zhihu.com/explore"
header = {  # 登录抓包获取的头部
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0)Gecko/20100101 Firefox/60.0'
}
html = requests.get(url, headers=header).text
doc = pq(html)
items = doc('.ExploreCollectionCard-contentList').items()
for item in items:
    # print(item)
    question = item.find('a').text()
    answer = item.find('.ExploreCollectionCard-contentExcerpt').text()
    file = open('explore.txt', 'a', encoding='utf-8')
    file.write('\n'.join([question, answer]))
    file.write('\n' + '=' * 50 + '\n')
    file.close()

