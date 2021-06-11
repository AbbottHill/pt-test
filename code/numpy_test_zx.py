import numpy as np
from pandas import Series

print(list(range(0, 4)))
print(list(np.arange(0, 4)))
print(np.random.random(10))
print(Series(np.random.randn(4), index=list(range(0, 4))))
print(Series(np.random.randint(19), index=list(range(0, 4))))

