
a = (1, 3, 5, 7)
b = 4
l = list(filter(lambda x: x < b, a))
print(l)

t = ('1', '2', '3', '1')
# t = ['1', '2', '3', '4', '1']
# t[1] = '0'
print(t[1])

for i in t:
    print(i, end=" ")
