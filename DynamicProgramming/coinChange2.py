'''
LC 518. Coin Change 2
'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''
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
        '''
        dp = [0] * (amount + 1)
        dp[0] = 1 #if we have reached 0 then that is 1 way
        
        for coin in coins:
            for x in range(coin, amount + 1):
                #no.of ways x can be summed is all the ways
                #x-coin can be summed
                dp[x] += dp[x - coin]
        return dp[amount]