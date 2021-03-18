import operator
from functools import reduce

class WeightedGraph:
    def __init__(self):
        self.graph = {}

    def in_graph(self, value):
        return value in self.graph

    def get(self, value):
        if not self.in_graph(value):
            return {}
        return self.graph[value]

    def add_node(self, value):
        if not self.in_graph(value):
            self.graph[value] = {}

    def add_edge(self, value1, value2, weight):
        if not self.in_graph(value1):
            return
        if not self.in_graph(value2):
            return
        self.graph[value1][value2] = weight

    def is_connected(self, value1, value2):
        def dfs(a, b):
            if a == b:
                return True
            visited.add(a)
            for neighbor in self.get(a):
                if neighbor in visited:
                    continue
                if dfs(neighbor, b):
                    return True
            return False
        
        if not self.in_graph(value1):
            return False
        if not self.in_graph(value2):
            return False
        visited = set()
        return dfs(value1, value2)

    def shortest_path(self, value1, value2):
        def bfs(value1, value2):
            start, end = (value1, 0), None
            parents = {start: None}
            q = [start]
            while q:
                curr = q.pop(0)
                value, weight = curr
                if value == value2:
                    end = (value, weight)
                    break

                visited.add(value)
                for neighbor, weight in self.get(value).items():
                    if neighbor in visited:
                        continue
                    next = (neighbor, weight)
                    parents[next] = curr
                    q.append(next)
            return parents, end
            
        if not self.is_connected(value1, value2):
            return [(-1, -1)]

        visited = set()
        parents, end = bfs(value1, value2)

        path = []
        while end:
            path.insert(0, end)
            end = parents[end]
        return path

class UnitConverter:
    """A data structure for adding and converting to/from different units of measurement.

    >>> uc = UnitConverter()
    >>> uc.add_conversion(12, 'inch', 'foot')
    >>> uc.add_conversion(3, 'foot', 'yard')
    >>> uc.add_conversion(22, 'yard', 'chain')
    >>> uc.convert(36, 'inch', 'foot')
    3.0
    >>> uc.convert(4, 'yard', 'inch')
    144
    >>> uc.convert(6, 'inch', 'chain')
    0.007575757575757575
    >>> uc.convert(7, 'inch', 'degrees')
    -1
    """
    def __init__(self):
        self.converter = WeightedGraph()

    def add_conversion(self, q, u1, u2):
        self.converter.add_node(u1)
        self.converter.add_node(u2)
        self.converter.add_edge(u2, u1, q)
        self.converter.add_edge(u1, u2, 1 / q)

    def convert(self, q, u1, u2):
        weights = [weight for value, weight in self.converter.shortest_path(u1, u2)]
        if weights == [-1]:
            return -1
        weights = weights[1:]
        return q * reduce(operator.mul, weights)