import sys

mem = dict()

def fib(n):
    if n <= 0:
        return n
    if n == 1:
        return n

    if n in mem:
        return mem[n]
    else:
        mem[n] = fib(n-1) + fib(n-2)
        return mem[n]

print( fib( int(sys.argv[1]) ) )