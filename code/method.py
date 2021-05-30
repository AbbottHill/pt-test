
############# filter map reduce zip
l = [1, 3, 5, 7]
l2 = [2, 4, 6, 8]
a = list(filter(lambda x: x > 4, l))
print(a)

print(list(map(lambda x,y: x + y, l, l2)))

from functools import reduce
red = reduce(lambda x, y: x + y, l, 0)
print(red)

for i in zip((1, 2, 3), (4, 5, 6)):
    print(i)

exit()

# 可变长参数 *a
def func(*a, b):
    print(a)


func(1, 2, 3, b=4)
func(1, 2, b=4)
func(b=4)


# 有默认值的参数调用是可以不传，需要放在形参的最后

def print_two_var(var_1, var_2='value 2'):
    print(var_1, var_2)
    return "result"


print_two_var(1, 2)
print_two_var(var_1=1, var_2=2)
print_two_var(var_2=1, var_1=2)
