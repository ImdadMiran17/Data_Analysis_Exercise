import numpy as np

arr = np.arange(0,10,1)
print("The Array")
print(arr)

new_arr1 = arr[1:7] # This command selects a range of elements from the array
print("\nThe new sliced array")
print(new_arr1)

new_arr2 = arr[:] # This command selects all elements in the array
print("\nThe new sliced array with all elements")
print(new_arr2)
