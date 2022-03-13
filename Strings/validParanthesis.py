'''
LC 20. Valid Parentheses
'''
class Solution:
    def isValid(self, s: str) -> bool:
        mapp = {}
        mapp[')'] = '('
        mapp[']'] = '['
        mapp['}'] = '{'
        
        stack = []
        for i in range(len(s)):
            if s[i] in ['(','[','{']:
                stack.append(s[i])
            elif len(stack) > 0:
                if mapp[s[i]] == stack[len(stack)-1]:
                    stack.pop()
                else:
                    return False
            else:
                return False
                
        return len(stack) == 0