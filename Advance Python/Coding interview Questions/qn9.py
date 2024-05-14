# Given a python list, find value 20 in the list, and if it is present , 
# replace it with 200. Only update the first occurence of a value?
list1 = [500,100,300,400,20,900]
l_indx = list1.index(20)
list1[l_indx] = 200
print(list1)

