import numpy as np

#Aggregate functions work on every element of a list and return a single value

array1 = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10]])

print(np.sum(array1))  # summation of DATA
print(np.mean(array1)) # mean of DATA
print(np.std(array1))  # Standard Deviation of DATA
print(np.var(array1))  # Variance of DATA


print(np.min(array1))  # Maximun observation in DATA 
print(np.max(array1))  # Minimum observation in DATA

print(np.argmax(array1)) # Postion of max observation in DATA
print(np.argmin(array1)) # Postion of Min observation in DATA

## Applying function to particular axis
# axis=0 means working with columns
# axis=1 means working with rows

print(np.sum(array1,axis=0)) # summation in all columns
print(np.sum(array1,axis=1)) # summation in all rows
