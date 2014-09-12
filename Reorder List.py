# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head == None or head.next == None:
            return
        start = head #use two pointer to get middle point of the LinkList
        end = head
        while end.next and end.next.next:
            start = start.next
            end = end.next.next
            
        m = start.next #head of the second half
        start.next = None
        start = head
        mid = self.reverseList(m) #reverse the second half of the LinkList
        
        #merge two link list
        while mid:
            newStart = start.next
            newMid = mid.next
            start.next = mid
            mid.next = newStart
            start = newStart
            mid = newMid
    
    #reverse the link list      
    def reverseList(self,head):
        cur = head
        pre = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre