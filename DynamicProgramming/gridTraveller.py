'''
https://youtu.be/oBt53YbR9Kk?t=3644
'''

mem = {}

def gridTraveller(m,n):
    if (m,n) in mem:
        return mem[(m,n)]

    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1

    mem[(m,n)] = gridTraveller(m-1, n) + gridTraveller(m, n-1)
    return mem[(m,n)]

print(gridTraveller(1,1))
print(gridTraveller(2,3))
print(gridTraveller(5,8))
print(gridTraveller(8,5))
print(gridTraveller(18,18))
print(gridTraveller(100,100))
print(gridTraveller(10000,10000))
print(gridTraveller(1000000,1000000))