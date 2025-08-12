class MinStack:

    def __init__(self):
        self.val_stack = []

    def push(self, val: int) -> None:
        if not self.val_stack:
            self.val_stack.append((val, val))
        else:
            self.val_stack.append((val, min(val, self.getMin())))

    def pop(self) -> None:
        self.val_stack.pop()

    def top(self) -> int:
        return self.val_stack[-1][0] if self.val_stack else None

    def getMin(self) -> int:
        return self.val_stack[-1][1] if self.val_stack else None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()