class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.freq = 1
        self.next, self.prev = None, None

class DLinkedList:
    def __init__(self):
        self.head, self.tail = Node(0,0), Node(0,0)
        self.head.next, self.tail.prev  = self.tail, self.head
        self.size = 0

    def add_node(self, new_node):
        prev, nxt = self.tail.prev, self.tail
        new_node.next = nxt
        new_node.prev = prev
        nxt.prev = new_node
        prev.next = new_node
        self.size += 1
    
    def remove_node(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        self.size -= 1
    
    def remove_lru(self):
        if self.size == 0: return None
        lru_node = self.head.next
        self.remove_node(lru_node)
        return lru_node

class LFUCache:

    def __init__(self, capacity: int):
        self.key_map = {}
        self.freq_map = collections.defaultdict(DLinkedList)
        self.min_freq = 0
        self.capacity = capacity
    
    def _update_freq(self, node):
        old_freq = node.freq
        self.freq_map[old_freq].remove_node(node)

        if old_freq == self.min_freq and self.freq_map[old_freq].size == 0:
            self.min_freq += 1
        
        node.freq +=1
        self.freq_map[node.freq].add_node(node)


    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1
        
        node = self.key_map[key]
        self._update_freq(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return -1
        
        if key in self.key_map:
            node = self.key_map[key]
            node.val = value
            self._update_freq(node)
            return
        
        if len(self.key_map) == self.capacity:
            lru_node = self.freq_map[self.min_freq].remove_lru()
            del self.key_map[lru_node.key]

        new_node = Node(key, value)
        self.key_map[key] = new_node
        self.freq_map[1].add_node(new_node)
        self.min_freq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)