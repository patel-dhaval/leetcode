class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev, self.next = None, None

class AllOne:

    def __init__(self):
        self.key_map = {}
        self.head, self.tail = Node(0), Node(0)
        self.head.next, self.tail.prev = self.tail, self.head

    def _add_node_after(self, prev_node, next_count, key):
        # prev_node -> < - new_node -> <- prev_node.next
        new_node = Node(next_count)
        new_node.keys.add(key)
        prev, nxt = prev_node, prev_node.next
        new_node.prev, new_node.next = prev, nxt
        prev.next, nxt.prev = new_node, new_node

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
        curr_count = curr_node.count
        next_count = curr_count + 1
        if next_count == curr_node.next.count:
            curr_node.next.keys.add(key)
            self.key_map[key] = curr_node.next
        else:
            new_node = self._add_node_after(curr_node, next_count, key)
            self.key_map[key] = new_node
        
        if not curr_node.keys and curr_node != self.head:
            self._remove_node_if_empty(curr_node)


    def dec(self, key: str) -> None:
        if key not in self.key_map:
            return 

        curr_node = self.key_map[key]
        curr_node.keys.remove(key)

        curr_count = curr_node.count
        next_count = curr_count - 1

        if next_count == 0:
            del self.key_map[key]

        elif next_count == curr_node.prev.count:
            curr_node.prev.keys.add(key)
            self.key_map[key] = curr_node.prev
        else:
            new_node = self._add_node_after(curr_node.prev, next_count, key)
            self.key_map[key] = new_node
        
        
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