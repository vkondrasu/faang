'''
LC 230. Kth Smallest Element in a BST
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def travesreInOrder(node):
            if node:
                travesreInOrder(node.left)
                inorder.append(node.val)
                if len(inorder) == k:
                    return
                travesreInOrder(node.right)
        
        inorder = [] 
        travesreInOrder(root)
        return inorder[k-1]
