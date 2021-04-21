# https://stackoverflow.com/questions/58777030/increment-key-decrement-key-find-max-key-find-min-key-in-o1-time

class BucketNode:
    def __init__(self, count, prev=None, next=None):
        self.count = count
        self.keys = set()
        self.prev = prev
        self.next = next

class Counter:
    """A data structure that stores items and their frequencies. Supports plus (add),
    min_freqs (remove), get_min_freq, and get_max_freq operations - all in (amortized) O(1) time.
    
    >>> c = Counter()
    >>> c.minus(-1) # Edge case
    >>> c.get_min() # Nothing has been added
    >>> c.get_max() # Nothing has been added
    >>> c.plus(1)
    >>> c.get_min()
    1
    >>> c.get_max()
    1
    >>> c.plus(1)
    >>> c.minus(1)
    >>> c.plus(2)
    >>> c.plus(2)
    >>> c.get_min()
    1
    >>> c.get_max()
    2
    >>> c.minus(1)  # 1 has been deleted
    >>> c.plus(3)
    >>> c.plus(3)
    >>> c.plus(3)
    >>> c.get_min()
    2
    >>> c.get_max()
    3
    >>> c.minus(2)
    >>> c.minus(2)
    >>> c.get_min()
    3
    >>> c.get_max()
    3
    >>> c.minus(3)
    >>> c.minus(3)
    >>> c.minus(3)
    >>> c.get_min()
    >>> c.get_max()
    """

    def __init__(self):
        self.counter = BucketNode(-1)
        self.counter.prev, self.counter.next = self.counter, self.counter
        self.keys_to_buckets = {}

    def _print_buckets(self):
        curr, nodes = self.counter.next, []
        while curr.count != -1:
            nodes.append((curr.count, curr.keys))
            curr = curr.next
        print(nodes)

    def _insert(self, count, key, prev_bucket, next_bucket):
        new_bucket = BucketNode(count)
        new_bucket.keys.add(key)
        new_bucket.prev, prev_bucket.next = prev_bucket, new_bucket
        new_bucket.next, next_bucket.prev = next_bucket, new_bucket
        return new_bucket

    def _remove(self, bucket):
        bucket.prev.next, bucket.next.prev = bucket.next, bucket.prev

    def plus(self, key):
        if key not in self.keys_to_buckets:
            if self.counter.next.count == 1:
                bucket = self.counter.next
                bucket.keys.add(key)
                b = bucket
            else:
                b = self._insert(1, key, self.counter, self.counter.next)
        else:
            bucket = self.keys_to_buckets[key]
            bucket.keys.remove(key)
            if not bucket.keys:
                self._remove(bucket)
                self.keys_to_buckets.pop(key)
            
            if bucket.next.count == bucket.count + 1:
                bucket.next.keys.add(key)
                b = bucket.next
            elif not bucket.keys:
                b = self._insert(bucket.count + 1, key, bucket.prev, bucket.next)
            else:
                b = self._insert(bucket.count + 1, key, bucket, bucket.next)
        self.keys_to_buckets[key] = b

    def minus(self, key):
        if key not in self.keys_to_buckets:
            return

        bucket = self.keys_to_buckets[key]
        bucket.keys.remove(key)
        if not bucket.keys:
            self._remove(bucket)
            self.keys_to_buckets.pop(key)
        
        b = None
        if bucket.prev.count == bucket.count - 1:
            bucket.prev.keys.add(key)
            b = bucket.prev
        elif bucket.count > 1:
            if not bucket.keys:
                b = self._insert(bucket.count - 1, key, bucket.prev, bucket.next)
            else:
                b = self._insert(bucket.count - 1, key, bucket.prev, bucket)
        
        if b:
            self.keys_to_buckets[key] = b

    def get_min(self):
        head = self.counter.next
        if head is self.counter:
            return
        return next(iter(head.keys))

    def get_max(self):
        tail = self.counter.prev
        if tail is self.counter:
            return
        return next(iter(tail.keys))