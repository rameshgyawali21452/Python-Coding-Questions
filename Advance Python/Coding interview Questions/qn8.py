# Add items 7000 after 6000  in the following python list:
import numpy as np
list2 = ([10, 20, [300, 400, [5000, 6000], 500], 30, 40])
list2[2][2].append(7000)
print(list2)