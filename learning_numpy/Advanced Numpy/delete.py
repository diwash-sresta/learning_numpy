'''
np.delete(array,index,axis = None)
'''

import numpy as np;
 # for 1d
arr = np.array([1,2,3,4,5,6,7,8])
new_arr = np.delete(arr,2)
print(new_arr)

#for 2d 

arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
new_arr_2d = np.delete(arr_2d,1,axis=0)
print(new_arr_2d)

new_col_arr_2d = np.delete(arr_2d,1,axis=1)
print(new_col_arr_2d)