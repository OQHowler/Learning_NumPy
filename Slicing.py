import numpy as np

# Making a 2d array
array1 = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]
                ])

# Slicing operator is written as array1[start:end:step]

### SLICING FOR ROWS

# Normal printing
print(array1[0])
print(array1[-1])

# Printing some specific continous portion of the list
print(array1[0:3]) # starting index is inclusive
                   # while the ending index is EXCLUSIVE

# starting from somewhere middle and printing the whole list
print(array1[1:])

# Printing every second row starting from the somewhere middle and ending somewhere at the middle
print(array1[1:3:2])

# Printing every second element of the whole list
print(array1[::2])

# Printing whole list in reverse
print(array1[::-1])

# Printing every second element of the reverse list 
print(array1[::-2]) 


### SLICING FOR COLUMNS

# Printing first element of every row
# OR
# Printing the first column as list
print(array1[:,0])

# Printing last column
print(array1[:,-1])

# Printing first three columns
print(array1[:,0:3])

# Printing every second column
print(array1[:,::2])

# Printing every column, from last column to first column
print(array1[:,::-1])


### SLICING FOR BOTH COLUNNS AND ROWS


# Printing intersection of first two rows and first two columns
print(array1[0:2,0:2])