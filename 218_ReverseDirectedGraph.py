# OOP Representation Adapted from Vineetjohn
# https://github.com/vineetjohn/daily-coding-problem/blob/master/solutions/problem_218.py

class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = set()

    def add_vertex(self, v):
        self.vertices.add(v)

    def add_edge(self, e):
        self.edges.add(e)

    def display_edges(self):
        edges = []
        for e in self.edges:
            edge = (e.src.val, e.dest.val)
            edges.append(edge)
        return edges

    def reverse_edges(self):
        """
        Transposes all edges in the graph.
        
        >>> g = Graph()
        >>> a = Vertex('a')
        >>> b = Vertex('b')
        >>> c = Vertex('c')
        >>> g.add_vertex(a)
        >>> g.add_vertex(b)
        >>> g.add_vertex(c)
        >>> g.add_edge(Edge(a, b))
        >>> g.add_edge(Edge(b, c))
        >>> ('a', 'b') in g.display_edges() and ('b', 'c') in g.display_edges()
        True
        >>> g.reverse_edges()
        >>> ('b', 'a') in g.display_edges() and ('c', 'b') in g.display_edges()
        True
        """

        for e in self.edges:
            e.reverse()

class Vertex:
    def __init__(self, val):
        self.val = val

class Edge:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def reverse(self):
        self.src, self.dest = self.dest, self.src