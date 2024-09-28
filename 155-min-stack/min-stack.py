class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            self.minVal = self.stack[-1][1]
        else:
            self.minVal = float('inf')
        if val < self.minVal:
            self.minVal = val  
        self.stack.append([val, self.minVal])
        return None

    def pop(self) -> None:
        self.stack.pop()
        return None

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        minval = self.stack[-1][1]
        return minval


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()