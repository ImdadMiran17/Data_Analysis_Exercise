import numpy as np
# Declare 2 array
arr1 = np.arange(1,40,4)
arr2 = np.arange(1,30,3)

print("The first array\n", arr1, "\nThe second array\n", arr2, '\n')

print("The Exponent Function")
print(np.exp(arr1))

print("\nThe Square Function")
print(np.square(arr1))

print("\nThe Square root Function")
print(np.sqrt(arr1))

print("\nThe Cube root Function")
print(np.cbrt(arr1))

print("\nThe Addition Function")
print(np.add(arr1, arr2))

print("\nThe Subtraction Function")
print(np.subtract(arr1, arr2))
