def RemoveDuplicate(list):
	flag = False
	j = 0
	for i in range(len(list)):
		if j == 0:
			j += 1
		elif flag == False and list[i] == list[i - 1]:
			flag = True
			j += 1
		elif list[i] != list[i - 1]:
			flag = False
			j += 1
		elif flag == True and list[i] != list[i - 1]:
			j += 1
		list[j - 1] = list[i]
	return j

list = [1,1,1,2,2,3,3,3,3,5]
k = RemoveDuplicate(list)
print(k)
print(list[:k])