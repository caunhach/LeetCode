class LinkedLists:
	def __init__(self, val=None):
		self.val = val
		self.next = None
	def Append(self, val):
		head = self
		while head.next:
			head = head.next
		head.next = LinkedLists(val)
	def AppendNode(self, node):
		head = self
		while head.next:
			head = head.next
		head.next = node
	def PrintLists(self):
		head = self
		while head:
			print(head.val, end=" ")
			head = head.next
		print("")
	def MergeTwoSortedLists(self, link2):
		Sorted_List = None
		link1 = self
		tmp = None
		if not link2:
			return link1
		if not link1:
			return link2
		while link1 or link2:
			if (link1 and not link2) or (link1 and link2 and link1.val <= link2.val):
				tmp = link1
				link1 = link1.next
				tmp.next = None
				if not Sorted_List:
					Sorted_List = tmp
				else:
					Sorted_List.AppendNode(tmp)
			elif (not link1 and link2) or (link1 and link2 and link2.val < link1.val):
				tmp = link2
				link2 = link2.next
				tmp.next = None
				if not Sorted_List:
					Sorted_List = tmp
				else:
					Sorted_List.AppendNode(tmp)
		return Sorted_List
			
link1 = LinkedLists(1)
link1.Append(2)
link1.Append(4)
# link1.PrintLists()
link2 = LinkedLists(1)
link2.Append(3)
link2.Append(7)
# link2.PrintLists()
link3 = link1.MergeTwoSortedLists(link2)
link3.PrintLists()
link5 = link1.MergeTwoSortedLists(None)
link5.PrintLists()
		