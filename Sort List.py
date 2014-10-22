# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self,head):
        if not head:
            return None
        head = self.sort(head)
        return head
        
    def sort(self,head):
        #given a head node, split it into two part and sort them recursively, finally merge them
        if head.next == None:
            #when the list has only one node
            return head
        slow = fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        mid = head.next
        if slow.next != None:
            mid = slow.next
            slow.next = None
        else:
            #only two nodes in the list
            head.next = None
        l = self.sort(head)
        r = self.sort(mid)
        
        #merge two sorted list
        start = l if l.val < r.val else r
        if l.val < r.val:
            l = l.next
        else:
            r = r.next
        cur = start
        while l and r:
            if l.val < r.val:
                cur.next = l
                cur = cur.next
                l = l.next
            else:
                cur.next = r
                cur = cur.next
                r = r.next
        while l:
            cur.next = l
            cur = cur.next
            l = l.next
        while r:
            cur.next = r
            cur = cur.next
            r = r.next
            
        return start
        