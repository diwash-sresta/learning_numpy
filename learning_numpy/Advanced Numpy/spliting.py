'''
np.split() = equal spliting
np.vsplit() = vertical spliting
np.hsplit() = horizontal spliting
'''
import numpy as np;

arr =np.array([[1,2,3],[7,8,9]])
print(np.vsplit(arr,2))
print(np.hsplit(arr,3))