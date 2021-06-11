from bs4 import BeautifulSoup
import requests

url = 'https://www.infoq.com/news/'
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

requests_get = requests.get(url, headers=headers)
# print(requests_get.text)
soup = BeautifulSoup(requests_get.text)
# print(soup.prettify())
# print(soup.title)
# soup.find_all()

