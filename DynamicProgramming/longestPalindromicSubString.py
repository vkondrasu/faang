'''
LC 5. Longest Palindromic Substring
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        palLen = 0
        pal = ""
        for i in range(n):
            l,r = i, i
            
            while l >= 0 and r < n and s[l] == s[r]:
                
                if (r-l+1) > palLen:
                    palLen = (r-l+1)
                    pal = s[l:r+1]
                    
                l -= 1
                r += 1
            
            
            l, r = i, i+1
            
            while l >= 0 and r < n and s[l] == s[r]:
                if (r-l+1) > palLen:
                    palLen = (r-l+1)
                    pal = s[l:r+1]
                    
                l -= 1
                r += 1
            
        return pal