import numpy as np
# Creating 2-D array
arr = np.arange(0,50,1).reshape(10,5) # Declare a 2-D array

print("The original array")
print(arr)

print("\nThe transposed array")
print(arr.transpose()) # Print the transposed array
#print(arr.T) # This can also be used and same result will be produced


# On line 3, a 2-D array is declared using the arange and reshape functions. The arange function generates the required array elements, and 
# the reshape function arranges them in the form of a 2-D matrix depending upon the parameters.
# The 1st parameter of the reshape function is the number of rows, and the 2nd parameter is the number of columns.
