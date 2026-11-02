from collections import heapq

# 1 # 1

# 1 # 1
# 2

# 0 # 0
# 2 # 1
# 1

class MinStack:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, val: int) -> None:
        self.stack1.append(val)
        if not self.stack2:
            self.stack2.append(val)
        elif val <= self.stack2[-1]:
            self.stack2.append(val)

    def pop(self) -> None:
        popped = self.stack1.pop()
        if popped == self.stack2[-1]:
            self.stack2.pop()

    def top(self) -> int:
        return self.stack1[-1]

    def getMin(self) -> int:
        return self.stack2[-1]