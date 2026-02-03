class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        res = []
        for point in points:
            temp_dist = point[0]*point[0] + point[1]*point[1]
            heapq.heappush(max_heap, (-temp_dist, point))

        while len(max_heap) > k:
            heapq.heappop(max_heap)

        while max_heap:
            closest_point = heapq.heappop(max_heap)
            res.append(closest_point[1])

        return res
