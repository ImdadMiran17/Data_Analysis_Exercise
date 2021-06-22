import numpy as np

arr = np.arange(0,10,1)
print("The Array")
print(arr)

new_arr = arr[1:7].copy()
print("\nThe new sliced array")
print(new_arr)

new_arr[:] = 20
print("\nThe Original array")
print(arr)
