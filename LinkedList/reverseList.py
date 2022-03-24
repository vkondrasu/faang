'''
LC 206. Reverse Linked List
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        temp = head
        if temp:
            nexxt = temp.next
        
        while temp:
            temp.next = prev
            prev = temp
            temp = nexxt
            if temp:
                nexxt = temp.next
            
        return prev