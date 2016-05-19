# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
	if not head or not head.next: return head

	newHead = head.next

	head.next = self.swapPairs(newHead.next)
	newHead.next = head

	return newHead
