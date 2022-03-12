'''
LC 138. Copy List with Random Pointer
'''


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        stemp = head
        
        result = Node(0)
        ttemp = result
        
        mapp = {} #maintain a map between source and target nodes (address)
        #check if the mapping already exist and use
        #if not create new node and maintain mapping
        
        while stemp:
            if stemp in mapp:
                ttemp.next = mapp[stemp]
            else:
                ttemp.next = Node(stemp.val)
                mapp[stemp] = ttemp.next
            ttemp = ttemp.next
            
            if stemp.random in mapp:
                ttemp.random = mapp[stemp.random]
            elif stemp.random:#only if random is not NULL
                ttemp.random = Node(stemp.random.val)
                mapp[stemp.random] = ttemp.random
            
            stemp = stemp.next
            
        return result.next