'''
LC 173. Binary Search Tree Iterator
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        self.arr = inorder(root)
        self.position = -1
        self.n = len(self.arr)
        

    def next(self) -> int:
        self.position += 1
        return self.arr[self.position]
        

    def hasNext(self) -> bool:
        return self.position < self.n-1
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()