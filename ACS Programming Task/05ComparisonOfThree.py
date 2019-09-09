#program that takes 3 numbers and outputs the largest number
i_Number1 = int(input("Please input a number"))
i_Number2 = int(input("Please input a number"))
i_Number3 = int(input("Please input a number"))
#use if statements to work out which number is the greatest

if i_Number1 > i_Number2 and i_Number1 > i_Number3:
    greatest= i_Number1
    if i_Number2 > i_Number3:
        middle = i_Number2
        lowest = i_Number3
    else:
        lowest = i_Number2
        middle = i_Number3
    print(greatest, middle, lowest)
if i_Number2 > i_Number1 and i_Number2 > i_Number3:
    greatest= i_Number2
    if i_Number1 > i_Number3:
        middle = i_Number1
        lowest = i_Number3
    else:
        lowest = i_Number1
        middle = i_Number3
    print(greatest, middle, lowest)
if i_Number3 > i_Number2 and i_Number3 > i_Number1:
    greatest= i_Number3
    if i_Number1 > i_Number2:
        middle = i_Number1
        lowest = i_Number2
    else:
        lowest = i_Number1
        middle = i_Number2
    print(greatest, middle, lowest)
if i_Number1 == i_Number2 and i_Number1 == i_Number3:
    print(i_Number1, i_Number2, i_Number3)
    
    





