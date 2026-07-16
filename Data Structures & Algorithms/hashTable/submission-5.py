class Pair:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value

class HashTable:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.table = [None] * capacity

    def insert(self, key: int, value: int) -> None:
        index = key % self.capacity
        while True:
            if self.table[index] == None:
                self.table[index] = Pair(key, value)
                self.size += 1
                break
            elif self.table[index].key == key:
                self.table[index].value = value
                break
            else:
                index = (index + 1) % self.capacity
        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = key % self.capacity
        while self.table[index] != None:
            if self.table[index].key == key:
                return self.table[index].value
            else:
                index = (index + 1) % self.capacity
        return -1

    def remove(self, key: int) -> bool:
        index = key % self.capacity
        while self.table[index] != None:
            if self.table[index].key == key:
                self.table[index] = None
                index = (index + 1) % self.capacity
                reinsert = []
                while self.table[index] != None:
                    reinsert.append(self.table[index])
                    self.table[index] = None
                    self.size -= 1
                    index = (index + 1) % self.capacity
                for pair in reinsert:
                    self.insert(pair.key, pair.value)
                self.size -= 1
                return True
            else:
                index = (index + 1) % self.capacity
        return False


    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        old_table = self.table
        self.capacity *= 2
        self.table = [ None ] * self.capacity
        self.size = 0
        for pair in old_table:
            if pair != None:
                self.insert(pair.key, pair.value)
