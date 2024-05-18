def MostWater(height):
	i = 0
	j = len(height) - 1
	_max = min(height[i], height[j]) * (len(height) - 1)
	while i < j:
		_max = max(_max, min(height[i], height[j]) * (j - i))
		if height[i] >= height[j]:
			j -= 1
		elif height[i] <= height[j]:
			i += 1
	return _max

height = [1,8,6,2,5,4,8,3,7]
print(MostWater(height))
height = [1,1]
print(MostWater(height))
height = [1,8,6,102,1055,200,8,103,7]
print(MostWater(height))