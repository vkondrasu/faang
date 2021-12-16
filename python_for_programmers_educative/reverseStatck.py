

from Stack import Stack

def reverse(s):
    result = []
    element = s.pop()
    if not s.is_empty():
        result = reverse(s)
    result.append(element)
    return result

s = Stack()
s.push(2)
s.push(3)
s.push(5)
s.push(8)
print(s)
print(reverse(s))