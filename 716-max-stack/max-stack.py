class MaxStack:

    def __init__(self):
        self.heap = []
        self.stack = []
        self.cnt = 0
        self.deleted_nodes = set()
        heapq.heapify(self.heap)

    def push(self, x: int) -> None:
        self.stack.append((x, self.cnt))
        heapq.heappush(self.heap, (-x, -self.cnt))
        self.cnt += 1

    def pop(self) -> int:
        while self.stack and self.stack[-1][1] in self.deleted_nodes:
            self.stack.pop()

        val, key = self.stack.pop()
        self.deleted_nodes.add(key)

        return val

    def top(self) -> int:
        while self.stack and self.stack[-1][1] in self.deleted_nodes:
            self.stack.pop()

        return self.stack[-1][0]

    def peekMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.deleted_nodes:
            heapq.heappop(self.heap)

        return -self.heap[0][0]

    def popMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.deleted_nodes:
            heapq.heappop(self.heap)

        val, key = heapq.heappop(self.heap)
        self.deleted_nodes.add(-key)
        return -val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()