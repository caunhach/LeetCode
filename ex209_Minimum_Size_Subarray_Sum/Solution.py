def MinimumSubarray(nums, target):
	i = 0
	j = 0
	sum = nums[0]
	Min = 0
	while j < len(nums):
		if sum == target:
			if Min == 0:
				Min = j - i + 1
				# print(Min)
				# print("i :", i)
				# print("j :", j)
			else:
				Min = min(j - i + 1, Min)
			j += 1
			if j < len(nums):
				sum += nums[j]
		elif sum < target:
			j += 1
			if j < len(nums):
				sum += nums[j]
		elif sum > target and i < j:
			sum -= nums[i]
			i += 1
		elif sum > target and i == j:
			j += 1
			if j < len(nums):
				sum += nums[j]
	return Min

target = 7
nums = [2, 3, 1, 2, 4, 3]
print(MinimumSubarray(nums, target))
target = 4
nums = [1, 4, 4]
print(MinimumSubarray(nums, target))
target = 11
nums = [1, 1, 1, 100, 4, 7, 1, 1]
print(MinimumSubarray(nums, target))