# 1190. Reverse Substrings Between Each Pair of Parentheses
# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/?envType=daily-question&envId=2024-07-11 
class Solution:
    def reverseParentheses(self, s: str) -> str:
        openIndex = []
        result = []
        openCloseCount = 0
        for i in range(len(s)):
            if s[i] == '(':
                # result contains `x` characters less than orginal string  
                # x = number of '(' and ')' characters encountered so far
                openIndex.append(i - openCloseCount)
                openCloseCount += 1
            elif s[i] == ')':
                revFrom = openIndex.pop()
                result[revFrom:] = result[revFrom:][::-1]
                openCloseCount += 1
            else:
                result.append(s[i])

        return "".join(result)
