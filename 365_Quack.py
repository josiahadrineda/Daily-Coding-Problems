class Stack:
    def __init__(self):
        self.stack = []

    def empty(self):
        return not self.stack

    def peek(self):
        return self.stack[-1] if self.stack else None

    def pop(self):
        return self.stack.pop() if self.stack else None

    def push(self, x):
        self.stack.append(x)

class Quack:
    """A data structure combining the properties of both Queues and Stacks. It can be
    viewed as a list of elements written left to right such that three operations are
    possible:

    1. push(x) - Add a new item X to the left end of the list
    2. pop() - Remove and return the leftmost item from the list
    3. pull() - Remove and return the rightmost item from the list

    This implementation of a Quack uses 3 Stacks and O(1) additional memory such that
    the runtime for all operations is amortized O(1).

    >>> q = Quack()
    >>> q.pop()
    >>> q.pull()
    >>> q.push(1)
    >>> q.push(2)
    >>> q.pull()
    1
    >>> q.pop()
    2
    """

    def __init__(self):
        self.head = Stack()
        self.head_copy = Stack()
        self.tail = Stack()

        self.size = 0

    def push(self, x):
        self.head.push(x)
        self.head_copy.push(x)

        self.size += 1

    def pop(self):
        if self.size == 0:
            while not self.head.empty():
                self.head.pop()
            while not self.tail.empty():
                self.tail.pop()
            return None
        else:
            return self.head.pop()

    def pull(self):
        if self.size == 0:
            while not self.head.empty():
                self.head.pop()
            while not self.tail.empty():
                self.tail.pop()
            return None
        else:
            while not self.head_copy.empty():
                self.tail.push(self.head_copy.pop())
            return self.tail.pop()