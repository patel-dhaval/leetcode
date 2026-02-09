from threading import Lock, Condition
class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.queue = deque()
        self.capacity = capacity
        self.lock = Lock()
        self.not_full = Condition(self.lock)
        self.not_empty = Condition(self.lock)
        

    def enqueue(self, element: int) -> None:
        with self.not_full:
            while len(self.queue)==self.capacity:
                self.not_full.wait()
            self.queue.append(element)
            self.not_empty.notify()
        

    def dequeue(self) -> int:
        with self.not_empty:
            while not self.queue:
                self.not_empty.wait()
            val = self.queue.popleft()
            self.not_full.notify()
            return val
        

    def size(self) -> int:
        with self.lock:
            return len(self.queue)
        