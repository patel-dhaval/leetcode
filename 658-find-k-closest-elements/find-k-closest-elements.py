"""
ip = [1,2,3]
k = 2
x = 3
max_heap = [[0, -2],[-1, -1]]
i = 1, 2, 3
mod_diff = 1, 0, 1  


res = [1,2]
"""
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pq = []
        nums = arr
        for num in nums:
            dist = abs(num - x)
            heapq.heappush(pq, (-dist, -num))  # Push negative to simulate max-heap
            if len(pq) > k:
                heapq.heappop(pq)

        res = [-heapq.heappop(pq)[1] for _ in range(k)]
        res.sort()
        return res