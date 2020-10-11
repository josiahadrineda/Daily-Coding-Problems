"""
Structure of self.neighbors:

e.g.
self.val = 'a'
self.neighbors['N'] = (Node('b'))

This means that 'b' is to the NORTH of 'a'
"""

class Node:

    def __init__(self, val):
        self.val = val
        self.neighbors = {
            'N': set(),
            'E': set(),
            'S': set(),
            'W': set()
        }

    def __repr__(self):
        return str(self.val), self.neighbors

class Map:

    def __init__(self, rules):
        self.rules = rules
        self.nodes = {}
        self.opp = {'N':'S',
                    'E':'W',
                    'S':'N',
                    'W':'E'}

    def validate_rules(self):
        for rule in self.rules:
            p1, dir, p2 = rule.split()
            if self.nodes.get(p1):
                p1 = self.nodes[p1]
            else:
                self.nodes[p1] = Node(p1)
                p1 = self.nodes[p1]
            if self.nodes.get(p2):
                p2 = self.nodes[p2]
            else:
                self.nodes[p2] = Node(p2)
                p2 = self.nodes[p2]

            if not self.add_rule(p1, dir, p2):
                return False
        return True

    def add_rule(self, p1, dir, p2):
        for char in dir:
            if p2 in p1.neighbors[char]:
                return False
            elif p1 in p2.neighbors[self.opp[char]]:
                return False

            for p in p1.neighbors[char]:
                if not self.add_rule(p, char, p2):
                    return False
                return True

        for char in dir:
            p2.neighbors[char].add(p1)
            p1.neighbors[self.opp[char]].add(p2)

        return True

m1 = Map(['A N B','B NE C','C N A'])
assert m1.validate_rules() == False

m2 = Map(['A NW B','A N B'])
assert m2.validate_rules() == True

m3 = Map(['A N B','B S C','A N C']) == True
