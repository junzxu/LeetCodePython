# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        #divide and conquer
        l = len(lists) 
        l1 = self.mergeKLists(lists[:l/2])
        l2 = self.mergeKLists(lists[l/2:])
        
        return self.mergeTwo(l1,l2)
    
    def mergeTwo(self, a, b):
        if a == None or b == None:
            return a if b==None else b
        elif a == None and b == None:
            return None
            
        start = a
        if a.val<b.val:
            a = a.next
        else:
            start = b
            b = b.next
            
        head = start
        while a and b:
            if a.val < b.val:
                head.next = a
                head = a
                a = a.next
            else:
                head.next = b
                head = b
                b = b.next
        while a:
            head.next = a
            head = a
            a = a.next
        while b:
            head.next = b
            head = b
            b = b.next
        
        return start