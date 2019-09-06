#program that gets two numbers and outputs the biggest number first
i_Number1 = int(input("Please input a number"))
i_Number2 = int(input("Please input a second number"))
final = -9999999999999
if i_Number1 > i_Number2:
    final = i_Number1
else:
    final = i_Number2
print(final)

