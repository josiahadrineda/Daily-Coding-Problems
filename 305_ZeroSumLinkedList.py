class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        curr = self
        nodes = []
        while curr:
            nodes.append(curr.val)
            curr = curr.next
        return str(nodes)

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        return repr(self.head)

def zero_sum_linked_list(ll):
    """Given a linked list LL, removes all consecutive nodes that sum to zero.

    >>> ll = LinkedList()
    >>> ll.head = Node(3, Node(4, Node(-7, Node(5, Node(-6, Node(6))))))
    >>> zero_sum_linked_list(ll)
    >>> ll
    [5]
    """
    assert ll, 'HEAD cannot be an empty linked list.'

    def mark_cum_sums(head):
        curr = head
        tot = 0
        while curr:
            curr.sum = curr.val + tot
            tot = curr.sum
            curr = curr.next

    mark_cum_sums(ll.head)
    head = ll.head

    dummy_head = Node(None, head)
    dummy_head.sum = 0
    curr = dummy_head
    sums = {}
    while curr:
        if sums.get(curr.sum) != None:
            sums[curr.sum].next = curr.next
        sums[curr.sum] = curr
        curr = curr.next

    ll.head = dummy_head.next