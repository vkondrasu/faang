'''
LC 1586. Binary Search Tree Iterator II
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
        self.n = len(self.arr)
        self.pointer = -1
        

    def hasNext(self) -> bool:
        return self.pointer < self.n-1
        

    def next(self) -> int:
        self.pointer += 1
        return self.arr[self.pointer]
        

    def hasPrev(self) -> bool:
        return self.pointer > 0
        

    def prev(self) -> int:
        self.pointer -= 1
        return self.arr[self.pointer]
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()