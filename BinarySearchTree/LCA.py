'''
LC 235. Lowest Common Ancestor of a Binary Search Tree
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def LCA(root, p, q):
        
            if root in [p,q]:
                return root
            if p.val < root.val and q.val < root.val:
                return LCA(root.left, p, q)
            if p.val > root.val and q.val > root.val:
                return LCA(root.right, p, q)
            return root
        
        return LCA(root, p, q)