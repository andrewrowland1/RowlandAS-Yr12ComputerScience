#This is a program that calculates the page rank for 3 pages

#Here we are just trying to establish connections between pages
#so that we can keep track of how many pages each page connectsto

A2B = int(input("input 1 if A points to B, input 0 if not"))
A2C = int(input("input 1 if A points to C, input 0 if not"))
B2A = int(input("input 1 if B points to A, input 0 if not"))
B2C = int(input("input 1 if B points to C, input 0 if not"))
C2A = int(input("input 1 if C points to A, input 0 if not"))
C2B = int(input("input 1 if C points to B, input 0 if not"))


#Here we are working out how many outbound links there are on each page
AConnections = A2B + A2C
BConnections = B2A + B2C
CConnections = C2A + C2B

Anew = 0
Bnew = 0
Cnew = 0

#Here, the for loop acts as the number of iterations that the program will do.
for counter in range (1,6):
    #Here, the values worked out from the previous iteration become the values
    #used in the equations.
    #This is so that we use the initial values from the previous iteration and
    #not the "worked" answers that are currently being worked out.
    Avalue = Anew
    Bvalue = Bnew
    Cvalue = Cnew
    #We set the initial priorities of each page to 1 on the first iteration
    if counter == 1:
        Avalue = 1
        Bvalue = 1
        Cvalue = 1
    #Here, each if loop calculates the priority of a page depending on what
    #and how many pages it is referenced by
    if B2A == 1 and C2A == 1:
        Anew = 0.15 + (0.85 * ((Bvalue/BConnections) + (Cvalue/CConnections)))
            
    if B2A == 1 and C2A == 0:
        Anew = 0.15 + (0.85 * (Bvalue/BConnections))

    if C2A == 1 and B2A == 0:
        Anew = 0.15 + (0.85 * (Cvalue/CConnections))

    if C2B == 1 and A2B == 1:
        Bnew = 0.15 + (0.85 * ((Avalue/AConnections) + (Cvalue/CConnections)))

    if C2B == 1 and A2B == 0:
        Bnew = 0.15 + (0.85 * (Cvalue/CConnections))

    if A2B == 1 and C2B == 0:
        Bnew = 0.15 + (0.85 * (Avalue/AConnections))
                         
    if A2C == 1 and B2C == 1:
        Cnew = 0.15 + (0.85 * ((Avalue/AConnections) + (Bvalue/BConnections)))

    if A2C == 1 and B2C == 0:
        Cnew = 0.15 + (0.85 * (Avalue/AConnections))

    if B2C == 1 and A2C == 0:
        Cnew = 0.15 + (0.85 * (Bvalue/BConnections))
    
    #At the end of each iteration the priorities for each page is printed
    print("Iteration: ", counter)
    print(Anew)
    print(Bnew)
    print(Cnew)
#NEXT counter

#Here, we will sort the pages from highest priority to lowest priority
if Anew > Bnew and Anew > Cnew and Bnew > Cnew: 
    print("Highest - Lowest Priority: A - B - C")
if Anew > Bnew and Anew > Cnew and Cnew > Bnew:
    print("Highest - Lowest Priority: A - C - B")
if Bnew > Anew and Bnew > Cnew and Anew > Cnew:
   print("Highest - Lowest Priority: B - A - C")
if Bnew > Anew and Bnew > Cnew and Cnew > Anew:
   print("Highest - Lowest Priority: B - C - A")
if Cnew > Anew and Cnew > Bnew and Anew > Bnew:
   print("Highest - Lowest Priority: C - A - B")
if Cnew > Anew and Cnew > Bnew and Bnew > Anew:
   print("Highest - Lowest Priority: C - B - A")
   



        
