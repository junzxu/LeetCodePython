# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: #two pointer meet at somewhere in the cycle
                cycle = head
                while cycle != fast: #cycle and fast pointer should meet at the begining of cycle
                    cycle = cycle.next
                    fast = fast.next
                return cycle
        return None