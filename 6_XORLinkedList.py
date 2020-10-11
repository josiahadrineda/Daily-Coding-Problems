#DLL
class Node:
    def __init__(self, next=None, prev=None, val=None):
        self.next = next
        self.prev = prev
        self.val = val

class DLL:
    def __init__(self):
        self.head = None

    def push(self, new_val):
        node = Node(next=self.head, prev=None, val=new_val)

        if self.head:
            self.head.prev = node
        self.head = node

    def append(self, new_val):
        node = Node(val=new_val)
        last = self.head

        if last is None:
            self.head = node
            return

        while last:
            last = last.next

        last.next = node
        node.prev = last

    def insert_after(self, prev_node, new_val):
        if prev_node is None:
            return

        node = Node(val=new_val)

        node.next = prev_node.next
        prev_node.next = node
        node.prev = prev_node

        if node.next:
            node.next.prev = node

    def insert_before(self, next_node, new_val):
        if next_node is None:
            return

        node = Node(val=new_val)

        node.prev = next_node.prev
        next_node.prev = node
        node.next = next_node

        if node.prev:
            node.prev.next = node
        else:
            self.head = node

#XORLL (assume get_pointer and dereference_pointer)
class XNode:
    def __init__(self, both=0, val=None):
        self.both = both
        self.val = val

class XLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def get_pointer(self):
        return

    def dereference_pointer(self):
        return

    def add(self, element):
        node = XNode(val=element)

        if self.head is None:
            self.head = self.tail = node
        else:
            node.both = self.get_pointer(self.tail)
            self.tail.both ^= self.get_pointer(node)
            self.tail = node

    def get(self, index):
        previous_address = 0
        current = self.head

        for i in range(index-1):
            temp = self.get_pointer(current)
            current = self.dereference_pointer(previous_address ^ current.both)
            previous_address = temp

            if current.both == previous_address and i < index-2:
                return None
            return current

if __name__ == "__main__":
    xll = XLL()

    while True:
        choice = int(input("1. ADD\n2. GET\n3. EXIT\n").strip())

        if choice == 1:
            element = int(input("Enter element: ").strip())
            xll.add(element)
        elif choice == 2:
            index = int(input("Enter index: ").strip())
            node = xll.get(index)

            if node:
                print(node)
        elif choice == 3:
            exit()
        else:
            print("Invalid choice. Please try again.")