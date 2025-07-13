'''
np.concatenate((array1,array2),axis = 0)

axis 0 > vertical stacking
axis 1 > horizontal stacking
'''
import numpy as np;

arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[1,3]])
new_arr = np.concatenate((arr1,arr2),axis=1)
print(new_arr)