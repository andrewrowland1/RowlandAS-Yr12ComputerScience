#program that asks the user for a number between 1 and 10 and then outputs the times table for that number
i_Number = int(input("Please input a number between 1 and 10"))
#Check if number is between 1 and 10

while i_Number < 1 or i_Number > 10:
    i_Number = int(input("Please input a number between 1 and 10"))
### End while

#program will times the number by the counter. after each loop the counter increases by 1 until the counter is above 12. then it will terminate
for counter in range (1,13):
    print(i_Number * counter)
    #counter increases by 1 each loop
    counter = counter + 1
### Next


###ACS - Comment are better but you need the end of loop comments
###ACS - You do not need to increment the counter as the for loop does this automtically for you




            

               

               

               
