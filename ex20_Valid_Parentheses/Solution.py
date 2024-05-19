from collections import deque

def ValidParentheses(s):
	parentheses = dict({")" : "(", "}" : "{", "]" : "["})
	stack = deque()
	i = 0
	while i < len(s):
		if s[i] == "(" or s[i] == "{" or s[i] == "[":
			stack.append(s[i])
		elif s[i] in parentheses and len(stack) != 0 and stack[-1] == parentheses[s[i]]:
			stack.pop()
		else:
			stack.append(s[i])
		i += 1
	if len(stack) != 0:
		return False
	return True

s = "(){}[]"
print(ValidParentheses(s))
s = "(]"
print(ValidParentheses(s))
s = "()"
print(ValidParentheses(s))