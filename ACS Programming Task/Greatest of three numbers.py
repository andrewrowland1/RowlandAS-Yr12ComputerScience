#program that takes 3 numbers and outputs the largest number
i_Number1 = int(input("Please input a number"))
i_Number2 = int(input("Please input a number"))
i_Number3 = int(input("Please input a number"))
#use if statements to work out which number is the greatest


if i_Number1 > i_Number2:
    greatest = i_Number1
else:
    greatest = i_Number2
if greatest < i_Number3:
    greatest = i_Number3
else:
    print(greatest)
