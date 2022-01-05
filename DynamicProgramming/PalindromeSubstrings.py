#https://leetcode.com/problems/palindrome-partitioning/discuss/1667786/Python-Simple-Recursion-oror-Detailed-Explanation-oror-Easy-to-Understand

#LC 131

class Solution:
    def partition(self, s: str):
        if not s: return [[]]
        ans = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:  # prefix is a palindrome
                for suf in self.partition(s[i:]):  # process suffix recursively
                    ans.append([s[:i]] + suf)
        return ans