class Stack:
    def __init__(self):
        self.stackArray = list()
        self.limit = 3
        self.top = 0

    def push(self, element):
        if self.top >= self.limit:
            return 'the stack is full'
        self.stackArray.append(element)
        self.top += 1

    def pop(self):
        if self.top <=0:
            return 'the stack is empty'
        item = self.stackArray.pop()
        self.top -= 1
        return item

    def size(self):
        print('size %s' % self.top)

obj = Stack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
print(obj.pop())
print(obj.pop())
print(obj.pop())
obj.size()
