'''
LC 148. Sort List
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        '''
        #Time Limit Exceeded
        #TC: O(n**2) algo 
        #SC: O(1) -- no additional space
        def insertIntoList(head, node):
            if head is None:
                return node
            if head.next is None:
                if head.val <= node.val:
                    head.next = node
                    return head
                else:
                    node.next = head
                    return node
            
            if node.val >= head.val and node.val <= head.next.val:
                node.next = head.next
                head.next = node
                return head
            else:
                insertIntoList(head.next, node)
                return head
        
        def sortSubList(head, prev):
            if head is None:
                return None
            if head.next is None:
                return head
            subHead = sortSubList(head.next, head)
            if head.val <= subHead.val:
                head.next = subHead
                return head
            else:
                if prev:
                    prev.next = subHead
                head.next = None
                return insertIntoList(subHead, head)
            
        return sortSubList(head, None)
        
        '''
        
        if not head or not head.next: return head
        
        def getSize(head):
            # Simply count the length of linked list
            counter = 0
            while head:
                counter +=1
                head = head.next
            return counter
        
        def split(head, size):
            # given the head & size, return the the start node of next chunk
            for i in range(size-1): 
                if not head: 
                    break 
                head = head.next

            if not head: return None
            next_start, head.next = head.next, None  #disconnect
            
            return next_start
        
        def merge(l1, l2, dummy_start):
            # Given dummy_start, merge two lists, and return the tail of merged list
            curr = dummy_start
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next, l1 = l1, l1.next
                else:
                    curr.next, l2 = l2, l2.next
                curr = curr.next
            
            curr.next = l1 if l1 else l2
            while curr.next: curr = curr.next  # Find tail
            # the returned tail should be the "dummy_start" node of next chunk
            return curr  

        total_length = getSize(head)
        dummy = ListNode(0)
        dummy.next = head
        start, dummy_start, size = None, None, 1
        
        while size < total_length:
            dummy_start = dummy
            start = dummy.next 
            while start:
                left = start
                right = split(left, size) # start from left, cut with size=size
                start = split(right, size) # start from right, cut with size=size
                dummy_start = merge(left, right, dummy_start)  # returned tail = next dummy_start 
            size *= 2
        return dummy.next