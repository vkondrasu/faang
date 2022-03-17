'''
LC 856. Score of Parentheses
'''
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = []
        score = 0
        
        for c in s:
            if c == '(':
                st.append(c)
            else:
                tempScore = 0
                while st[-1] != '(':
                    tempScore += st.pop()
                st.pop()
                if tempScore != 0:
                    st.append(tempScore * 2)
                else:
                    st.append(1)
        
        for r in st:
            score += r
            
        return score