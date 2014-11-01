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
        if head is None or k <= 0: return head
        new_head = head
        count = k-1
        while new_head and count > 0:
            new_head = new_head.next
            count -= 1
        if count != 0 or new_head == None:
            return head
        pre = self.reverseKGroup(new_head.next, k)
        cur = head
        while pre != new_head:
            new_cur = cur.next
            cur.next = pre
            pre = cur
            cur = new_cur
        return new_head