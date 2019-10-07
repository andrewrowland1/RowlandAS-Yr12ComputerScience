i = 0
j = 0
list1 = [2,5,15,36,47,56,59,78,156,244,268]
list2 = [18,39,42,43,66,69,100]
mergeList = []

while ((i < len(list1)) and (j < len(list2))):
	if list1[i] < list2[j]:
		mergeList.append(list1[i])
		i = i + 1
	else: 
		mergeList.append(list2[j])
		j = j + 1
	#endif
#endwhile
while i < len(list1):
	mergeList.append(list1[i])
	i = i + 1
#endwhile
while j < len(list2):
	mergeList.append(list2[j])
	j = j + 1
#endwhile
print(mergeList)
