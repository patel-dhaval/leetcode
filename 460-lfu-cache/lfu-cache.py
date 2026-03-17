class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev, self.next = None, None

class DLinkedList:
    def __init__(self):
        self.size = 0
        self.head, self.tail = Node(0, 0), Node(0,0)
        self.head.next, self.tail.prev = self.tail, self.head

    def add(self, node):
        new_node = node
        self.size += 1
        prev, nxt = self.tail.prev, self.tail
        new_node.prev, new_node.next = prev, nxt
        prev.next, nxt.prev = new_node, new_node
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        self.size -= 1
    
    def remove_lru(self):
        if self.size > 0: 
            node = self.head.next
            self.remove(node)
            return node
        return False


class LFUCache:

    def __init__(self, capacity: int):
        self.key_map = {}
        self.freq_map = collections.defaultdict(DLinkedList)
        self.min_freq = 0
        self.capacity = capacity

    def update(self, node):
        old_freq = node.freq
        self.freq_map[old_freq].remove(node)
        if old_freq == self.min_freq and (self.freq_map[old_freq].size == 0):
            self.min_freq += 1

        node.freq += 1
        self.freq_map[node.freq].add(node)
    

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1

        node = self.key_map[key]
        self.update(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return 
    
        if key in self.key_map:
            node = self.key_map[key]
            node.value = value
            self.update(node)
            return
        
        if self.capacity <= len(self.key_map):
            node = self.freq_map[self.min_freq].remove_lru()
            del self.key_map[node.key]
        
        node = Node(key, value)
        self.key_map[key] = node
        self.min_freq = 1
        self.freq_map[self.min_freq].add(node)

        return



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)