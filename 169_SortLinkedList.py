# (Not-so-) Basic Premise: Bottom-up Merge Sort (non-recursive)
# https://leetcode.com/problems/sort-list/discuss/46712/Bottom-to-up(not-recurring)-with-o(1)-space-complextity-and-o(nlgn)-time-complextity

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        nodes = []
        temp = self
        while temp:
            nodes.append(temp.val)
            temp = temp.next
        return str(nodes)

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return repr(self.head)

def sort(head):
    """Sorts a linked list in O(nlogn) time and **constant** space.

    >>> l = LinkedList()
    >>> l.head = Node(5, Node(4, Node(3, Node(2, Node(1)))))
    >>> l
    [5, 4, 3, 2, 1]
    >>> l = sort(l.head)
    >>> l
    [1, 2, 3, 4, 5]
    """

    n = ll_len(head)
    group_size = 1
    dummy_head = Node(0)
    dummy_head.next = head
    l, r, tail = None, None, None
    while group_size < n:
        curr = dummy_head.next
        tail = dummy_head
        while curr:
            l = curr
            r = split(l, group_size)
            curr = split(r, group_size)
            tail = merge(tail, l, r)
        group_size <<= 1
    return dummy_head.next

def merge(head, l, r):
    curr = head
    while l and r:
        if l.val <= r.val:
            curr.next, l = l, l.next
        else:
            curr.next, r = r, r.next
        curr = curr.next
    curr.next = l or r
    
    while curr.next:
        curr = curr.next
    return curr

def split(head, k):
    i = 1
    while head and i < k:
        head, i = head.next, i + 1

    if not head:
        return head

    temp, head.next = head.next, None
    return temp

def ll_len(head):
    num_nodes = 0
    while head:
        num_nodes, head = num_nodes + 1, head.next
    return num_nodes