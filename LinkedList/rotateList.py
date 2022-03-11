'''
LC 61. Rotate List
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head:
            return head #nothing to do
        
        n = 0
        temp = head
        
        #get length of list
        while temp:
            temp = temp.next
            n += 1
        #get proper value of k   
        k = k%n
        
        #may be we don't need to rotate
        if k == 0:
            return head
        
        count = 1
        temp = head
        #move to node -- after this node next nodes will go to start
        while count < n-k:
            temp = temp.next
            count += 1
         
        #make new Head at this point
        newHead = temp.next
        #end the list
        temp.next = None
        temp = newHead
        
        #travel to the end
        while temp.next:
            temp = temp.next
        #attach old head here  
        temp.next = head
        
        return newHead