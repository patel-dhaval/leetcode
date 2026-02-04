class RandomizedSet:

    def __init__(self):
        self.indices = {}
        self.vals = []

    def insert(self, val: int) -> bool:
        if val in self.indices.keys():
            return False
        self.vals.append(val)
        self.indices[val] = len(self.vals) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices.keys():
            return False
        idx_to_remove = self.indices[val]
        val_at_last_idx = self.vals[-1]
        self.indices[val_at_last_idx] = idx_to_remove
        self.vals[idx_to_remove] = self.vals[-1]
        self.vals.pop()
        del self.indices[val]
        return True

    def getRandom(self) -> int:
        n = len(self.vals)
        rand = randint(0, n-1)

        return self.vals[rand]

        

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()