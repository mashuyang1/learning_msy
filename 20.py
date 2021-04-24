import socket
import urllib.request
import urllib.error

try:
    res = urllib.request.urlopen('http://www.cuiqingcai.com/index.htm', timeout=0.01)
except urllib.error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print('time out')