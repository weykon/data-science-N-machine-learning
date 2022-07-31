import numpy as np
# Broadcasting ?
arr1 = np.array([1, 0, 1])
arr2 = np.array([1])
print(arr1 + arr2)

arr1 = np.array([[30, 15], [19, 42]])
arr2 = np.array([[101, 90], [45, 64]])
print(np.dot(arr1, arr2))
