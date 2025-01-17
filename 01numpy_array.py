#Arrays in NumPy is like learning how to handle data smarter and faster in Python.
#Think of NumPy arrays as a toolbox for numbers—it’s faster, cleaner, and built for the kind of work you’ll need when handling a lot of data.
import numpy as np
#1D array
l1=[1,2,3,4]
n1=np.array(l1)
print(n1)
print(type(n1)) 

#2D array
n2=np.array([[1,2,3,4],[4,5,6,7]])      # [1, 2, 3, 4] and [4, 5, 6, 7] must be enclosed in another list, like [[1, 2, 3, 4], [4, 5, 6, 7]]
print(n2)
print(type(n2))

#Initializing NumPy array with zeros.
n3=np.zeros((10,10))                    # 10 rows and 10 columns.
print(n3)

#Initializing NumPy array with same number.
n4=np.full((3,3),55)                    # 3 rows and 3 columns.
print(n4)

#Initializing NumPy array within a range.
n5=np.arange(10,100)                    # Excluding 100
print(n5)

n6=np.arange(10,100,5)                 # Excluding 100
print(n6)

#Initializing NumPy array with random numbers.
n7=np.random.randint(100,200,10)               # Generate 10 random integers between 100 and 200

#Checking the shape of NumPy arrays.
n8=np.array([[1,2,3,4,],[4,3,2,1]])
print(n8) 

n8.shape=(4,2)
print(n8)

n8.shape=(8,1)
print(n8)


