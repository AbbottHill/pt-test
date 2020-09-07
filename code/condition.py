"""
if c1:
    ...
elif c2:
    ...
else

"""

codes = ['sh60000', 'sz60000', 'sh60001', 'hf60003']

# code = 'sz600001'
# if code.startswith('sz'):
#     print(code, "深交所")


for c in codes:
    if c.startswith('sz'):
        print(c, "深交所")
    elif c.startswith('sh'):
        print(c, "上交所")
    else:
        print(c, "error")


########################## abbr #################################
"""
variable = 满足条件时的值 if 条件 else 不满足条件时的值   
"""

value = 1 if 0 > 1 else 2
print(value)

