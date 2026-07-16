class DynamicArray:
    
    def __init__(self, capacity: int):
        self.Array = [None] * capacity
        self.size = 0
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.Array[i]

    def set(self, i: int, n: int) -> None:
        self.Array[i] = n

    def pushback(self, n: int) -> None:
        self.size += 1
        if self.size > self.capacity:
            self.resize()
        self.Array[self.size - 1] = n

    def popback(self) -> int:
        n = self.Array[self.size - 1]
        self.Array[self.size - 1] = None
        self.size -= 1
        return n

    def resize(self) -> None:
        self.Array = self.Array + [None]*self.capacity
        self.capacity *= 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity