'''
LC 91. Decode Ways
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        mem = {}
        
        def subDecode(i):
            if i == n:
                return 1
            if s[i] == '0':
                return 0
            if i == n-1:
                return 1
            if i in mem:
                return mem[i]
            
            ans = subDecode(i+1)
            if int(s[i:i+2]) <= 26:
                ans += subDecode(i+2)
            mem[i] = ans
            
            return ans
        return subDecode(0)