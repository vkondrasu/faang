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

stackObject = Stack()
print(stackObject.is_empty())
stackObject.push("hello")
stackObject.push("python")
stackObject.push("I'm coming")

print(stackObject.get_stack())

print(stackObject.pop())
stackObject.push("I'm here")
print(stackObject.get_stack())
print(stackObject.is_empty())

"""