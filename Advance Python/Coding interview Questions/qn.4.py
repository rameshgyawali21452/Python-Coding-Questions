# zip is used to combine the elemenst from the two or more iterable for instance(tuples or list) into tuples
# concatenate two lists index-wise

list1 = ['Th','i','Ram','Gyaw']
list2 = ['is','s','esh','ali']
a= [i+j for i,j in zip(list1,list2)]
print(a)