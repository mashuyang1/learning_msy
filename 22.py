from urllib.parse import urlencode, parse_qsl, quote, unquote
from urllib.parse import urlparse

params = {'name': 'germey',
          'age': '23'}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)
params = urlparse(url)
canshu = parse_qsl(params.query)
print(canshu)
kw = '中国'
url = base_url + 'wd=' + quote(kw)
print(url)
url = unquote(url)
print(url)