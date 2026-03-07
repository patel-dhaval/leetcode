class Solution:

    def __init__(self, w: List[int]):
        self.prefix_arr = []
        self.prefix_sum = 0
        for n in w:
            self.prefix_sum += n
            self.prefix_arr.append(self.prefix_sum)
        self.total_sum = self.prefix_sum

    def pickIndex(self) -> int:
        #self.rand_val = random.random() * self.total_sum
        self.rand_val = randint(1, self.prefix_arr[-1])
        return self.search(self.rand_val)
    
    def search(self, target: int):
        low, high = 0, len(self.prefix_arr) - 1

        while low < high:
            mid = (low+high)//2
            if target == self.prefix_arr[mid]:
                return mid
            elif target > self.prefix_arr[mid]:
                low = mid + 1
            else:
                high = mid
        
        return low


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()