class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data=data

    def get_next(self):
        return self.next

    def set_next(self,  nxt):
        self.next=nxt

class LinkedStack:
    def __init__(self):
        self.head = None

    def push(self, element):
        node_obj = Node()
        node_obj.set_data(element)
        node_obj.set_next(self.head)
        self.head = node_obj
        return self.show(self.head)

    def pop(self):
        if self.isempty():
            print('stack is emplty')
            return '-1'
        temp = self.head
        popped = self.head.next
        self.head = popped
        print(popped.data)
        return self.show(popped)

    def insertEnd(self, element):
        current = self.head
        if current:
            while current.get_next() != None:
                current = self.current.get_next
            current.set_next(None(element))
        else:
            self.push(element)

    def search(self, data):
        current = self.head
        count = 0
        while current.get_data() != data:
            current = current.get_next()
            count += 1
            if count > self.size():
                return "Not existed"

        return "Postion %s" % count


    def insertPos(self, pos, element):
        if pos == 0:
            self.push(element)
        if pos > self.size() or pos < 0:
            return None
        else:
            if pos == self.size():
                self.insertEnd(element)
            else:
                newNode = Node()
                newNode.set_data(element)
                count = 0
                current = self.head
                while count != pos-1:
                    current = current.get_next()
                    count += 1
                newNode.set_next(current.get_next())
                current.set_next(newNode)
    def deleteend(self):
        current = self.head

        while current.get_next() != None:
            prev = current
            current = current.get_next()
        current = None
        prev.set_next(None)

    def deletePos(self, pos):
        if pos > self.size():
            return "There is no this position"
        elif pos == self.size():
            self.deleteend()
        elif pos == 1:
            self.pop()
        else:
            current = self.head
            count = 0
            while count != pos-1:
                prev = current
                current = current.get_next()
                next = current.get_next()
                count += 1
            prev.set_next(next)

    def isempty(self):
        return True if self.head is None else False

    def show(self, nxt):
        if hasattr(nxt, 'next'):
            print(nxt.data, end=" ")

            if nxt.next is not None:
                self.show(nxt.next)
            else:
                print(" ")
    def display(self):
        current = self.head
        while current.next != None:
            print(current.get_data(), end=" ")
            current = current.get_next()
        print(current.get_data())

    def size(self):
        current = self.head
        count = 0
        while current:
          count += 1
          current = current.get_next()
        return count




stack = LinkedStack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.search(1))

stack.insertPos(1, 4)

stack.display()

stack.deletePos(3)
stack.display()