# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
# @param two ListNodes
# @return a ListNode
	def mergeTwoLists(self, l1, l2):
		head = ListNode(0)
		node = head
		while l1 and l2:
			if l1.val <= l2.val:
				node.next = l1
				node = l1
				l1 = l1.next
			else:
				node.next = l2
				node = l2
				l2 = l2.next

		while l1:
			node.next = l1
			node = node.next
			l1 = l1.next

		while l2:
			node.next = l2
			node = node.next
			l2 = l2.next

		return head.next