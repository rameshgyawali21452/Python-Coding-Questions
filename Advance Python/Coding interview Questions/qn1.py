# How to Remove from one array those items that exist in another?

import numpy as np
a = np.array([3,2,5,6,9])
b = np.array([3,9,10,12,19])
# using set operation to display the not existing items of a in b

c = np.setdiff1d(a,b)
print(c)
