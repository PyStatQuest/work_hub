import numpy as np
#Creating a Random Integer Array
n1=np.random.randint(1,50,10)
print(n1)

np.save("myarray",n1)  #Save the array to a file named "myarray.npy"

new_np=np.load("myarray.npy")   # Load the saved array from the file
print(new_np) 