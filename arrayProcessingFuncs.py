import numpy as np
# Declare 2 arrays of different types
arr1 = np.random.rand(7)
arr2 = np.array(['Dog', 'Cat', 'Lion', 'Dog', 'Eagle', 'Turtle', 'Lion'])

print("The original array")
print(arr1)

print("\nMean of all elements of array")
print(arr1.mean())

print("\nVariance of all elements of array")
print(arr1.var())

print("\nStandard Deviation of all elements of array")
print(arr1.std())

print("\nSum of all elements of array")
print(arr1.sum())

print("\nSorted array")
arr1.sort()
print(arr1)

print("\nOriginal array")
print(arr2)

print("\nUnique array")
print(np.unique(arr2))
