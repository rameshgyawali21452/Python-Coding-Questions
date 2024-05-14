#Map Function Approach

def area(a):
    return a*a
list1 = [2,4,5,9,20,29,5,6,7]
list2 = list(map(area,list1))
print(list2)