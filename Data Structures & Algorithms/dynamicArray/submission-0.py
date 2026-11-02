class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [None] * capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.length == len(self.arr):
            self.resize()
        
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        self.length -= 1
        return self.arr[self.length]

    def resize(self) -> None:
        new_capacity = len(self.arr) * 2
        new_arr = [None] * new_capacity
        for i, entry in enumerate(self.arr):
            new_arr[i] = entry
        
        self.arr = new_arr

    def getSize(self) -> int:
        return self.length    
    
    def getCapacity(self) -> int:
        return len(self.arr)