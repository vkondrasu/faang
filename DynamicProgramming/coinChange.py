'''
LC 322. Coin Change
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        mem = {}
        def getCoins(val):
            if val in mem:
                return mem[val]
            if val < 0:
                return math.inf
            if val == 0:
                return 0
            if val in coins:
                return 1
            
            min_coins = math.inf
            for coin in coins:
                min_coins =  min(min_coins, 1+ getCoins(val-coin))
            mem[val] = min_coins  
            return mem[val]
             
        answer = getCoins(amount)
        return -1 if answer == math.inf else answer
        '''
        
        dp = [math.inf] * (amount+1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] = min(dp[x], dp[x-coin] + 1)
                
        return dp[amount] if dp[amount] != math.inf else -1
        