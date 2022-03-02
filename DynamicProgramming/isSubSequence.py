'''
LC 392. Is Subsequence
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ns = len(s)
        nt = len(t)
        dp = [ [0 for j in range(nt+1)]for i in range(ns+1)]
        
        for i in range(ns-1, -1, -1):
            for j in range(nt-1,-1,-1):
                if s[i] == t[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
                    
        return dp[0][0] == ns