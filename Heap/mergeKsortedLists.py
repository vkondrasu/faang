'''
LC 23. Merge k Sorted Lists
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0) # a dummy value
        
        q = PriorityQueue()
        
        for l in lists:
            if l:
                q.put((l.val, l))
                
        while not q.empty():
            value, node = q.get()
            #add to result
            point.next = ListNode(value)
            point = point.next
            
            #get next node
            node = node.next
            
            if node:
                q.put((node.val, node))
                
        return head.next # head poits to a dummy value
        