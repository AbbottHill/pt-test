"""
first python
"""
# coding=utf-8
from past.builtins import raw_input
from datetime import datetime
import random

a1 = [1, 2, 3]
arr = []
for x in range(10):
    # global arr=[]
    a_ = random.choice(a1)
    arr.append(a_)
print(arr)
print(type(arr))

print(str(datetime.now().date()).replace('-', ''))
print(str(datetime.now().date()))

print("hello world")
print("你好！")

print(1 / 2)

print(3 ** 2)

print(3 * "abc-")

print(1, 2, 3)

stock_count = 3000
print(stock_count, type(stock_count))

price = 3.5
print(1 + price)


#
# if True:
#     print ("Answer")
#     print ("True")
# else:
#     print ("Answer")
#     # 没有严格缩进，在执行时会报错
#   print ("False")


paragraph = """这是一个段落。
包含了多个语句"""

"""
这是一个段落。
包含了多个语句
"""

raw_input("按下 enter 键退出，其他任意键显示...\n")

# mutiple row
import sys
x = 'runoob'
sys.stdout.write(x + '\n')


input("\n\n按下 enter 键后退出。")

if __name__ == '__main__':
    print('--main--')


