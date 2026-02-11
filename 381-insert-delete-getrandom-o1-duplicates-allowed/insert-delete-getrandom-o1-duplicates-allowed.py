"""
DRY RUN:
["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom"]
[[], [1], [1], [2], [], [1], []]

vals = 2
indices = 2:0

idx_to_remove = 0
val_to_swap = 2
vals[0] = 2
self.indices[2] = 0
"""
class RandomizedCollection:

    def __init__(self):
        self.vals = []
        self.indices = collections.defaultdict(set)

    def insert(self, val: int) -> bool:
        isNew = False
        if not val in self.indices:
            isNew = True
        
        self.vals.append(val)
        self.indices[val].add(len(self.vals) - 1)
        return isNew

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        
        idx_to_remove = self.indices[val].pop()
        val_to_swap = self.vals[-1]
        self.vals[idx_to_remove] = self.vals[-1]
        self.indices[val_to_swap].add(idx_to_remove)
        self.indices[self.vals[-1]].remove(len(self.vals)-1)

        if len(self.indices[val]) == 0:
            del self.indices[val] 
        self.vals.pop()
        return True

    def getRandom(self) -> int:
        return self.vals[randint(0, len(self.vals)-1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()