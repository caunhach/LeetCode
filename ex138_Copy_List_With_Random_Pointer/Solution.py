class Nodes:
	def __init__(self, data=None):
		self.data = data
		self.next = None
		self.random = None
	def PrintLists(self):
		head = self
		while head:
			print("self: ", head.data, end=" ")
			if head.random:
				print("random: ", head.random.data)
			else:
				print("random: ", None)
			head = head.next
	def Append(self, data):
		head = self
		while head.next:
			head = head.next
		head.next = Nodes(data)
	def CopyLists(self, list1):
		list2 = None
		tmp = list1
		head = list1
		tmp2 = None
		head2 = None
		while list1:
			if not list2:
				list2 = Nodes(list1.data)
				head2 = list2
				tmp2 = list2
			else:
				list2.Append(list1.data)
			list1 = list1.next
		# list2.PrintLists()
		list1 = head
		# list1.PrintLists()
		while list1:
			tmp = head
			tmp2 = head2
			while tmp and tmp2 and tmp != list1.random:
				tmp = tmp.next
				tmp2 = tmp2.next
			list2.random = tmp2
			# if tmp2:
			# 	print(tmp2.data)
			list1 = list1.next
			list2 = list2.next
		# head2.PrintLists()
		return head2


list1 = Nodes(7)
list1.Append(13)
list1.Append(11)
list1.Append(10)
list1.Append(1)
tmp = list1.next.next.next.next.next
list1.random = tmp
tmp = list1
list1.next.random = tmp
tmp = list1.next.next.next.next
list1.next.next.random = tmp
tmp = list1.next.next
list1.next.next.next.random = tmp
tmp = list1
list1.next.next.next.next.random = tmp
# list1.PrintLists()
list2 = Nodes()
list2 = list2.CopyLists(list1)
list2.PrintLists()