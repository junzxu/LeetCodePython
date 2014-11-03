# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
    	if head is None:
    		return head
    	pre = head
    	cur = head.next
    	while cur:
    		if cur.val == pre.val:
    			cur = cur.next
    			pre.next = cur
    		else:
    			pre = cur
    			cur = cur.next
    	return head