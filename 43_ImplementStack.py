import heapq

class Stack:
    def __init__(self):
        self.stack = []
        self.heap = []
    
    def push(self, val) -> None:
        self.stack.append(val)
        heapq.heappush(self.heap, val)

    def pop(self):
        if self.stack:
            to_remove = self.stack[:-1]
            self.stack = self.stack[:-1]
            self.heap.remove(to_remove)
        else:
            return None
    
    def max(self):
        return self.heap[-1] if self.heap else None

#Driver code
stack = Stack()
assert stack.pop() == None
assert stack.max() == None
assert stack.push(2) == None
assert stack.max() == 2
assert stack.push(1) == None
assert stack.max() == 2