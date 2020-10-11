class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.val, end=' ')
            curr = curr.next
        print()

    def insert(self, val):
        node = Node(val)

        curr = self.head
        if not curr:
            self.head = node
        else:
            while curr.next:
                curr = curr.next
            curr.next = node

    def k_last_element(self, k):
        #Two-pass (returns element but doesn't remove)
        """
        prev = None
        curr = self.head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        while k > 1:
            prev = prev.next
            k -= 1
        return prev.val
        """

        #One-pass
        prev = curr = self.head
        i = 0
        while curr.next:
            if i >= k:
                prev = prev.next
            curr = curr.next
            i += 1
        
        if i == k:
            return self.head.next
        else:
            prev.next = prev.next.next
            return self.head

#Driver code
sll = SLL()

sll.insert(1)
sll.insert(2)
sll.insert(3)
sll.insert(4)
sll.insert(5)
sll.print_list()

sll.k_last_element(3)
sll.print_list()