# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if not head:
            return None
        pre = ListNode(0)
        pre.next = self.swapPair(head)
        return pre.next
    
    def swapPair(self,start):
        if start == None:
            return None
        elif start.next == None:
            return start
        else:
            next_next = start.next.next
            new_start = start.next
            new_start.next = start
            start.next = self.swapPair(next_next)
            return new_start