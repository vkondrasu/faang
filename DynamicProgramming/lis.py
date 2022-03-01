'''
LC 300. Longest Increasing Subsequence
'''

class Solution:
    def longestIncreasingSubsequence(self, nums):
        n =  len(nums)
        LIS = [1] * n

        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)

s = Solution()
assert(s.longestIncreasingSubsequence([10,9,2,5,3,7,101,18]) == 4)
assert(s.longestIncreasingSubsequence([0,1,0,3,2,3]) == 4)
assert(s.longestIncreasingSubsequence([7,7,7,7,7,7,7]) == 1)