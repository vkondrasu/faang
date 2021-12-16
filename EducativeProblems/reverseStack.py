
import sys

sys.path.append('../')

import Stack

def reverse(s):
    result = []
    element = s.pop()
    if len(s) > 0:
        result = reverse(s)

    return result.append(element)

s = Stack()
s.append(2)
s.append(3)
s.append(5)
s.append(8)
print(reverse(s))
