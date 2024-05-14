def divide(a, c):
    try:
        b = a / c
        print(f"The divided value is : {b}")
        return 1
    except ZeroDivisionError:
        print(f"Value is invalid!")
        return 0
    except Exception as ae:#It takes all error however zerodivision error takes only zero division error.
        print(" Invalid input")

    finally:#It excutes all the time whatever happens
        print("I am executed all the time")

divide(5,0)