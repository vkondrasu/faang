from Stack import Stack

import sys

ip_number = int(sys.argv[1])


def decimal_to_binary(number):
    s = Stack()
    while number > 0:
        s.push(int(number%2))
        number //=2

    binary_str = ""

    while not s.is_empty():
        binary_str += str(s.pop())

    return binary_str

print( decimal_to_binary(ip_number) )

