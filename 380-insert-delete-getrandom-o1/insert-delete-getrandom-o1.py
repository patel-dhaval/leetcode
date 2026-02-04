class RandomizedSet:

    def __init__(self):
        self.hash_set = {}
        self.val_arr = []

    def insert(self, val: int) -> bool:
        if val in self.hash_set.keys():
            return False
        self.val_arr.append(val)
        self.hash_set[val] = len(self.val_arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash_set.keys():
            return False
        idx = self.hash_set[val]
        val_at_last_idx = self.val_arr[len(self.val_arr)-1]
        self.hash_set[val_at_last_idx] = idx
        self.val_arr[idx], self.val_arr[len(self.val_arr)-1] = self.val_arr[len(self.val_arr)-1], self.val_arr[idx]
        self.val_arr.pop()
        del self.hash_set[val]
        return True

    def getRandom(self) -> int:
        n = len(self.val_arr)
        rand = randint(0, n-1)

        return self.val_arr[rand]

        

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()