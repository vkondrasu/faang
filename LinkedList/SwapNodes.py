'''
LC 1721. Swapping Nodes in a Linked List
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        front, back = None, None
        temp, count = head, 0
        
        while temp:
            count += 1
            
            if back:
                back = back.next
            if count == k:
                front = temp
                back = head
                
            temp = temp.next
            
        temp = front.val
        front.val = back.val
        back.val = temp
        
        return head