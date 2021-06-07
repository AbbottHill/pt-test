import numpy as np

print(np.zeros((3, 5)))
print(np.ones((5, 3)))

print(np.empty((2, 3, 2)))

#
# arr1 = np.array([2, 3, 4])
# print(arr1)
# print(arr1.dtype)
#
# arr2 = np.array([1.2, 3, 5])
# print(arr2)
# print(arr2.dtype)
#
# print(arr1 + arr2)
#
# print(arr2 * 10)
#
# data = [arr1, arr2]
# arr3 = np.array(data)
# print(arr3)

arr4 = np.arange(10)
print(arr4)
arr4[5:8] = 10
print(arr4)

arr5 = arr4[5:9].copy()
print(arr5)

