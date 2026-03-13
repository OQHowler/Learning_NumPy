import numpy as np

# Broadcasting is the method of working with two arrays in which sometimes one of the array is virtually stretched to become the same shape as the other array

## RULES FOR BROADCASTING OF TWO ARRAYS
# suppose we print shape of two arrays
# suppose their dimensions od the shape are (A1,B1,C1,D1,E1,...) 
#                                           and 
#                                           (A2,B2,C2,D2,E2....)
# Then broadcasting can only be done when 
# (A1 is equal to A2 ) OR (A1 has value 1) OR (A2 has value 1) 
# check this condition for every dimension
# If this condition is true for every dimension then only broadcasting can be applied

#making two arrays of acceptable shapes
array1= np.array([1,2,3])
array2= np.array([[1],[2],[3]])

# Broadcasting
print(array1*array2)

