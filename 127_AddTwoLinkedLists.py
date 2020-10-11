class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if not self:
            return ''
        elif not self.next:
            return f'Node({self.val})'
        return f'Node({self.val}, {repr(self.next)})'

def add_a_and_b(a, b):
    """
    Given two linked lists a and b, where each list is an integer representation
    with each node as a digit of said integer (in reverse), returns the sum of
    the two lists as another list (same representation).

    >>> a = Node(9, Node(9))
    >>> b = Node(5, Node(2))
    >>> c = add_a_and_b(a, b)
    >>> print(c)
    Node(4, Node(2, Node(1)))
    >>> a = Node(9)
    >>> b = Node(1)
    >>> c = add_a_and_b(a, b)
    >>> print(c)
    Node(0, Node(1))
    """

    if not a and b:
        return Node(0)
    elif not a:
        return b
    elif not b:
        return a

    head_a, head_b = a, b
    prev, temp, carry = None, Node(0), 0
    head_c = temp
    while head_a or head_b or carry:
        c = carry
        if head_a and head_b:
            c += head_a.val + head_b.val
            head_a, head_b = head_a.next, head_b.next
        elif head_a:
            c = head_b.val
            head_a = head_a.next
        elif head_b:
            c = head_a.val
            head_b = head_b.next

        if c >= 10:
            c, carry = c % 10, 1
        else:
            carry = 0

        temp.val = c
        temp.next = Node(0)
        prev, temp = temp, temp.next

    prev.next = None
    return head_c