'''
LC 1143. Longest Common Subsequence
'''

class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        n1 = len(t1)
        n2 = len(t2)

        dp = [ [0 for j in range(n2+1)] for i in range(n1+1) ]

        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                if t1[i] == t2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        return dp[0][0]

s = Solution()
assert(s.longestCommonSubsequence("abcde","ace") == 3)
assert(s.longestCommonSubsequence("abc","abc") == 3)
assert(s.longestCommonSubsequence("abc","def") == 0)