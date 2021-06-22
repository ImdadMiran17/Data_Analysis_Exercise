import numpy as np
# Declare a 2-D array
arr2d = np.array([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
])
print("The Array")
print(arr2d)

print("\nThe new sliced array")
print(arr2d[1:3, 0:2])

print("\nThe new sliced column")
print(arr2d[:, 1:2])
