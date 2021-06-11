import pandas as pd
from pandas import Series, DataFrame
import numpy as np
from numpy import nan as NA


data = Series([1, NA, 3])
print(data.dropna())

data2 = DataFrame([[1, 2, 3], [1, NA, NA], [NA, NA, NA]])
print(data2.dropna(), end='\n\n')
print(data2.T, end='\n\n')
print(data2.T.dropna(axis=1, how='all'), end='\n\n')

data2.fillna(0)
print(data2, end='\n\n')
data2.fillna(0, inplace=True)
print(data2, end='\n\n')


data3 = Series(np.random.randn(5), index=[['a', 'a', 'a', 'b', 'b'], [1, 2, 3, 1, 2]])
print(data3)
print(data3['b'])
print(data3.b)

print(data3.unstack())
print(data3.unstack().stack())