import sys
import urllib
from urllib import request, parse
import socket

print(sys.getdefaultencoding())

# url = 'http://www.baidu.com'
# response1 = request.urlopen(url, timeout=1)
# print(response1.read())

url = 'http://httpbin.org/get?a=%E5%8F%82%E6%95%B0'
response1 = request.urlopen(url, timeout=1)
print(response1.read().decode('utf-8'))

try:
    response2 = request.urlopen('http://httpbin.org/get?a=1', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('time out !')

headers = {
    'Host': 'httpbin.org',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
}

dict = {
    'name': '小明'
}

data = bytes(parse.urlencode(dict), encoding='utf-8')
url_post = 'http://httpbin.org/post'
req = request.Request(url_post, data=data, headers=headers, method='POST')
response3 = request.urlopen(req)
print(response3.read().decode('utf-8'))


import requests
response4 = requests.post(url_post, dict)
print(response4.json())

url_get = 'http://httpbin.org/get?name=小明'
response5 = requests.get(url_get, dict)
print(response5.json())

