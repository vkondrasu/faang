'''
LC 242. Valid Anagram
'''
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_counter = Counter(s)
        t_counter = Counter(t)
        
        
        
        for c in s_counter:
            if s_counter[c] != t_counter[c]:
                return False
        return True