'''
LC 17. Letter Combinations of a Phone Number
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d_map = {}
        d_map['2'] =['a','b','c']
        d_map['3'] =['d','e','f']
        d_map['4'] =['g','h','i']
        d_map['5'] =['j','k','l']
        d_map['6'] =['m','n','o']
        d_map['7'] =['p','q','r','s']
        d_map['8'] =['t','u','v']
        d_map['9'] =['w','x','y','z']
        
        
        n = len(digits)
        if n == 0:
            return []
        prev = []
        for l in d_map[digits[0]]:
            prev.append(l)
            
        i = 1
        while i < n:
            cur = []
            for s in prev:
                for l in d_map[digits[i]]:
                    cur.append(s+l)
                    
            prev = cur
            cur = []
            i += 1
            
        return prev