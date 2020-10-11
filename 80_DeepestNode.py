from collections import defaultdict

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return self.val

class Tree:
    def __init__(self):
        self.root = None

    def __repr__(self):
        root = self.root
        nodes = self.bfs(root, [])
        return str(nodes)

    def bfs(self, root, nodes):
        q = [root]
        while q:
            curr = q.pop(0)
            nodes.append(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return nodes

def deepest_node(root):
    nodes, max_dep = bfs_with_depths(root, defaultdict(list))
    return nodes[max_dep][0]

def bfs_with_depths(root, dd):
    max_dep = 0
    q = [(root, 0)]
    while q:
        curr_node, curr_dep = q.pop(0)
        dd[curr_dep].append(curr_node.val)
        if curr_node.left:
            q.append((curr_node.left, curr_dep+1))
        if curr_node.right:
            q.append((curr_node.right, curr_dep+1))
        max_dep = max(max_dep, curr_dep)
    return dd, max_dep

tree = Tree()
tree.root = Node('a')
tree.root.left = Node('b')
tree.root.right = Node('c')
tree.root.left.left = Node('d')

print(tree)

assert deepest_node(tree.root) == 'd'