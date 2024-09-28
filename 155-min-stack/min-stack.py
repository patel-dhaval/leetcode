# class MinStack:

#     def __init__(self):
#         self.stack = []

#     def push(self, val: int) -> None:
#         if self.stack:
#             self.minVal = self.stack[-1][1]
#         else:
#             self.minVal = float('inf')
#         if val < self.minVal:
#             self.minVal = val  
#         self.stack.append([val, self.minVal])
#         return None

#     def pop(self) -> None:
#         self.stack.pop()
#         return None

#     def top(self) -> int:
#         return self.stack[-1][0]

#     def getMin(self) -> int:
#         minval = self.stack[-1][1]
#         return minval


class MinStack:

    def __init__(self):
        self.stk1=[]
        self.stk2=[inf]
        
        

    def push(self, val: int) -> None:
        self.stk1.append(val)
        self.stk2.append(min(val,self.stk2[-1]))
        

    def pop(self) -> None:
        self.stk1.pop()
        self.stk2.pop()

        

    def top(self) -> int:
        return self.stk1[-1]
        

    def getMin(self) -> int:
        return self.stk2[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()