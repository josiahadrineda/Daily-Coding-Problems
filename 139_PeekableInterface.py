class PeekableInterface:
    def __init__(self, iterator):
        self.it = iterator
        self.next_val = next(self.it)
        self.has_next_val = True

    def peek(self):
        return self.next_val

    def next(self):
        curr = self.next_val
        try:
            self.next_val = next(self.it)
        except StopIteration:
            self.next_val = None
            self.has_next_val = False
        return curr

    def has_next(self):
        return self.has_next_val

sample_list = [1, 2, 3, 4, 5]
iterator = iter(sample_list)
peekable = PeekableInterface(iterator)

assert peekable.peek() == 1
assert peekable.has_next()

assert peekable.next() == 1
assert peekable.next() == 2
assert peekable.next() == 3

assert peekable.peek() == 4
assert peekable.has_next()

assert peekable.next() == 4
assert peekable.has_next()
assert peekable.peek() == 5
assert peekable.next() == 5

assert not peekable.has_next()
assert not peekable.peek()