'''
LC 139. Word Break
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def canBeBroken(s):
            #if entire word is in wordDict -- we are good
            if s in wordDict:
                return True
            #empty string is good
            if len(s) == 0:
                return True
            
            if s in mem:
                return mem[s]
            
            ans = False
            
            for i in range(len(s)):
                #if the string sofar in dict -- check if rest of it canBeBroken
                if s[0:i+1] in wordDict:
                    ans = canBeBroken(s[i+1:len(s)])
                    #if the rest of the string can't be broken then we need to continue extending the current string otherwise we are good and can stop further checking
                    if ans:
                        break
            mem[s] = ans
            return ans
        
        mem = {}
        return canBeBroken(s)