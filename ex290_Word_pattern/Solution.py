def WordPattern(s, pattern):
	word = dict()
	i0 = 0
	i = 0
	j = 0
	while j < len(s):
		j = i
		while j < len(s) and s[j] != " ":
			j +=1
		if not pattern[i0] in word:
			word[pattern[i0]] = s[i:j]
		else:
			if word[pattern[i0]] != s[i:j]:
				return False
		i0 += 1
		i = j
		while i < len(s) and s[i] == " ":
			i += 1
	return True

pattern = "abba"
s = "dog cat cat dog"

print(WordPattern(s, pattern))

pattern = "abba"
s = "dog cat cat fish"

print(WordPattern(s, pattern))

pattern = "aaaa"
s = "dog cat cat dog"

print(WordPattern(s, pattern))

pattern = "abca"
s = "dog cat bird dog"

print(WordPattern(s, pattern))