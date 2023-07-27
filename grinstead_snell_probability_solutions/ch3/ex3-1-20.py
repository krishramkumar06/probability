from numpy import random
import numpy as np

n = 5
arr1 = np.random.permutation(n-1)
arr2 = np.random.permutation(n-1)
arr1 = np.append(arr1, (n-1))
arr2 = np.append(arr2, (n-1)) 

print(arr1)
print(arr2)

