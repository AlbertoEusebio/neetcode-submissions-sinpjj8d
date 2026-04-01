class Node:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.next = self.previous = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.dummy = Node(-1, -1)
        self.tail = Node(-1,-1)
        self.dummy.next=self.tail
        self.tail.previous = self.dummy
        self.l = 0

    def insert(self, node):
        previous, nxt = self.tail.previous, self.tail
        previous.next = nxt.previous = node
        node.next, node.previous = nxt, previous

    def remove(self, node):
        node.previous.next = node.next
        node.next.previous = node.previous

    def get(self, key: int) -> int:
        
        if key in self.cache:
            # Reading the cache is a op
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.l -= 1

        n = Node(value, key)
        self.cache[key] = n
        self.insert(n)

        self.l += 1

        if len(self.cache) > self.capacity:
            k = self.dummy.next.key
            self.remove(self.dummy.next)
            del self.cache[k]
            self.l -= 1

        print(key, value, self.dummy.next.key, self.cache.keys(), len(self.cache))


