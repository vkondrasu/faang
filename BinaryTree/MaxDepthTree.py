class Solution:
    def depthOfTree(self, root, cur_depth):
        if root.left is None and root.left is None:
            self.answer = max(self.answer, cur_depth)
            
        if root.left:
            self.depthOfTree(root.left, cur_depth+1)
            
        if root.right:
            self.depthOfTree(root.right, cur_depth+1)
            
    def maxDepthDFS(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        self.answer = 0
        
        self.depthOfTree(root, 1)
        
        return self.answer

    def maxDepthBFS(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        depth = 0
        q = deque()
        q.append(root)
        
        while len(q) > 0:
            
            depth += 1
            size = len(q)
            
            for i in range(size):
                at = q.popleft()
                if at.left: q.append(at.left)
                if at.right: q.append(at.right)
                
        return depth