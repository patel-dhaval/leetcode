class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        def create_max_heap(heap, stones):
            for val in stones:
                heapq.heappush(heap, -val)
            
            return heap

        max_heap = create_max_heap(heap, stones)
        while len(max_heap) > 1:
            stone1 = heapq.heappop(max_heap)
            stone2 = heapq.heappop(max_heap)

            if stone1 == stone2:
                continue
            else:
                new_weight = abs(stone1 - stone2)
                heapq.heappush(max_heap, -new_weight)
        
        return -max_heap[0] if max_heap else 0