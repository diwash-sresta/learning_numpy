import numpy as np;

a = np.array([1,2,3])
b = np.array([[1,2,3],[4,5,6]])
c = np.array([10,20,30,40.5])

print(a.shape)

print(a.size)#size

# Get Dimensions
print(a.ndim)

#Get size
print(b.shape)

#Get Type
print(a.dtype)
print(c.dtype)

#Get Size
print(b.itemsize)
print(a.itemsize)

# Get Total size
print(a.nbytes)
