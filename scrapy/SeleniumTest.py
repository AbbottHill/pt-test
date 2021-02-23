from selenium import webdriver

chrome = webdriver.Chrome(executable_path="D:\driver\chromedriver\chromedriver.exe")

#2.通过浏览器向服务器发送URL请求
chrome.get("https://www.baidu.com/")


