mylist=[]
outlet1=[11,12,15,10]
outlet2=[5,8,3,6]
outlet3=[10,12,15,10]

mylist.append(outlet1)
mylist.append(outlet2)
mylist.append(outlet3)
total = 0
print(mylist[0][0])
for y in range (0,4):
    for x in range (0,3):
        total = total + mylist[x][y]
    print("value for quarter", y , " = ", total)
    total = 0

print(sum(outlet1))
print(sum(outlet2))
print(sum(outlet3))
