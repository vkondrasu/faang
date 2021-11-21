import sys
from Stack import Stack

"""

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

"""

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    if p1 == "[" and p2 == "]":
        return True
    if p1 == "{" and p2 == "}":
        return True

    return False

def is_paren_balanced(paren_string):
    s = Stack()
    is_balnced = True

    for i in range(len(paren_string)):
        if paren_string[i] in "[{(":
            s.push(paren_string[i])
        else:
            if s.is_empty():
                is_balnced = False
                break
            else:
                if not is_match(s.peek(), paren_string[i]):
                    is_balnced = False
                    break
                else:
                    s.pop()

    if s.is_empty() and is_balnced:
        return True
    else:
        return False



print(is_paren_balanced(sys.argv[1]))