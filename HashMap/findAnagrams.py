'''
LC 438. Find All Anagrams in a String
'''
from collections import Counter 
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        mapp = Counter(p)
        maps = Counter(s[0:len(p)])
        
        #print(mapp)
        #print(maps)
        
        result = [0] if mapp == maps else []
        
        for i in range(len(p), len(s)):
            maps[s[i]] = 1 + maps.get(s[i], 0)
            maps[s[i-len(p)]] -= 1
            
            if maps[s[i-len(p)]] == 0:
                del maps[s[i-len(p)]]
                
            if mapp == maps: # what is the complexity of this operation
                result.append(i-len(p)+1)
                
        return result