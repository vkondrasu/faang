'''
LC 589. N-ary Tree Preorder Traversal
'''

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.result = []
        def traversePre(root):
            if not root:
                return
            self.result.append(root.val)
            for child in root.children:
                traversePre(child)
                
        traversePre(root)
        return self.result