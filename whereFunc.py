import numpy as np
# Declare 2 arrays
arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([500, 600, 700, 800])

cond = np.array([False, True, False, True]) # Create an array with bool operators

res = np.where(cond, arr1, arr2) # apply the where condition
print(res)

# The NumPy where function took 3 values cond, arr1, and arr2. This function first checks the value for cond.
# If the value of cond is True, then it returns the value of arr1 for the respective index, and if it is False, then it returns the value of arr2 for its respective index.
# In this case, arr1 is the first parameter after cond, and arr2 is the last parameter of the where function. These arrays can be changed and replaced with any desired value.
