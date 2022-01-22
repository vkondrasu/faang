'''
LC 1602. Find Nearest Right Node in Binary Tree
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        q = deque()
        
        q.append(root)
        
        while q:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                
                if cur == u:
                    if i < size-1:
                        return q.popleft()
                    else:
                        return None
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                    
        return None