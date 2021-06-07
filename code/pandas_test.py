import pandas as pd
from pandas import Series, DataFrame
import random

s1 = Series([4, 5, -6, 7])
print(s1)
print(s1.index)
print(s1.values)

s2 = Series([1, 2, -3, 4], index=['a', 'b', 'c', 'd'])
print(s2)

# dic to series
sdata = {'bj': 10000, 'hf': 1000, 'aq': 500}
s3 = Series(sdata)
print(s3)

s3.index = ['bj', 'sh', 'hf']
print(s3)
print(type(s3))


s4 = s3.reindex(['sh', 'bj', 'hf', 1], fill_value=10)  # reindex
print('s4', s4)

s5 = s4.reindex(range(6), method='ffill')
print(s5)

print('--------------------------------------------------------------------')

ddata = {'city': ['shanghai', 'shanghai', 'beijing', 'hefei'],
         'year': [2019, 2020, 2020, 2021],
         'pop': [2000, 2001, 3000, 1000]}
df = DataFrame(ddata)
print(df)

# print(random.randint(1, 4))
df['new'] = random.randint(1, 4)
print(df)
df['cap'] = df.city = 'beijing'
print(df)

pop = {'bj': {2008: 1.5, 2009: 2.0},
       'sh': {2008: 2.0, 2009: 2.6}}
df2 = DataFrame(pop)
print(df2)
print(df2.T)  # 行列转换


