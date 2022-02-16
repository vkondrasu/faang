'''
LC 24. Swap Nodes in Pairs
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def swap(head):
        
            if head is None or head.next is None:
                return head
            cur = head
            nextt = head.next
            remain = nextt.next
            
            temp  = cur
            head = nextt
            head.next = cur
            cur.next = swap(remain)
            return head
        
        return swap(head)