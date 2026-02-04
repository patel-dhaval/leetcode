class RandomizedCollection:

    def __init__(self):
        self.indices = DefaultDict(set)
        self.vals = []

    def insert(self, val: int) -> bool:
        isNew = False
        if not self.indices[val]: # Returns True if key missing OR set is empty
            isNew = True

        self.vals.append(val)
        self.indices[val].add(len(self.vals) - 1)
        return isNew

    def remove(self, val: int) -> bool:
        
        if len(self.indices[val]) == 0:
            return False

        idx_to_remove = self.indices[val].pop()
        val_to_swap = self.vals[-1]
        self.indices[val_to_swap].add(idx_to_remove)
        self.indices[val_to_swap].remove(len(self.vals)-1)
        self.vals[idx_to_remove] = self.vals[-1]
        self.vals.pop()
        return True

    def getRandom(self) -> int:
        n = len(self.vals)
        rand = randint(0, n-1)
        return self.vals[rand]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()