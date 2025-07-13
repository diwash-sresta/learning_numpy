'''
np.isinf(array) 
eg : 10 ^1000 
1/0
'''
import numpy as np;
arr = np.array([1,2,np.inf,3,4,-np.inf])
print(np.isinf(arr))#checking infinity value

clean_arr = np.nan_to_num(arr, posinf=1000, neginf=-1000)#replacing infinity value
print(clean_arr)