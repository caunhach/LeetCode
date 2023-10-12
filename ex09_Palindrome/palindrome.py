class solution:
	def isPalindrome(self, x: int) ->bool:
		if (x < 0 or x % 10 == 0):
				return False
		right = 0
		while True:
			right = right * 10 + x % 10
			if right == x or right == x // 10:
				return True
			x = x // 10
			if right > x:
				return False
s = solution()
print("Palindrome") if s.isPalindrome(4785874) else print("Not Palindrome")