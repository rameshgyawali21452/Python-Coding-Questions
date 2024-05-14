# Given a Python list, remove all occurrence of 20 from the list 
list1 = [5,20,15,20,25,50,20]
count1 = list1.count(20)
# def removeval(list2, val):
#     return ()
for i in range(count1):
    list1.remove(20)
print(list1)