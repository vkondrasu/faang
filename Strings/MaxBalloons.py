'''
LC 1189. Maximum Number of Balloons
'''
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        #b a ll oo n
        #ablno
        mapp = {}
        mapp['a'] = 0
        mapp['b'] = 1
        mapp['l'] = 2
        mapp['n'] = 3
        mapp['o'] = 4
        
        char_count = [0] * 5
        for c in text:
            if c in mapp:
                char_count[mapp[c]] += 1
                
        char_count[2] //= 2
        char_count[4] //= 2
        
        return min(char_count)