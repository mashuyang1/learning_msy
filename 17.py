import urllib.request
import http.cookiejar

filename = 'cookie.txt'
cookie = http.cookiejar.LWPCookieJar()  
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
opener.open('http://www.baidu.com')
cookie.save(filename, ignore_discard=True, ignore_expires=True)
