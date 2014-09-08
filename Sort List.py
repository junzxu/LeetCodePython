# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if head == None:
            return None
        tmp = []
        current = head
        while current != None:
            tmp.append(current.val)
            current = current.next
        tmp.sort()
        current = head
        for i in range(0,len(tmp)):
            current.val = tmp[i]
            current = current.next
        return head