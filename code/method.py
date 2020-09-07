
# 有默认值的参数调用是可以不传，需要放在形参的最后

def print_two_var(var_1, var_2='value 2'):
    print(var_1, var_2)
    return "result"


print_two_var(1, 2)
print_two_var(var_1=1, var_2=2)
print_two_var(var_2=1, var_1=2)
