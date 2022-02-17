'''
LC 39. Combination Sum
'''
from collections import deque
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        dp = [math.inf] * (amount+1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] = min(dp[x], dp[x-coin] + 1)
                
        return dp[amount] if dp[amount] != math.inf else -1
        '''
        q = deque()
        for candidate in candidates:
            q.append((candidate, [candidate]))
            
        result = []
        while q:
            cur, pre = q.popleft()
            if cur == target:
                pre.sort()
                if pre not in result:
                    result.append(pre)
                continue
            for candidate in candidates:
                if cur + candidate <= target:
                    q.append((cur+candidate, pre + [candidate]))
                    
        return result
        