'''
LC 669. Trim a Binary Search Tree
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def trimTree(root, parent, low, high):
            if root is None:
                return
            if root.val < low:
                parent.left = root.right
                trimTree(parent.left, parent, low, high)
            if root.val > high:
                parent.right = root.left
                trimTree(parent.right, parent, low, high)
                
            trimTree(root.left, root, low, high)
            trimTree(root.right, root, low, high)
        
        while root and (root.val < low or root.val > high):
            if root.val < low:
                root = root.right
            else:
                root = root.left
        if root:    
            trimTree(root.left, root, low, high)
            trimTree(root.right, root, low, high)
        
        return root
