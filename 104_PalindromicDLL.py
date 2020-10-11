class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def __repr__(self):
        return f'Val: {self.val}'

class DLL:
    def __init__(self):
        self.head = None

    def __repr__(self):
        head = self.head
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        return str(nodes) if nodes else 'Empty list.'

    def insert(self, val):
        node = Node(val)
        head = self.head
        if not head:
            self.head = node
        else:
            while head.next:
                head = head.next
            head.next = node
            node.prev = head

    def is_palindrome(self):
        """
        Determine whether the doubly linked list is a valid palindrome.

        >>> dll1 = DLL()
        >>> dll1.insert(1)
        >>> dll1.insert(2)
        >>> dll1.insert(3)
        >>> dll1.insert(4)
        >>> dll1.insert(5)
        >>> dll1.is_palindrome()
        False

        >>> dll2 = DLL()
        >>> dll2.insert(1)
        >>> dll2.insert(2)
        >>> dll2.insert(3)
        >>> dll2.insert(2)
        >>> dll2.insert(1)
        >>> dll2.is_palindrome()
        True
        """

        dll_copy = DLL()

        head = self.head
        while head.next:
            head = head.next

        while head:
            dll_copy.insert(head.val)
            head = head.prev

        return repr(self) == repr(dll_copy)