import sys

mem = dict()


def climb(n):
    """
    to reach step 5, we can reach from step 3 or step 4
    climb(5) = climb(4) + climb(3)

    to reach first step climb(1) =1 and climb(2) = 2
    """

    if n <= 2:
        return n

    if n in mem:
        return mem[n]

    mem[n] = climb(n-1) + climb(n-2)
    return mem[n]


print( climb(int(sys.argv[1])) )