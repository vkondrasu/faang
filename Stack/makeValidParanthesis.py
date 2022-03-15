'''
LC 1249. Minimum Remove to Make Valid Parentheses
'''
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0
        st = []
        sr = []
        
        for i in range(len(s)):
            if s[i] == '(':
                count += 1
                st.append(i)
            elif s[i] == ')':
                count -= 1
                #if there are ')' without '(' then we should remove that
                if count < 0:
                    sr.append(i)
                    count += 1
         
        #if the count is > 0 then we need to remove last count number of '('
        while count > 0:
            sr.append(st.pop())
            count -= 1
        
        result = ""
        for i in range(len(s)):
            if i not in sr:
                result += s[i]
                
        return result