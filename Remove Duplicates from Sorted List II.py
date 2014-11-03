# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
    	if not head:
    		return None
    	start = ListNode(0)
    	start.next = head
    	pre = start
    	cur = head
    	while cur and cur.next:
    		if cur.next.val != cur.val:
    			pre = cur
    			cur = cur.next
    		else:
    			tmp = cur.next
    			while tmp and tmp.val == cur.val:
    				tmp = tmp.next
    			cur = tmp
    			pre.next = cur
    	return start.next