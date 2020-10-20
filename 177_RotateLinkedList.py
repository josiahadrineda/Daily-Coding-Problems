class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        head = self.head
        while head:
            nodes.append(head.val)
            head = head.next
        return str(nodes)

def rotate(l, k):
    """Given a linked list L and a positive integer K, rotates
    the list to the right by K spaces.

    >>> l = LinkedList()
    >>> l.head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    >>> rotate(l, 3)
    >>> l
    [3, 4, 5, 1, 2]
    """
    assert isinstance(l, LinkedList), 'L must be of type LinkedList.'
    assert k > 0, 'K must be a positive integer.'

    n = 0
    head = l.head
    temp = head
    while temp:
        n, temp = n + 1, temp.next

    k %= n
    if k:
        spaces = n - k
        break_point, new_head, temp = None, head, head
        while temp.next:
            if spaces > 0:
                spaces, break_point, new_head = spaces - 1, new_head, new_head.next
            temp = temp.next
        break_point.next = None
        temp.next = head
        l.head = new_head