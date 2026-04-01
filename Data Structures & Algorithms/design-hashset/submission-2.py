class MyHashSet:

    def __init__(self):
        self.keys = [0] * 1_000_000

    def add(self, key: int) -> None:
        self.keys[key] = 1

    def remove(self, key: int) -> None:
        self.keys[key] = 0

    def contains(self, key: int) -> bool:
        return bool(self.keys[key])


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)