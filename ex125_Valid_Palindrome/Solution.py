def ValidPalindrome(str):
	i = 0
	j = len(str) - 1
	while i < j:
		while not str[i].isalpha():
			i += 1
		while not str[j].isalpha():
			j -= 1
		if str[i].isalpha and str[j].isalpha():
			if str[i].lower() != str[j].lower():
				return False
			i += 1
			j -= 1
	return True

s = "A man, a plan, a canal: Panama"
print(ValidPalindrome(s))
s = "race a car"
print(ValidPalindrome(s))
s = " "
print(ValidPalindrome(s))