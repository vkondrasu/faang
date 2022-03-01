
# There are n buildings in New York City and as a real estate agent you decided to visit some of the buildings every day as follows:
# 1 Visit one building.
# 2 If the number of remaining buildings (n) is divisible by 2 then you can visit n/2 buildings.
# 3 If the number of remaining buildings (n) is divisible by 3 then you can visit 2*(n/3) buildings.
# You can only choose one of the strategies per day.
# Return the minimum number of days to visit n buildings.

# n=10

# naive approach: 1 building per day, 10 days

# visited:   5, 1, 2, 1, 1
# remaining: 5, 4, 2, 1, 0
# 5 days


# visted:    1, 6, 2, 1
# remaining: 9, 3, 1, 0
# 4 days

import math

'''
def getMinDaysToVisit(n):
    count = 0
    while n > 0:
        n -= max(2*n//3, n//2, 1)
        count += 1

    return count
'''

def getMinDaysToVisit(n):
    dp = {}
    dp[0]=0
    dp[1]=1

    i=2
    while i<=n:
        dp[i]=dp[i-1]+1
        if i%3 == 0:
            dp[i] = min(dp[i], 1+dp[i//3])
        elif i%2 == 0:
            dp[i] = min(dp[i], 1+dp[i//2])

        i += 1
    return dp[n]
    


'''
def getMinDaysToVisit(n):
    mem = {}
    mem[0] = 0
    mem[1] = 1
    def minNumDays(n):
        if n == 1:
            return 1
        if n < 1:
            return 0

        if n in mem:
            return mem[n]

        build_1 = 1+ minNumDays(n-1)
        build_n2 = math.inf
        build_n3 = math.inf
        
        if n%2 == 0:
            build_n2 = (1 + minNumDays(n//2))
        if n%3 == 0:
            build_n3 = (1 + minNumDays(n//3))

        mem[n] = min(min( build_1, build_n2), build_n3)

        return mem[n]
    
    return minNumDays(n)
'''

print(getMinDaysToVisit(8))
print(getMinDaysToVisit(11))
print(getMinDaysToVisit(10))
print(getMinDaysToVisit(100))
print(getMinDaysToVisit(1000))
print(getMinDaysToVisit(10000))
print(getMinDaysToVisit(100000))
print(getMinDaysToVisit(1000000))