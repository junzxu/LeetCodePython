# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if k <= 0:
            return head
        pre = ListNode(0)
        pre.next = self.reverseK(head,k)
        return pre.next
    
    def reverseK(self, start, k):
        #reverse next k nodes and return the beginning of reversed list
        count = k-1
        end = start
        while count>0 and end:
            end = end.next
            count -= 1
        if end == None:
            return start
            
        pre = start
        cur = start.next
        start.next = self.reverseK(end.next, k)
        for i in range(0,k-1):
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return end
            