# Given a two python list. Iterate both lists simultaneously such that list
#  1 should display item in orginal order and list2 in reverse order?
l1 = [1,2,4,5,6]
l2 = [3,4,7,9,10]
#We should print the l1 in same order but l2 in reverse order
l3=[]
l4 = []
for i,j in zip(l1,l2[::-1]):
    l3.append(i)
    l4.append(j)
    print(i,j)

print(l3,l4)

