"""
LC 144
"""


class Solution:
    """
    My Solution
    """
    def __init__(self):
        self.order = []
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(root):
            
            if root is None:
                return

            self.order.append(root.val)

            if root.left:
                self.preorderTraversal(root.left)

            if root.right:
                self.preorderTraversal(root.right)
                
        traverse(root)
        
        return self.order

    """ using stack data structure """

    def preorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        stack, output = [root,],[]
        
        while stack:
            at = stack.pop()
            if at:
                output.append(at.val)
                stack.append(at.right)
                stack.append(at.left)
                    
        return output

    """ Morris Travesrasl
    I am yet to understand this
    """

    def preorderMorrisTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node, output = root, []
        while node:  
            if not node.left: 
                output.append(node.val)
                node = node.right 
            else: 
                predecessor = node.left 

                while predecessor.right and predecessor.right is not node: 
                    predecessor = predecessor.right 

                if not predecessor.right:
                    output.append(node.val)
                    predecessor.right = node  
                    node = node.left  
                else:
                    predecessor.right = None
                    node = node.right         

        return output