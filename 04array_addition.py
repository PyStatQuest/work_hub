#Addition of NumPy Arrays
import numpy as np
n1 = np.array([10,20])
n2 = np.array([30,40])

print(np.sum([n1,n2]))

print(np.sum([n1,n2],axis=0))

print(np.sum([n1,n2],axis=1))
