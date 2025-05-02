import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]
        res = []
        heapq.heapify(max_heap)
        print(max_heap)
        while len(max_heap) > 1:
            stone1 = heapq.heappop(max_heap)
            stone2 = heapq.heappop(max_heap)
            
            if stone2 > stone1:
                temp_stone = abs(stone1 - stone2)
                print(temp_stone)
                heapq.heappush(max_heap, -temp_stone)
        
        return -(max_heap[0]) if max_heap else 0