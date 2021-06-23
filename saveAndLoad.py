import numpy as np

arr1 = np.random.randn(7)

print("The original array:")
print(arr1)

np.save('saved_arr',arr1) # save the array 

arr2 = np.load('saved_arr.npy') # load the saved array from file

print("\nThe array loaded from file:")
print(arr2)
