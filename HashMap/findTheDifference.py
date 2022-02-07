'''
LC 389. Find the Difference
'''
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        smap = Counter(s)
        tmap = Counter(t)
        
        for k,v in tmap.items():
            if k not in smap or smap[k] < v:
                return k