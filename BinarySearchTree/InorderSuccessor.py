# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

""" LC 285 """


class Solution:
    """
    My Solution
    """
    def __init__(self):
        self.found = False
        self.result = None
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> TreeNode:
        
        if root is None:
            return
        
        if root.left:
            self.inorderSuccessor(root.left, p)
            
        if self.result is None and self.found :
            self.result = root
        
        if root == p:
            self.found = True
        
        if root.right:
            self.inorderSuccessor(root.right, p)
            
        return self.result

    """ LC solution """

