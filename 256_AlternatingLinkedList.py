class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if not self.next:
            return f'Node({self.val})'
        return f'Node({self.val}, {repr(self.next)})'

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return repr(self.head)

def alternate_ll(l):
    """Given a linked list L, alternates L's values via the
    following scheme: LOW -> HIGH -> LOW -> HIGH

    >>> l = LinkedList()
    >>> l.head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    >>> alternate_ll(l)
    >>> l.head
    Node(1, Node(3, Node(2, Node(5, Node(4)))))
    >>> l.head = Node(5, Node(4, Node(3, Node(2, Node(1)))))
    >>> alternate_ll(l)
    >>> l.head
    Node(1, Node(3, Node(2, Node(5, Node(4)))))
    """
    assert l, 'L cannot be an empty Linked List.'

    def sort_ll(head):
        def find_mid(head):
            slow, fast = head, head
            prev = None
            while fast and fast.next:
                prev, slow, fast = slow, slow.next, fast.next.next
            prev.next = None
            return slow

        def merge_two(a, b):
            dummy = Node(0)
            head = dummy
            while a and b:
                if a.val <= b.val:
                    head.next, a = a, a.next
                else:
                    head.next, b = b, b.next
                head = head.next
            if a:
                head.next = a
            if b:
                head.next = b
            return dummy.next

        if not head or not head.next:
            return head
        
        m = find_mid(head)
        l = sort_ll(head)
        r = sort_ll(m)
        return merge_two(l, r)

    def swap_ll(head):
        if not head or not head.next:
            return head
        node = head.next
        head.next = swap_ll(node.next)
        node.next = head
        return node

    l.head = sort_ll(l.head)
    l.head.next = swap_ll(l.head.next)