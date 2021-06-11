import requests
import re
import shutil
import os

content = requests.get('http://www.cnu.cc/discoveryPage/hot-0?page=1')
print(content.text)

pattern = re.compile('<a href="(.*?)".*?"title">(.*?)</div>', re.S)
results = re.findall(pattern, content.text)
print(results)

for i in results:
    url, name = i
    print(url, re.sub('\s', '', name))

def download_pic(pic_url, local_path):
    response = requests.get(pic_url, stream=True)
    if response.status_code == 200:
        with open(local_path, 'wb') as f:
            # response.raw.deconde_content = True
            shutil.copyfileobj(response.raw, f)


abspath = os.path.abspath('.')
download_pic('http://imgoss.cnu.cc/2106/10/53917fa4a3983bacb16e7f9c449b7dc8.jpg?x-oss-process=style/content',
             os.path.join(abspath, 'download_1.jpg'))
