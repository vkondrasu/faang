'''
LC 589. N-ary Tree Preorder Traversal
'''

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

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

    def preOrderRecursive(self, root):
        st, op = [root] , []

        while st:
            node = st.pop()
            op.append(node.val)
            st.extend(node.children[::-1])