class Heap:
    """A data structure for returning the maximum-valued element.
    """

    def __init__(self, start=[]):
        self.heap = start

    def push(self, item):
        self.heap.append(item)

    def pop(self):
        if not self.heap:
            return None
        else:
            ind = self.heap.index(max(self.heap))
            return self.heap.pop(ind)

class Stack(Heap):
    """A data structure for returning elements in chronological order.
    *Must be implemented using Heap*
    """

    def __init__(self, start=[]):
        Heap.__init__(self, start)
        self.ind = 0

    def push(self, item):
        super().push((self.ind, item))
        self.ind += 1

    def pop(self):
        pair = super().pop()
        if not pair:
            return pair
        else:
            _, el = pair
            return el

# Tests
stk = Stack()
stk.push(1)
stk.push(7)
stk.push(4)
assert stk.pop() == 4
stk.push(2)
assert stk.pop() == 2
assert stk.pop() == 7
assert stk.pop() == 1
assert not stk.pop()