def raiseerror():
    a = int(input("Enter the x value between 0 to 20 : "))
    if(a < 0 or a > 20):
        raise ValueError("Value should between 0 to 20!")
    else:
        print("successfully executed.")

raiseerror()