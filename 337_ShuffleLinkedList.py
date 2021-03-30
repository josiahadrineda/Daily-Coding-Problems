from random import random

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
        
        s = '< '
        for node in nodes:
            s += str(node) + ' '
        s += '>'
        return s

# TC = O(N^2), SC = O(1)
def shuffle(ll):
    """Given a LinkedList LL, uniformly shuffles the nodes in LL, prioritizing
    space over time.
    """
    assert ll, 'LL cannot be an empty LinkedList.'

    def get_random_node(head):
        nodes, rand_node = 0, None
        while head:
            if not head._visited:
                nodes += 1
                if random() < 1 / nodes:
                    rand_node = head
            head = head._next
        if rand_node:
            rand_node._visited = True
        return rand_node

    head = ll.head
    while head:
        setattr(head, '_visited', False)
        setattr(head, '_next', head.next)
        head = head.next
    
    head = get_random_node(ll.head)
    temp = head
    while True:
        next = get_random_node(ll.head)
        if not next:
            temp.next = None
            break
        temp.next = next
        temp = temp.next

    temp = ll.head
    while temp:
        delattr(temp, '_visited')
        _temp = temp._next
        delattr(temp, '_next')
        temp = _temp

    ll.head = head

ll = LinkedList()
ll.head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(ll)

shuffle(ll)
print(ll)