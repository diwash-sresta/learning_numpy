import numpy as np;

arr = np.array([1,2,3,4,5])
print(arr)

#with default values
#np.zeros(shape)

zeros_array = np.zeros(3)
print(zeros_array)

#ones(shape)

ones_array = np.ones((2,3))
print(ones_array)

#full(shape,value)

filled_array = np.full((2,3),7)
print(filled_array)