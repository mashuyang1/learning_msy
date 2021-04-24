import urllib.request
import http.cookiejar

cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookie.txt', ignore_expires=True, ignore_discard=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
res = opener.open('http://www.baidu.com')
print(res.read().decode('utf-8'))
