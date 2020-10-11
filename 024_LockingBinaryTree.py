#All operations must run in O(h), h = tree height
class Node:
    def __init__(self, val, parent):
        self.val = val
        self.parent = parent
        self.left = None
        self.right = None

        #Is the node locked?
        self.locked = False

        #Optimize lock and unlock methods using a count attr
        self.locked_descendants = 0
    
    def is_locked(self):
        return self.locked

    def lock(self):
        if check_lock_ancestors(self) or self.locked_descendants > 0:
            return False
        else:
            self.locked = True
            update_ancestors(self, True)
            return True
    
    def unlock(self):
        if check_lock_ancestors(self) or self.locked_descendants > 0:
            return False
        else:
            self.locked = False
            update_ancestors(self, False)
            return True

def check_lock_ancestors(node):
    if not node.parent:
        return False
    elif node.parent.locked:
        return True
    return check_lock_ancestors(node.parent)

def update_ancestors(node, toggle_locks):
    update_factor = 1 if toggle_locks else -1
    if node.parent:
        node.parent.locked_descendants += update_factor
        update_ancestors(node.parent, toggle_locks)

#Driver code (taken from vineeetjohn)
a = Node("a", None)
b = Node("b", a)
c = Node("c", a)
d = Node("d", b)
e = Node("e", b)
f = Node("f", c)
g = Node("g", c)

assert b.lock()
assert b.is_locked()
assert c.lock()
assert b.unlock()
assert not b.is_locked()
assert d.lock()

assert not g.lock()
assert c.unlock()
assert g.lock()

assert f.lock()
assert e.lock()
assert a.locked_descendants == 4
assert b.locked_descendants == 2
assert c.locked_descendants == 2