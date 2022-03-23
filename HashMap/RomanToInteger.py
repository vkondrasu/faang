'''
LC 13. Roman to Integer
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        mapp = {}
        
        mapp['I'] = 1
        mapp['V'] = 5
        mapp['X'] = 10
        mapp['L'] = 50
        mapp['C'] = 100
        mapp['D'] = 500
        mapp['M'] = 1000
        
        d_map = {}
        d_map['V'] = 'I'
        d_map['X'] = 'I'
        d_map['L'] = 'X'
        d_map['C'] = 'X'
        d_map['D'] = 'C'
        d_map['M'] = 'C'
        
        result = 0
        n = len(s)
        for i in range(n):
            if s[i] in d_map and i > 0 and d_map[s[i]] == s[i-1]:
                result -= 2* mapp.get(s[i-1])
            result += mapp.get(s[i])
            
        return result