'''
LC 640. Solve the Equation
'''

class Solution:
    def solveEquation(self, equation: str) -> str:
        
        def breakIt(s):
            result = []
            r = ""
            for i in range(len(s)):
                if s[i] == '+' or s[i] == '-':
                    if len(r) > 0:
                        result.append(r)
                    r = s[i]
                else:
                    r += s[i]
                    
            result.append(r)
            return result
        
        def coeff(s):
            if s == "":
                return 1
            if s[0] == '+':
                return coeff(s[1:])
            if s[0] == '-':
                return -coeff(s[1:])
            
            return int(s)
                
        
        lr = equation.split("=")
        lhs, rhs = 0, 0
        
        for x in breakIt(lr[0]):
            if "x" in x:
                lhs += coeff(x[0:-1])
            else:
                rhs -= int(x)
        #print(lhs, rhs)      
        for x in breakIt(lr[1]):
            if "x" in x:
                lhs -= coeff(x[0:-1])
            else:
                rhs += int(x)
                
        #print(lhs, rhs)
        
        if lhs == 0:
            if rhs == 0:
                return "Infinite solutions"
            else:
                return "No solution"
            
        return "x=" + str(rhs // lhs)