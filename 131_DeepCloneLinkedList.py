class Node:
    def __init__(self, val, next=None, rand=None):
        self.val = val
        self.next = next
        self.rand = rand

    def __repr__(self):
        return str(self.val)

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        head = self.head
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        return str(nodes)

    def print_rand(self):
        head = self.head
        nodes, visited = [], set()
        while head:
            if head in visited:
                break
            nodes.append(head.val)
            visited.add(head)
            head = head.rand
        return nodes

def deep_clone(head):
    """Given the head of a singly-linked list w/ random pointers, deep clone the list.
    
    >>> a = Node(1)
    >>> b = Node(2)
    >>> c = Node(3)
    >>> d = Node(4)
    >>> l1 = LinkedList()
    >>> l1.head = a
    >>> a.next, a.rand = b, d
    >>> b.next, b.rand = c, a
    >>> c.next, c.rand = d, b
    >>> d.rand = c
    >>> l2 = deep_clone(l1.head)
    >>> print(l1)
    [1, 2, 3, 4]
    >>> print(l2)
    [1, 2, 3, 4]
    >>> l1.print_rand()
    [1, 4, 3, 2]
    >>> l2.print_rand()
    [1, 4, 3, 2]
    >>> l1.head.val = 5
    >>> print(l2)
    [1, 2, 3, 4]
    """
    nodes = {}
    temp_head = head
    while temp_head:
        nodes[temp_head] = Node(temp_head.val)
        temp_head = temp_head.next

    temp_head = head
    while temp_head:
        nodes[temp_head].next = nodes.get(temp_head.next)
        nodes[temp_head].rand = nodes.get(temp_head.rand)
        temp_head = temp_head.next
    
    clone = LinkedList()
    clone.head = nodes[head]
    return clone