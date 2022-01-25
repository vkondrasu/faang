'''
LC 404. Sum of Left Leaves
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.summ = 0
        
        def getSum(root):
            if not root:
                return
            if root.left:
                #add only leaf left nodes
                if root.left.left is None and root.left.right is None:
                    self.summ += root.left.val
                else:
                    getSum(root.left)
                
            if root.right:
                getSum(root.right)
                
        getSum(root)
        
        return self.summ