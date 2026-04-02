class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev, self.next = None, None
   
class LRUCache:

    def __init__(self, capacity: int):
        self.key_map = {}
        self.capacity = capacity
        self.head, self.tail = Node(0,0), Node(0,0)
        self.head.next, self.tail.prev = self.tail, self.head

    def _add_node(self, node):
        prev, nxt = self.tail.prev, self.tail
        node.prev, node.next = prev, nxt
        prev.next, nxt.prev = node, node
    
    def _remove_node(self, node=None):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1
        
        node = self.key_map[key]
        self._remove_node(node)
        self._add_node(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return False
        
        if key in self.key_map:
            self._remove_node(self.key_map[key])
            
        self.key_map[key] = Node(key, value)       
        self._add_node(self.key_map[key])

        while len(self.key_map) > self.capacity:
            lru_node = self.head.next
            self._remove_node(lru_node)
            del self.key_map[lru_node.key]
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)