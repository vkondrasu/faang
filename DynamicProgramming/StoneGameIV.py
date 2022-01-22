'''
LC 1510 Stone Game IV
'''

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(maxsize=None)
        def dfs(remain):
            if remain == 0:
                return False
            
            sq_root = int(remain**0.5)
            
            for i in range(1, sq_root+1):
                if not dfs(remain - i*i):
                    return True
                
            return False
        
        return dfs(n)
        