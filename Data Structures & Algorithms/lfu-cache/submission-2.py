class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.frq = 1
        self.right = None
        self.left = None
    
class LinkedList:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
    
        self.head.right = self.tail
        self.tail.left = self.head
        
        self.size = 0

    def len(self):
        return self.size

    def append(self, node):
        prev = self.tail.left
        prev.right = node
        node.left = prev

        node.right = self.tail
        self.tail.left = node

        self.size += 1
    
    def remove(self, node):
        
        left, right = node.left, node.right

        left.right = right
        right.left = left
        node.left = None
        node.right = None

        self.size -= 1

    def popleft(self) -> Node:
        if self.size == 0:
            return None
        
        node = self.head.right
        self.remove(node)

        return node

class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.l = 0
        self.cache = {} # val x node map
        self.freqMaps = defaultdict(LinkedList) # freqs x nodes
        self.min_freq = 0

    def count(self, node):
        f = node.frq
        self.freqMaps[f].remove(node)
        if f == self.min_freq and self.freqMaps[f].len() == 0:
            self.min_freq += 1
        
        node.frq = f + 1
        self.freqMaps[f+1].append(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.count(node)

        return node.val

        # list order is already good proxy
        # for each operation we must cut and put on top

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        
        if key not in self.cache:
            if self.l == self.cap:
                node = self.freqMaps[self.min_freq].popleft()
                print("Remove", node.key, node.val, node.frq)
                del self.cache[node.key]
                self.l -= 1

            n = Node(key, value)
            self.cache[key] = n
            self.freqMaps[1].append(n)
            self.min_freq = 1
            self.l += 1
        else:
            n = self.cache[key]
            n.val = value    
            self.count(n)

        print(self.cache)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)