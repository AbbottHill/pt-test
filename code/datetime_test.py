# 复制代码
# coding=utf-8
import datetime
import time



print(time.time()) #自1971年1月1日00:00:00 距离现在秒数
time.sleep(1)
print(time.time()) #自1971年1月1日00:00:00 距离现在秒数

now = datetime.datetime.now()
print('datetime.datetime.now()', now)
offsetday = datetime.timedelta(days=10)
now_offsetday = now + offsetday
print(now_offsetday)
print(now_offsetday.year)

# 将日期转化为字符串 datetime => string
print(now.strftime('%Y-%m-%d %H:%M:%S'))

t_str = '2012-03-05 16:26:23'
# 将字符串转换为日期 string => datetime
d = datetime.datetime.strptime(t_str, '%Y-%m-%d %H:%M:%S')
print(d)

# 在datetime模块中有timedelta类，这个类的对象用于表示一个时间间隔，比如两个日#期或者时间的差别。

# 计算两个日期的间隔
d1 = datetime.datetime.strptime('2012-03-05 17:41:20', '%Y-%m-%d %H:%M:%S')
d2 = datetime.datetime.strptime('2012-03-02 17:41:20', '%Y-%m-%d %H:%M:%S')
delta = d1 - d2
print(delta.days)
print(delta)

print(d1 < d2)

# 今天的n天后的日期。
now = datetime.datetime.now()

for num in range(1, 15):
    delta = datetime.timedelta(days=-num)
    n_days = now + delta
    print(n_days.strftime('%Y-%m-%d %H:%M:%S'))


