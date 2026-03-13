import numpy as np

# Making a ZERO dimensional array 
array1=np.array('A')


# Making a ONE dimensional array 
array2=np.array(['A','B'])

# Making a TWO dimensional array
array3 =np.array(['A','B'],['C','D',],['E','F'])

# Making a THREE dimensional array
                                                      # each layer has 3 rows
                                                      # each row has 2 columns
array4=np.array([[['A','B'],['C','D',],['E','F']],    # top most layer 
                 [['G','H'],['I','J',],['K','L']],
                 [['M','N'],['O','P',],['Q','R']]])   # bottom most layer

print(array1.ndim)#prints value of dimension of our array1(which is zero)

print(array4.shape)# returns a tuple of integers in the following form
#(layers/depth,  number of rows,  number of columns)

# Printing elements with chain indexing
print(array4[0][0][1])

# Printing elements with multi- dimensional indexing
print(array4[0,0,1])# FASTER EXECUTION

#Using string concatenation to print words
word=array4[1,0,1] + array4[1,1,0]
print(word)