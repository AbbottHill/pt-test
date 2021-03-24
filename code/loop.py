
num_list = [1, 2, 3, 4, 5, 10]
price_list = [0.01234, 0.023456, 0.0345, 0.04567]

""" ##########################################################################
range 
range(N) [0, 1, ... N-1 ]
range(a, b) [a, a+1 ... b-1  ]
"""
print(range(10 + 1))
print(list(range(10 + 1)))

# sum_result = 0
# for num in num_list:
#     sum_result += num
# print(sum_result)

sum_result = 0
for num in range(1, 10):
    print(num, end=', ')
    sum_result += num
print(sum_result)

""" ##########################################################################
for
"""


# abbr      value = [临时变量的操作语句 for 循环中的变量 in arr]
# price_list_round = [round(price, 3) for price in price_list]
# print(price_list_round)

""" ##########################################################################
while

"""

# num = 1
# num_end = 10
# sum_result = 0
# while True:
#     sum_result += num
#     if num >= num_end:
#         break
#     num += 1
# print(sum_result)



