# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        Map = {} #store visited node by its label
        if head is None:
            return head
        new = RandomListNode(head.label)
        Map[head.label] = new
        newhead = new
        cur = head
        while cur.next:
            next = RandomListNode(cur.next.label)
            new.next = next
            Map[cur.next.label] = next
            cur = cur.next
            new = new.next
        cur = head
        new = newhead
        #point each node to its random node
        while cur:
            if cur.random != None:
                label = cur.random.label
                tmp = Map[label]
                new.random = tmp
            new = new.next
            cur = cur.next
        return newhead