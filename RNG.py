# Using the RNG Library in Python using NumPy
import numpy as np

# making a RNG object
rng=np.random.default_rng()

# Printing a random integer between 1 and 6 (like a dice)
print(rng.integers(1,7))

# Printing 5 random numbers between 1 and 100 in a 1d list
print(rng.integers(low=1,high=101,size =5))

# Printing 6 random numbers between 1 and 100 in a 2d list
print(rng.integers(low=1,high=101,size =(2,3)))

#using a seed gives the same random result
rng1=np.random.default_rng(seed=1)
print(rng1.integers(1,7))

# Printing random loating point numbers
print(np.random.uniform(-1,1,size=2))

# Shuffling an array
array1=np.array([1,2,3,4,5,6,7,8,9])
rng.shuffle(array1)
print(array1)

# Random choice from a array
array2=np.array([11,22,33,44,55,66,77,88,99])

choice2=rng.choice(array2)
print(choice2)

more_choices2=rng.choice(array2,size=2)
print(more_choices2)