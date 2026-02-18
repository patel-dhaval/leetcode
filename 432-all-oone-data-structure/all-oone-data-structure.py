"""
Head - 1 - Tail 

Node 
self.count = 0
self.keys = set()

Node 
self.count = 0
self.keys = set()

Node 
self.count = 1
self.keys = set(leet, hello)

Node 
self.count = 2
self.keys = set( 

self.key_map = {hello: 1, leet: 1}

"""
class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.next, self.prev = None, None

class AllOne:

    def __init__(self):
        self.key_map = {}
        self.head, self.tail = Node(0), Node(0)
        self.head.next, self.tail.prev = self.tail, self.head
        
    def _add_node_after(self, prev_node, count):
        # prev_node -> <- new_node -> < - prev_node.next
        
        new_node = Node(count)
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node
        
        return new_node

    
    def _remove_node_if_empty(self, node):
        if not node.keys:
            prev, nxt = node.prev, node.next
            prev.next, nxt.prev = nxt, prev
            return True
        return False

    
    def inc(self, key: str) -> None:
        curr_node = self.head
        if key in self.key_map:
            curr_node = self.key_map[key]
            curr_node.keys.remove(key)
        
        next_count = curr_node.count + 1

        if next_count == curr_node.next.count:
            curr_node.next.keys.add(key)
            self.key_map[key]= curr_node.next
        else:
            next_node= self._add_node_after(curr_node, next_count)
            next_node.keys.add(key)
            self.key_map[key] = next_node

        if not curr_node.keys and curr_node != self.head:
            self._remove_node_if_empty(curr_node)


    def dec(self, key: str) -> None:
        curr_node = self.key_map[key]
        curr_node.keys.remove(key)

        next_count = curr_node.count - 1

        if next_count == curr_node.prev.count:
            curr_node.prev.keys.add(key)
            self.key_map[key]= curr_node.prev
        else:
            next_node= self._add_node_after(curr_node.prev, next_count)
            next_node.keys.add(key)
            self.key_map[key] = next_node
        
        if not curr_node.keys and curr_node != self.head:
            self._remove_node_if_empty(curr_node)


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