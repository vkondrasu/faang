import sys

from Stack import Stack

original = sys.argv[1]

"""
print(original[::-1])
"""

def reverse_string(original):
    s = Stack()
    for i in range(len(original)):
        s.push(original[i])

    rev_str = ""
    while not s.is_empty():
        rev_str += s.pop()

    return rev_str

print(reverse_string(original))