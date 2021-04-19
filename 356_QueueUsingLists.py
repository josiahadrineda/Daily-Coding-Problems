class Queue:
    """A purely list-based implementation of the Queue data structre (apart from
    the capacity as input).

    >>> q = Queue(3)
    >>> q.enqueue(1)
    >>> q.dequeue()
    1
    >>> q.get_size()
    0
    >>> q.dequeue()     # Nothing
    >>> q.enqueue(2)
    >>> q.enqueue(3)
    >>> q.enqueue(4)
    >>> q.enqueue(5)    # Nothing
    >>> q.get_size()
    3
    >>> q.dequeue()
    2
    >>> q.dequeue()
    3
    >>> q.dequeue()
    4
    >>> q.get_size()
    0
    """
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.q = [0] * self.capacity
        self.info = [0] * 3     # [size, head, tail]

    def _adjust_index(self, index):
        return index % self.capacity

    def _set_size(self, size):
        self.info[0] = size

    def _set_head(self, head):
        self.info[1] = head

    def _set_tail(self, tail):
        self.info[2] = tail

    def get_size(self):
        return self.info[0]

    def _get_head(self):
        return self.info[1]

    def _get_tail(self):
        return self.info[2]

    def enqueue(self, value):
        if self.get_size() == self.capacity:
            return

        head = self._get_head()
        self.q[head] = value
        self._set_head(self._adjust_index(head + 1))

        size = self.get_size()
        self._set_size(size + 1)

    def dequeue(self):
        if self.get_size() == 0:
            return

        tail = self._get_tail()
        value = self.q[tail]
        self.q[tail] = 0
        self._set_tail(self._adjust_index(tail + 1))

        size = self.get_size()
        self._set_size(size - 1)

        return value