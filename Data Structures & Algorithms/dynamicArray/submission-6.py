class DynamicArray:
    
    def __init__(self, capacity: int):
        self.cpt = capacity
        self.array = []

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:

        self.array.append(n)
        if len(self.array) > self.cpt:
            self.cpt *= 2

            
    def popback(self) -> int:
        c = self.array[-1]
        self.array = self.array[:-1]
        
        return c

    def resize(self) -> None:
        self.ctp = 2 * self.ctp

    def getSize(self) -> int:
        return len(self.array)
    
    def getCapacity(self) -> int:
        return self.cpt