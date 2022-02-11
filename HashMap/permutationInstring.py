'''
LC 567. Permutation in String
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1Map = Counter(s1)
        s2Map = Counter(s2[0:n])
        
        
        
        result = False
        
        l , r = 0, n-1
        n = len(s2)
        
        while r < n:
            if s1Map == s2Map:
                return True
            
            #remove starting char
            s2Map[s2[l]] -= 1
            if s2Map[s2[l]] == 0:
                del s2Map[s2[l]]
            
            #move starting point   
            l += 1
            
            #add end char
            r += 1
            if r < n:
                s2Map[s2[r]] = s2Map.get(s2[r], 0) + 1
            
        return result