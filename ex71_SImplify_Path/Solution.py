from collections import deque

def PrintPath(simple_path):
	str = ""
	if len(simple_path) == 0:
		str = "/"
	while len(simple_path) > 0:
		str = str + "/" + simple_path[0]
		simple_path.popleft()
	print(str)

def SimplifyPath(path):
	simple_path = deque()
	i = 0
	j = 0
	while j < len(path):
		i = j
		j += 1
		tmp = ""
		if i < len(path) and j < len(path) and path[i] == "/" and path[j] == "/":
			i = j
		while j < len(path) and path[j] != "/":
			j +=1
		if i + 1 < len(path):
			tmp = path[i + 1: j]
		if tmp == "..":
			if len(simple_path) > 0:
				simple_path.pop()
		elif tmp == "." or tmp == "":
			continue
		else:
			simple_path.append(tmp)
	PrintPath(simple_path)

path = "/home/user/Documents/.././/Pictures/."
SimplifyPath(path)
path = "/.../a/../b/c/../d/./"
SimplifyPath(path)
path = "/home//foo/"
SimplifyPath(path)
path = "/../"
SimplifyPath(path)