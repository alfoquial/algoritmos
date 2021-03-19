class HashTable:
    """A class implementation of a map"""

    def __init__(self):
        self.size = 11
        self.slots = []
        self.data = []

    def put(self, key, value):
