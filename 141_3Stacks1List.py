class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.child = None

"""
Keys to Improvement:
    - Instead of only storing parents, store the node at the top of each stack
    - In that way, we can minimize push and pop operations to O(1)
      instead of O(n), n = ancestry
"""

class MultiStack:
    def __init__(self):
        self.list = []
        self.parents = [None] * 3

    def __repr__(self):
        nodes = []
        for p in self.parents:
            ancestry = []
            while p:
                ancestry.append(p.val)
                p = p.child
            nodes.append(ancestry.copy())
        return str(nodes)

    def pop(self, id):
        try:
            if self.parents[id]:
                p = self.parents[id]
                while p.child:
                    p = p.child

                self.list.remove(p)

                if p.parent:
                    p.parent.child = None
                else:
                    self.parents[id] = None

                return p.val
        except IndexError:
            return None

    def push(self, item, id):
        try:
            n = Node(item)
            self.list.append(n)
            if not self.parents[id]:
                self.parents[id] = n
                return

            p = self.parents[id]
            while p.child:
                p = p.child

            p.child = n
            n.parent = p
        except IndexError:
            return None

st = MultiStack()

assert repr(st) == '[[], [], []]'
st.push(1, 0)
st.push(2, 1)
st.push(3, 2)
assert repr(st) == '[[1], [2], [3]]'
val = st.pop(3)
assert not val
val = st.pop(2)
assert val == 3
st.push(6, 0)
st.push(7, 0)
assert repr(st) == '[[1, 6, 7], [2], []]'
val = st.pop(0)
assert val == 7
val = st.pop(1)
assert val == 2
assert repr(st) == '[[1, 6], [], []]'