import urllib.request
from urllib import error

try:
    res = urllib.request.urlopen('https://www.cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('request successful')
