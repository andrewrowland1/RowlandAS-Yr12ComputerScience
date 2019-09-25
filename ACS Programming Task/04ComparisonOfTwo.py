#program that gets two numbers and outputs the biggest number first
i_Number1 = int(input("Please input a number"))
i_Number2 = int(input("Please input a second number"))
final = -9999999999999
if i_Number1 > i_Number2:
    final = i_Number1
    lowest = i_Number2
else:
    final = i_Number2
    lowest = i_Number1
# endif
print(final, lowest)

##ACS - A good slution .. well done
###ACS - try to think of comments which explain the condition for the if statement


