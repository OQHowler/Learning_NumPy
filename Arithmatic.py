import numpy as np

# making simple arrays
array1=np.array([1,2,3,4])
array2=np.array([5,6,3,8])

### SCALAR ARITHMATIC
# All basic operations 
print(array1 +1)
print(array1 -2)
print(array1 *3)
print(array1 /1)
print(array1**4)


### VECTORIZED MATH FUNCTIONS
print(np.sqrt(array1))
print(np.floor(array1))
print(np.ceil(array1))
print(np.round(array1))
print(np.sqrt(array1))

### COMBINING BOTH
print(np.pi * array1 ** 5)


### Element by element arithmatic
print(array1+array2)
print(array1**array2)


### COMPARISON OPERATOR
# makes a boolean array
print(array1==array2)
print(array2>=6)


###DIRECTLY ASSIGNING VALUES BASED ON SOME CONDITTION
array2[array2==3]=7
print(array2)