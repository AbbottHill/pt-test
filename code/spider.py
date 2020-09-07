from urllib.request import urlopen

url = "http://hq.sinajs.cn/list=sz000001"

request = urlopen(url)
content = request.read()
# content = content.decode("utf-8")
content = content.decode("gbk")
print(content)

# exit(0)

contents = content.split(",")
print(contents)
print(contents[3])

exit(0)
