class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev, self.next = None, None
    
class AllOne:
    def __init__(self):
        self.key_map = {}
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next, self.tail.prev = self.tail, self.head


    def _add_node(self, prev_node, count):
        node = Node(count)
        # prev_node -> <- new_node -> <- prev_node.next
        prev, nxt = prev_node, prev_node.next 
        node.prev, node.next = prev, nxt
        prev.next, nxt.prev = node, node
        return node
        
    
    def _remove_node(self, node):
        if not node.keys:
            prev, nxt = node.prev, node.next
            prev.next, nxt.prev = nxt, prev
            return True
        
        return False
        

    def inc(self, key: str) -> None:
        initial_node = self.head
        if key in self.key_map:
            initial_node = self.key_map[key]
            initial_node.keys.remove(key)
            
        initial_count = initial_node.count
        next_count = initial_count + 1
        
        if next_count == initial_node.next.count:
            self.key_map[key] = initial_node.next
            initial_node.next.keys.add(key)
        else:
            node = self._add_node(initial_node, next_count)
            node.keys.add(key)
            self.key_map[key] = node

        if not initial_node.keys and initial_node != self.head:
            self._remove_node(initial_node)

        return

    def dec(self, key: str) -> None:
        if key not in self.key_map:
            return 
        
        initial_node = self.key_map[key] 
        initial_node.keys.remove(key)

        initial_count = initial_node.count
        next_count = initial_count - 1

        if next_count == 0:
            del self.key_map[key]
        
        elif next_count == initial_node.prev.count:
            self.key_map[key] = initial_node.prev
            initial_node.prev.keys.add(key)
        else:
            node = self._add_node(initial_node.prev, next_count)
            node.keys.add(key)
            self.key_map[key] = node
           
        if not initial_node.keys and initial_node != self.head:
            self._remove_node(initial_node)

        return

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head: return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail: return ""
        return next(iter(self.head.next.keys))

        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()