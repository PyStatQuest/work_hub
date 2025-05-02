# Numpy Intersection and Difference
# The function takes two separate arguments (not a tuple)
import numpy as np
n1=np.array([30,40,50,60,70,80,90])
n2=np.array([10,20,30,40,50])

print(np.intersect1d(n1,n2))

print(np.setdiff1d(n1,n2))    # finds elements in n1 that are not in n2

print(np.setdiff1d(n2,n1))    #  finds elements in n2 that are not in n1
