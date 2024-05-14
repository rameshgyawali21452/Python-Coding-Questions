f = open('file.txt','w')
f.write(" Hey I am super exicited to work with AI,Ml and DL!")
f.close()

f = open('file.txt','rb')#rb = opening in binary file, rt = opening in text file
print(f.read())
f.close()

#  no need to close if we open the file using with keyboard
with open('file.txt','a') as f:
    f.write(" \n Since 12 jan 2023")


# This is how we work with file handling in python.+