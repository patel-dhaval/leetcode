class MaxStack:

    def __init__(self):
        self.stack = []
        self.heap = []
        self.cnt = 0
        self.soft_deleted = set()

    def push(self, x: int) -> None:
        heapq.heappush(self.heap, (-x, -self.cnt))
        self.stack.append((x, self.cnt))
        self.cnt += 1

    def pop(self) -> int:
        while self.stack and self.stack[-1][1] in self.soft_deleted:
            self.stack.pop()
        val, idx = self.stack.pop()
        self.soft_deleted.add(idx)
        return val

    def top(self) -> int:
        while self.stack and self.stack[-1][1] in self.soft_deleted:
            self.stack.pop()
        val, idx = self.stack[-1]
        return val

    def peekMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.soft_deleted:
            heapq.heappop(self.heap)

        return -self.heap[0][0]

    def popMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.soft_deleted:
            heapq.heappop(self.heap)

        val, idx =  heapq.heappop(self.heap)
        self.soft_deleted.add(-idx)
        return -val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()