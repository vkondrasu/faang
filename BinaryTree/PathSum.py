"""
LC 112
easy
"""

class Solution:
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root is None:
            return False
        
        #root-to-leaf sum
        #if target sum is at a node that is a leaf then only it's True
        if targetSum == root.val:
            if root.left is None and root.right is None :
                return True
        
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)