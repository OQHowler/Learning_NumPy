import numpy as np

# Filtering means selecting data points form a list that match some specific criteria

# take data as ages of students in a class
ages1 = np.array([
 [21, 17, 19, 20, 16, 30, 18, 65],
 [39, 22, 15, 99, 18, 19, 20, 21]
])

# Creating a array of students who are  teenagers
teenagers1 = ages1[ages1<20] # flattens out the array as we are using boolean indexing
print(teenagers1)

# Creating a array of students who are adult
adults1 = ages1[ages1>=20] 
print(adults1)

### if ordering really matters, then we will have to use a specific function
# syntax for this new function -> np.where(condition,array, what to replace non satifiale elements with)
adults2 = np.where(ages1>=20,ages1,0)
print(adults2)
#This method is inefficent and should be used only when ordering is really required