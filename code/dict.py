d = {1: 2, 3: 4, 5: 6}
d2 = {2: 3}

print(d.update(d2))
print(d)

shengxiao_dic = {}
shengxiao_str = '鼠牛虎兔龙蛇马羊猴鸡犬猪'
for sx in shengxiao_str:
    shengxiao_dic[sx] = shengxiao_str.index(sx) + 1
print(shengxiao_dic)

# 字典推导式
shengxiao_dic = {i: shengxiao_str.index(i) + 1 for i in shengxiao_str}
print(shengxiao_dic)