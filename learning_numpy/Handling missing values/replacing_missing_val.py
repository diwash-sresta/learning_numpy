#np.nan_to_num(array,nan=value) default =0

import numpy as np;
arr = np.array([1,2,np.nan,3,4,np.nan])
clean_arr = np.nan_to_num(arr,nan=0)
print(clean_arr)