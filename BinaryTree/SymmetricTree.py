class Solution:
    def isMatch(self, node1, node2):
        #if both are None then that is a match and we can return
        if node1 is None and node2 is None:
            return True
        
        #to compare further we need to make sure both of them are not None
        if node1 and node2:
            """
            When comparing 2 trees,
            1. root values has to match
            2. first tree left and second tree right subtrees need to match
            3. first tree right and second tree left subtrees need to match
            """
            return (node1.val == node2.val) and self.isMatch(node1.left, node2.right) and self.isMatch(node1.right, node2.left)
        #if anyone is a None then it's not a match we can return with False
        else:
            return False
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #empty tree is a symmetric tree
        if root is None:
            return True
        #left tree has to match with right tree
        return self.isMatch(root.left, root.right)