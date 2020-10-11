class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if self.next:
           return f'Node({self.val}, {repr(self.next)})'
        elif self.val:
            return f'Node({self.val})'
        return ''

def swap_iter(head):
    """Given the head of a singly linked list,
    swaps every two nodes and returns its head.
    
    >>> h = Node(1, Node(2, Node(3, Node(4))))
    >>> h
    Node(1, Node(2, Node(3, Node(4))))
    >>> swap_iter(h)
    Node(2, Node(1, Node(4, Node(3))))
    >>> h = Node(1, Node(2, Node(3)))
    >>> swap_iter(h)
    Node(2, Node(1, Node(3)))
    """
    assert head, 'Cannot swap nodes of an empty linked list.'

    swap, temp = Node(), head
    swap_temp = swap
    while temp:
        n1 = temp.val
        temp = temp.next
        if temp:
            n2 = temp.val
            temp = temp.next

            swap_temp.next = Node(n2)
            swap_temp = swap_temp.next
            swap_temp.next = Node(n1)
            swap_temp = swap_temp.next
        else:
            swap_temp.next = Node(n1)
            break
    return swap.next

# vineetjohn

def swap_recur(head):
    """Recursive implementation of above algorithm.

    >>> h = Node(1, Node(2, Node(3, Node(4))))
    >>> h
    Node(1, Node(2, Node(3, Node(4))))
    >>> swap_iter(h)
    Node(2, Node(1, Node(4, Node(3))))
    >>> h = Node(1, Node(2, Node(3)))
    >>> swap_iter(h)
    Node(2, Node(1, Node(3)))
    """
    assert head, 'Cannot swap nodes of an empty linked list.'

    return swap_recur_helper(head)

def swap_recur_helper(head):
    if not head or not head.next:
        return head

    n1 = head
    n2 = head.next
    rest = swap_recur_helper(n2.next)

    n2.next = n1
    n1.next = rest

    return n2