'''
reshape(rows,columns) specify new shape

can only be done if dimensions match

1D -> 2D
'''

import numpy as np;

arr = np.array([1,2,3,4,5,6])
reshaped_arr = arr.reshape(2,3)
print(reshaped_arr)