list = [4,5,6,7,8]
print(list[0])
for i in list:#it will print all available list element eventhough we print first element!
    print(i)
# how can we overcome or print only one time then iterator concept comes here! lets say
it = iter(list)
print(it.__next__())
#it's print the element only one time where ever we use where next keyboard helps to access the next element.
print(it.__next__())
for i in list :
    print(it.__next__())#print the remaining element in the list