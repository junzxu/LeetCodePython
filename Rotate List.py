# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
    	if not head or k == 0: return head
    	newHead = tail = head #newHead is the new head after rotation, tail is the last node before rotation
    	while k > 1:
    		tail = tail.next
    		k -= 1
    		if tail == None:
                #k might be larger than list size
    			newHead = tail = head
    	while tail.next:
            #move tail to the last node
    		tail = tail.next
    		if not tail.next:
    			newEnd = newHead
    			newHead = newHead.next
    			newEnd.next = None
    		else: newHead = newHead.next
    	if newHead != head: tail.next = head
    	return newHead