class RandomizedSet:

    def __init__(self):
        self.indices = {}
        self.vals = []


    def insert(self, val: int) -> bool:
        absent = True
        if val in self.indices:
           return False

        self.vals.append(val)
        self.indices[val] = len(self.vals) - 1

        return absent 

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        
        idx_to_remove = self.indices[val]
        val_to_swap = self.vals[-1]
        self.indices[val_to_swap] = idx_to_remove
        self.vals[idx_to_remove] = val_to_swap
        del self.indices[val]
        self.vals.pop()

        return True

    def getRandom(self) -> int:
        return self.vals[randint(0, len(self.vals)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()