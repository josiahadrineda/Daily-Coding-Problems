class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "Val: {}\nNext: {}".format(self.val, self.next)

class SLL:
    def __init__(self):
        self.head = None

    def __repr__(self):
        curr = self.head
        nodes = []
        while curr:
            nodes.append(curr.val)
            curr = curr.next
        return str(nodes)

    def append(self, val):
        curr = self.head
        to_insert = Node(val)
        if not curr:
            self.head = to_insert
        else:
            while curr.next:
                curr = curr.next
            curr.next = to_insert

    def reverse(self):
        curr = self.head
        prev = None
        next = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

sll = SLL()

sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)
sll.append(5)
print(sll)

sll.reverse()
print(sll)