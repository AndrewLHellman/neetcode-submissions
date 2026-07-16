class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        current_min = self.getMin()
        entry = (val, current_min if current_min <= val else val)
        self.stack.append(entry)  

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return float('inf')
        return self.stack[-1][1]
