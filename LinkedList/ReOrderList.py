"""
LC 143
"""

class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        
        """
        
        q = deque()
        
        temp = head
        count = 1
        
        if temp.next is None: #only one element
            return head
        
        temp = temp.next
        count += 1
        
        while temp.next:
            q.append(temp.next)
            count += 1
            
            if len(q) > count//2:
                q.popleft()
                
            temp = temp.next
                
        if len(q) > 0:
            temp = head
                
        for i in range(len(q)):
            item = q.pop()
            item.next = temp.next
            temp.next = item
            
            temp = temp.next.next
            
        temp.next = None


    def reorderListSolution(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        
        """
        
        #find middle point
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #reverse the list   
        prev, curr = None, slow
        while curr:
            tmp = curr.next

            curr.next = prev
            prev = curr
            curr = tmp
            
        #merge list
        first, second = head, prev
        while second.next:
            tmp = first.next
            first.next = second
            first = tmp

            tmp = second.next
            second.next = first
            second = tmp