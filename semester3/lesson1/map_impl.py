KEY_SIZE = 5

def hash(key):
    length = len(key)
    return length % KEY_SIZE

class MyMap:
    def __init__ (self):
        self.memory = [None] * KEY_SIZE
    def get(self, k):
        item = self.memory[hash(k)]
        return item[1]
    def put(self, k, v):
        self.memory[hash(k)] = (k, v)
