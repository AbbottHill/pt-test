七 = "七"
list_var = [1, 2, '3', "four", 5, "6", 七, [8], 9]

# print(list_var, type(list_var))
# print(list_var[6])
# print("七" in list_var)
# print(list_var.index(5))
# print(list_var.index(4))  # ValueError: 4 is not in list

# print('**' * 30)
# print(len(list_var))
# print(list_var[1: 7])
# print(list_var[1: 7: 3])    # 从1-7中每隔3个元素，取第一个

list_num = [2, 1, 5, 6, 3]
# print(max(list_num))
# print(min(list_num))
# print(sorted(list_num))
# list_num.sort() # sort 改变原数组，sorted 不改变
# print(list_num)

# list_num.sort(reverse=True)
# print(list_num)
# del list_num[1]
# print(list_num)

# print(list_num + list_var)
list_num.reverse()
print(list_num)

"""
dist 字典
"""

dist_var = {1: "a", 2: "b"}
print(dist_var[1])    # [key] 会报异常，get 返回None
# print(dist_var[0])    # [key] 会报异常，get 返回None
# print(dist_var.get(1))
# print(dist_var.get(0))

print(dist_var.keys())
print(dist_var.values())
