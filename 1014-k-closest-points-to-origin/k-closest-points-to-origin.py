class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        closest_points = []
        for point in points:
            temp_dist = point[0]*point[0] + point[1]*point[1]
            heapq.heappush(min_heap, (-temp_dist, [point[0], point[1]]))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        for val in min_heap:
            closest_points.append(val[1])

        return closest_points