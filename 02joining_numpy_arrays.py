# Joining numpy arrays
import numpy as np
n1=np.array([1,2,3])
n2=np.array([4,5,6]) 

print(np.vstack((n1,n2)))          # Vertical stacking
print(np.hstack((n1,n2)))          # Horizontal stacking
print(np.column_stack((n1,n2)))    # column stack




