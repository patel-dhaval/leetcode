import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        heapq.heapify(max_heap)
        res = []
        for x,y in points:
            dist = x**2 + y**2
            heapq.heappush(max_heap, [-dist, [x,y]])
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        while max_heap:
            v = heapq.heappop(max_heap)
            res.append(v[1])

        return res
