'''
LC 1305. All Elements in Two Binary Search Trees
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.list1 = []
        self.list2 = []
        def printTree(root, lst):
            if not root:
                return
            printTree(root.left, lst)
            lst.append(root.val)
            printTree(root.right, lst)
        #time O(n) space O(n)   
        printTree(root1, self.list1)
        printTree(root2, self.list2)
        
        #time O(n1+n2) space O(n1+n2)
        def mergeLists(list1, list2):
            result = []
            
            i = j = 0
            n1 = len(list1)
            n2 = len(list2)
            
            while i < n1 and j < n2:
                if list1[i] <= list2[j]:
                    result.append(list1[i])
                    i += 1
                else:
                    result.append(list2[j])
                    j += 1
                    
            while i < n1:
                result.append(list1[i])
                i += 1
                
            while j < n2:
                result.append(list2[j])
                j += 1
                
            return result
                
            
        
        return mergeLists(self.list1, self.list2)
        '''
    
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stack1, stack2, output = [], [], []
        
        while root1 or root2 or stack1 or stack2:
            # update both stacks
            # by going left till possible
            while root1:
                stack1.append(root1)
                root1 = root1.left
            while root2:
                stack2.append(root2)
                root2 = root2.left

            # Add the smallest value into output,
            # pop it from the stack,
            # and then do one step right
            if not stack2 or stack1 and stack1[-1].val <= stack2[-1].val:
                root1 = stack1.pop()
                output.append(root1.val)
                root1 = root1.right
            else:
                root2 = stack2.pop()
                output.append(root2.val)   
                root2 = root2.right

        return output