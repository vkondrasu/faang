'''
LC 518. Coin Change 2
'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        def dfs(i, a):
            if a == amount:
                return 1
            if a > amount:
                return 0
            if i > n-1:
                return 0
            
            if (i,a) in dp:
                return dp[(i,a)]
            
            dp[(i,a)] = dfs(i, a+coins[i]) + dfs(i+1, a)
            
            return dp[(i,a)]
        
        n = len(coins)
        dp = {}
        return dfs(0,0)