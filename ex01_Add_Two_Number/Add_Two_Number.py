from typing import Optional

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		carry = 0
		ans = None
		while l1 != None or l2 != None or carry != 0 :
			l1val = l1.val if l1 else 0
			l1 = l1.next if l1 else None
			l2val = l2.val if l2 else 0
			l2 = l2.next if l2 else None
			sum = l1val + l2val + carry
			carry = sum // 10
			tmp = ListNode(sum % 10)
			if ans:
				ans.next = tmp
			else:
				ans = tmp
			ans = ans.next

l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next = ListNode(9)
l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)
s = Solution()
s.addTwoNumbers(l1, l2)