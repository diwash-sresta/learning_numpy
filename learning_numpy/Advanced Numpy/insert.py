'''
np.insert(array,index,value,axis=None)
axis = 0 -> row -wise & default, 1 -> column-wise change
'''
import numpy as np;
#for 1d array
arr = np.array([10,20,30,40,50,60])
new_arr = np.insert(arr,3,70)
print(new_arr)

#for 2d array

arr_2d = np.array([[1,2,3],[7,8,9]])
new_arr_2d = np.insert(arr_2d,1,[4,5,6],axis=0)
print(new_arr_2d)
print(arr_2d)