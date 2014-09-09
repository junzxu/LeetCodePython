# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head is None:
            return head
        baseNode = ListNode(0)
        baseNode.next = head
        cur = head
        while cur.next:
            if cur.next.val >= cur.val:
                cur = cur.next
            else:
                node = baseNode
                while node.next.val <= cur.next.val:
                    node = node.next
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = node.next
                node.next = tmp
        return baseNode.next