def Anagrams(strs):
	info = dict()
	for words in strs:
		a = ''.join(sorted(words))
		if not a in info:
			info[a] = [words]
		else:
			info[a].append(words)
	ans = list()
	for e in info:
		ans.append(info[e])
	return ans
			
strs = ["eat","tea","tan","ate","nat","bat"]
print(Anagrams(strs))

strs = ["a"]
print(Anagrams(strs))

strs = ["eat","tea","tan","ate","nat","bat", "sexy", "yesx"]
print(Anagrams(strs))