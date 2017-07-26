# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        lessHead = ListNode(0)
        greaterHead = ListNode(0)
        less = lessHead
        great = greaterHead
        cur = head
        while cur:
            if cur.val < x:
                less.next = cur
                less = less.next
            else:
                great.next = cur
                great = great.next
            cur = cur.next
        
        less.next = greaterHead.next
        great.next = None
        return lessHead.next
