## program that inputs number and outputs the factorial of that number

def fact(number):
    total = 1
    for counter in range (1,number+1):
        total = total * counter
    #next counter
    return total

number = int(input("Please input the number you would like to perform the factorial task on"))
final = fact(number)
print(final)
    
