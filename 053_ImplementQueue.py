class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, el):
        self.s1.append(el)

    def dequeue(self):
        if len(self.s1) == 0 and len(self.s2) == 0:
            return -1
        else:
            if len(self.s2) == 0:
                while self.s1:
                    self.s2.append(self.s1.pop())
            return self.s2.pop()

#Driver code
q = Queue()
assert q.enqueue(1) == None
assert q.enqueue(2) == None
assert q.enqueue(3) == None
assert q.enqueue(4) == None
assert q.dequeue() == 1
assert q.dequeue() == 2
assert q.enqueue(5) == None
assert q.enqueue(6) == None
assert q.dequeue() == 3
assert q.dequeue() == 4
assert q.dequeue() == 5
assert q.dequeue() == 6
assert q.dequeue() == -1