class Node:
    def __init__(self, name, weight=0, children=[]):
        self.name = name
        self.weight = weight
        self.children = children

    def is_leaf(self):
        return not self.children

class Tree:
    def __init__(self):
        self.root = None

    def longest_path(self):
        def bfs(root):
            max_path = float('-inf')
            q = [root]
            while q:
                curr = q.pop(0)
                max_path = max(max_path, dfs(curr))
                for child in curr.children:
                    q.append(child)
            return max_path

        def dfs(root):
            def max_path(root):
                if root.is_leaf():
                    return root.weight
                else:
                    paths = [max_path(child) for child in root.children]
                    return root.weight + max(paths)
            
            paths = [max_path(child) for child in root.children]
            return sum(sorted(paths, reverse=True)[:2])

        return bfs(self.root)

t = Tree()

a = Node('a')
b = Node('b', 3)
c = Node('c', 5)
d = Node('d', 8)
e = Node('e', 2)
f = Node('f', 4)
g = Node('g', 1)
h = Node('h', 1)

t.root = a
a.children = [b, c, d]
d.children = [e, f]
e.children = [g, h]

assert t.longest_path() == 17