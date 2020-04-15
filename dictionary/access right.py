def is_leap(year):
    leap = False
    
    # Write your logic here
    if leap % 400 == 0:
        leap = True
    elif leap % 4 == 0:
        if leap % 100 != 0:
            leap = True
        else:
            leap = False


    return leap

is_leap(1900)