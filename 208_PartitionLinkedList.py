class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        head = self.head
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        return str(nodes)

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def partition(l, k):
    """Given a linked list of numbers L and a positive integer pivot K, partitions
    L so that all nodes less than K come before nodes greater than or equal to K.

    >>> l = LinkedList()
    >>> l.head = Node(5, Node(4, Node(3, Node(2, Node(1)))))
    >>> print(l)
    [5, 4, 3, 2, 1]
    >>> partition(l, 3)
    >>> print(l)
    [1, 2, 5, 4, 3]
    """
    assert l, 'L cannot be an empty linked list.'
    assert k > 0, 'K must be a positive integer.'

    head = l.head
    prev, curr = head, head.next
    while curr:
        if curr.val < k:
            prev.next = curr.next
            curr.next = head
            head = curr
            curr = prev.next
        else:
            prev, curr = curr, curr.next
    l.head = head