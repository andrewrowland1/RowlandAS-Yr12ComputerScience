parkingspace = [
    ["empty", "empty","empty","empty","empty","empty", "empty","empty","empty","empty"],
    ["empty", "empty","empty","empty","empty","empty", "empty","empty","empty","empty"],
    ["empty", "empty","empty","empty","empty","empty", "empty","empty","empty","empty"],
    ["empty", "empty","empty","empty","empty","empty", "empty","empty","empty","empty"],
    ["empty", "empty","empty","empty","empty","empty", "empty","empty","empty","empty"],
    ["empty", "empty","empty","empty","empty","empty", "empty","empty","empty","empty"],
    ["empty", "empty","empty","empty","empty","empty", "empty","empty","empty","empty"],
    ["empty", "empty","empty","empty","empty","empty", "empty","empty","empty","empty"],
    ["empty", "empty","empty","empty","empty","empty", "empty","empty","empty","empty"],
    ["empty", "empty","empty","empty","empty","empty", "empty","empty","empty","empty"],
    ]
plate = str(input("Please enter your number plate"))
row = int(input("Please enter your row"))
space = int(input("Please enter your space"))
row = row -1
space = space - 1
if parkingspace[row][space] == "empty":
    parkingspace[row][space] = plate
else:
    print("This space is taken")
print(parkingspace)
    
    
            

