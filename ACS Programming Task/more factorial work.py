def fact(number):
    if number == 0:
        factorial = 1
    else:
        factorial = number * fact(number-1)
    #endif
    return factorial
number = int(input("input number"))
final = fact(number)
print(final)


