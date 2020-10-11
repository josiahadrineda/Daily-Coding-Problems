# Vineet John's Implementation
# Note to self: Learn more about static and class methods

class Doubleton:
    instances = {}
    is_even = False

    def __init__(self, id):
        self.id = id

    @classmethod
    def initialize(cls):
        cls.instances[0] = cls(0)
        cls.instances[1] = cls(1)

    @classmethod
    def get_instance(cls):
        if not cls.instances:
            cls.initialize()

        cls.is_even = not cls.is_even
        return cls.instances[int(cls.is_even)]

i1 = Doubleton.get_instance()
assert i1.id == 1
i2 = Doubleton.get_instance()
assert i2.id == 0
i3 = Doubleton.get_instance()
assert i3.id == 1
i4 = Doubleton.get_instance()
assert i4.id == 0
i5 = Doubleton.get_instance()
assert i5.id == 1