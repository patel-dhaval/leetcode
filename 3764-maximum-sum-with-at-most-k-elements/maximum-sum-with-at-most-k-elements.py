class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        def heap_calc(min_heap, k, arr):
            for num in arr:
                heapq.heappush(min_heap, num)
                if len(min_heap) > k:
                    heapq.heappop(min_heap)
            return min_heap[:k]

        combined = []
        i = 0
        for row in grid:
            combined = combined + (heap_calc([], limits[i],row))
            i+=1
        
        min_heap = []
        for num in combined:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
            
        sol_sum = 0
        while len(min_heap):
            sol_sum = (heapq.heappop(min_heap)) + sol_sum

        return sol_sum
