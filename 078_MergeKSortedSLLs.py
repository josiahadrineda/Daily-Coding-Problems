class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "\nVal: {}\nNext: {}\n".format(self.val, self.next)

class SLL:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(curr.val)
            curr = curr.next
        return str(nodes) if nodes else "Empty linked list."

    def insert(self, val):
        node = Node(val)
        curr = self.head
        if not curr:
            self.head = node
            return

        while curr.next:
            curr = curr.next
        curr.next = node

def merge_k_sorted_linked_lists(*args):
    args = [*args]
    k = len(args)
    ptrs = [0] * k
    l_merged = SLL()
    while True:
        finished_lists = 0
        local_min = float('inf')
        local_min_ind = 0
        for i in range(k):
            if not args[i].head:
                finished_lists += 1
                continue

            if args[i].head.val <= local_min:
                local_min = args[i].head.val
                local_min_ind = i
        
        if finished_lists == k:
            break

        l_merged.insert(args[local_min_ind].head.val)
        args[local_min_ind].head = args[local_min_ind].head.next
    return l_merged

l1 = SLL()
l1.insert(1)
l1.insert(4)
l1.insert(7)
print(l1)

l2 = SLL()
l2.insert(2)
l2.insert(5)
l2.insert(8)
print(l2)

l3 = SLL()
l3.insert(3)
l3.insert(6)
l3.insert(9)
print(l3)

l_merged = merge_k_sorted_linked_lists(l1, l2, l3)
print(l_merged)