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
        if head is None:
            return None
            
        l = g = None # define two pointer l for values less than x, g for values greater or equal than x
        l_start = g_start = None  # remember the start location of l and g
        cur = head
        
        while cur:
            if cur.val < x:
                if not l:
                    l = cur
                    l_start = l
                else:
                    l.next = cur
                    l = l.next
            else:
                if not g:
                    g = cur
                    g_start = cur
                else:
                    g.next = cur
                    g = g.next
            cur = cur.next

        if g:
            g.next = None
        if l:
            l.next = g_start
            return l_start
        else:
            return g_start