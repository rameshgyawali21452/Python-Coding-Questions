#How to sort a numpy array by a specific column in a 2D dimensional Array ?

import numpy as np
index = 2
a = np.array([[2,3,1],
              [0,3,2],
              [2,1,0]])
arr_sort = a[a[:,index].argsort()]# To sort the specific column
print(arr_sort)
# if we wanna sort numpy in 2D array by row or column!
print(np.sort(a,axis = 0)) #axis = 0 for sorting by row and 1 for sorting by column