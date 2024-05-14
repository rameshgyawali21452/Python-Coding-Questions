user = input()
l = user.split(",")
coding = input(" Enter encoding or decoding")
#encodeing
if(coding == "encoding"):
    b =[]
    for letter in l:
        if(len(letter) >= 3):
            l1 = 'lrk'
            l2 = 'jcd'
            st = l1 + letter[-1] + letter[::-1] + l2
            b.append(st)
        else:
            st = letter[-1] + letter[::-1]
            b.append(st)
    print(" ".join(b))

#Decoding
elif (coding =="decoding"):
    d = []
    for str in l:
        if len(str) >= 7:
            ac = str[3:-3]
            tm = ac[::-1]
            d.append(tm)
        else:
            tm = str[2::-1] + str[-1]
            d.append(tm)
        

    print("".join(d))
else:
    print("invalid input!!")

