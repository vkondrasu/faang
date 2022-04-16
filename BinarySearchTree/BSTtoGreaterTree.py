'''
LC 538. Convert BST to Greater Tree
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #inorder traversal -- sorted array -- sum from right side
        #construct array again
        
        inorder = []
        
        def traverseInOrder(root):
            if not root:
                return
            traverseInOrder(root.left)
            inorder.append([root, root.val])
            traverseInOrder(root.right)
            
        traverseInOrder(root)
        
        n = len(inorder)
        
        if n == 0:
            return root
        
        mapp = {}
        
        mapp[inorder[n-1][0]] = inorder[n-1][1]
        
        for i in range(n-2,-1,-1):
            inorder[i][1] += inorder[i+1][1]
            mapp[inorder[i][0]] = inorder[i][1]
            
        def updateTree(root):
            if not root:
                return
            root.val = mapp[root]
            updateTree(root.left)
            updateTree(root.right)
            
        updateTree(root)
            
        return root
            
