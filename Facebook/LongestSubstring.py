import sys

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0]*128
        
        right = left = result = 0
        
        n = len(s)
        
        while right < n:
            r = s[right]
            chars[ord(r)] += 1
            
            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1
                
            result = max(result, right-left+1)
            right += 1
            
        return result

s = Solution()
print(s.lengthOfLongestSubstring(sys.argv[1]))
