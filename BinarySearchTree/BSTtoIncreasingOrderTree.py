'''
LC 897. Increasing Order Search Tree
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        inorder = []
        
        def traverseInOrder(node):
            if not node:
                return
            traverseInOrder(node.left)
            inorder.append(node)
            traverseInOrder(node.right)
            
        traverseInOrder(root)
        
        n = len(inorder)
        for i in range(n-1):
            inorder[i].left = None
            inorder[i].right = inorder[i+1]
            
        inorder[n-1].left = None
        inorder[n-1].right = None
        
        return inorder[0]
