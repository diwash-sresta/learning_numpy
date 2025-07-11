#Conversion of the data types.

import numpy as np;

arr = np.array([1.2,2.3,3.2])
int_arr = arr.astype(int)
print(int_arr.dtype)
print(int_arr)