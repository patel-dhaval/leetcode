from heapq import heappush, heappop
from typing import List

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        min_heap = []

        for i, row in enumerate(grid):
            # Sort the row and take the largest 'limits[i]' numbers
            top_elements = sorted(row, reverse=True)[:limits[i]]
            
            for num in top_elements:
                heappush(min_heap, num)
                if len(min_heap) > k:
                    heappop(min_heap)  # Keep only the top k elements

        return sum(min_heap)
