# Seek() and tell()
# Seek() is used for printing the current position 
#tell() is used to returning the current position of the file! 
f1 = open("file.txt",'r')
f1.seek(10)# it will read after 10 positions.
curr_chr = f1.read(10)
print(curr_chr)
print(type(f1))
# if  i want to know the current position of the file 
print(f1.tell())
# The reason behind this is , i have started from 10 index, i read 10 index . i.e 20
# Make sence? 

