def Candy(ratings):
	candy = 1
	amounts = 0
	for i in range(len(ratings)):
		if i == 0:
			if len(ratings) < 2 or ratings[0] <= ratings[1]:
				candy = 1
			elif ratings[0] > ratings[1]:
				candy = 2
		elif ratings[i] > ratings[i - 1]:
			candy += 1
		elif ratings[i] <= ratings[i - 1]:
			candy = 1
		amounts += candy
	return amounts
ratings = [1,0,2]
print(Candy(ratings))
ratings = [1,2,2]
print(Candy(ratings))
ratings = [4,2,3,3,3,3,4,5,4]
print(Candy(ratings))