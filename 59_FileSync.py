import hashlib

m = hashlib.md5

class MerkleNode:
    def __init__(self):
        self.parent = None
        self.hash = None

class MerkleDir(MerkleNode):
    def __init__(self):
        MerkleNode.__init__(self)
        self.children = []
        self.is_dir = True

    def recalculate_hash(self):
        if self.children:
            collated_hash = ""
            for child in self.children:
                collated_hash += child.hash
            self.hash = m(collated_hash.encode()).hexdigest()

class MerkleFile(MerkleNode):
    def __init__(self):
        MerkleNode.__init__(self)
        self.contents = None
        self.is_dir = False

    def update_contents(self, new_contents):
        self.hash = m(new_contents.encode()).hexdigest()
        self.contents = new_contents
        if self.parent:
            self.parent.recalculate_hash()

    def add_to_dir(self, dir_node):
        self.parent = dir_node
        dir_node.children.append(self)

        while dir_node:
            dir_node.recalculate_hash()
            dir_node = dir_node.parent

a_1 = MerkleFile()
b_1 = MerkleDir()
a_1.update_contents("abc")
a_1.add_to_dir(b_1)
a_1.update_contents("abcd")

a_2 = MerkleFile()
b_2 = MerkleDir()
a_2.update_contents("abc")
a_2.add_to_dir(b_2)