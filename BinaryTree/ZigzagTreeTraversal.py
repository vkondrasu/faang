class Solution:
    def levelOrderZigzag(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []
        q = deque()
        q.append(root)
        
        output = []
        temp_output = []
        
        flip = False
        
        while len(q) > 0:
            size = len(q)
            
            for i in range(size):
                at = q.popleft()
                
                temp_output.append(at.val)
                if at.left: q.append(at.left)
                if at.right: q.append(at.right)
                    
            if flip:
                temp_output.reverse()
                flip = False
            else:
                flip = True
                    
            output.append(temp_output)
            temp_output = []
            
        return output