'''
LC 1100. Find K-Length Substrings With No Repeated Characters
'''
class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        count = 0
        mapp = Counter(s[0:k])
        l = 0
        if len(mapp) == k:
            count += 1
        for i in range(k,len(s)):
            mapp[s[l]] -= 1
            
            if mapp[s[l]] == 0:
                del mapp[s[l]]
            l += 1
                
            mapp[s[i]] = mapp.get(s[i], 0) + 1
            
            if len(mapp) == k:
                count += 1
                
        return count