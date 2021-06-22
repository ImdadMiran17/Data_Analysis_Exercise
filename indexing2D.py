import numpy as np
# Declare a 2-D array
arr2d = np.array([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
])
print("The Array")
print(arr2d)

print("\nElement at row 0 and column 1")
print(arr2d[0][1])

print("\nElements in a range of last two rows & columns")
print(arr2d[1:3, 1:3])

arr2d[1:3, 1:3] = 20
print("\nNew 2D array after changing last two rows & columns values")
print(arr2d)
