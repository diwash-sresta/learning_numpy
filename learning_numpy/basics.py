import numpy as np;

a= np.array([1,2,3,4], dtype='int32')
print(a)

b= np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)

# Get Dimensions
print(a.ndim)

#Get size
print(b.shape)

#Get Type
print(a.dtype)

#Get Size
print(b.itemsize)
print(a.itemsize)

# Get Total size
print(a.nbytes)