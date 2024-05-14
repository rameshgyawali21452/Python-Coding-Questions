# GOing to reading the file of readfile.txt line by line \
f1 = open("readfile.txt",'r')
while True:
    l = f1.readline()
    if not l:
        break
    a0 = int(l.split(",")[0])# doing a type casting with spliting the elements with ","
    a1 = int(l.split(",")[1])
    a2 = int(l.split(",")[2])
    a4 = int(l.split(",")[3])

    print(f"The marks of Python is : {a0*2}")
    print(f"The marks of Python is : {a1*2}")
    print(f"The marks of Python is : {a2*2}")
    print(f"The marks of Python is : {a4*2}")
