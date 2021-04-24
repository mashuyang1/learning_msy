import sys

import requests
from selenium import webdriver

sys.argv = ['we', 'are', 'arguments']
print('The command line arguments are:')
for i in sys.argv:
    print(i)

requests.get('http://www.baidu.com')
browse = webdriver.Chrome()
browse.close()

