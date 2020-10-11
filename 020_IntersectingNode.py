class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.val, end=' ')
            temp = temp.next
        print()

    def insert(self, val):
        node = Node(val)
        temp = self.head

        if not temp:
            self.head = node
            return

        while temp.next:
            temp = temp.next
        temp.next = node

def find_intersecting_node(ll1: LinkedList, ll2: LinkedList) -> Node:
    cnt1, cnt2 = 0, 0

    temp = ll1.head
    while temp:
        cnt1 += 1
        temp = temp.next
    
    temp = ll2.head
    while temp:
        cnt2 += 1
        temp = temp.next
    
    diff = abs(cnt1 - cnt2)
    head1, head2 = ll1.head, ll2.head
    if cnt1 > cnt2:
        while diff > 0:
            head1 = head1.next
            diff -= 1
    elif cnt2 > cnt1:
        while diff > 0:
            head2 = head2.next
            diff -= 1
    
    while head1 and head1.val != head2.val:
        head1 = head1.next
        head2 = head2.next
    
    if head1:
        return head1.val
    return None

#Driver code
ll1 = LinkedList()
ll1.insert(1)
ll1.insert(2)
ll1.insert(3)
ll1.insert(4)
ll1.insert(5)
ll1.print_list()

ll2 = LinkedList()
ll2.insert(6)
ll2.insert(7)
ll2.insert(8)
ll2.insert(9)
ll2.insert(5)
ll2.print_list()

print(find_intersecting_node(ll1, ll2))