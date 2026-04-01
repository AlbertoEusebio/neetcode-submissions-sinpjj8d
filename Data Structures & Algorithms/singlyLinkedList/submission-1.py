class LinkedList:
    
    def __init__(self):
        self.lst = []
        self.nodes = []
    
    def get(self, index: int) -> int:
        if index >= len(self.lst) or index < 0:
            return -1
        return self.lst[index]

    def insertHead(self, val: int) -> None:
        self.lst = [val] + self.lst        

    def insertTail(self, val: int) -> None:
        self.lst.append(val)

    def remove(self, index: int) -> bool:
        if index >= len(self.lst) or index < 0:
            return False

        self.lst = self.lst[:index] + self.lst[index+1:]
        return True

    def getValues(self) -> List[int]:
        return self.lst
