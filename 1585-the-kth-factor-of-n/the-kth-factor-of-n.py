import heapq
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        min_heap = []
        for i in range(1,n+1):
            if n%i == 0:
                heapq.heappush(min_heap, i)

        print(min_heap)
        return min_heap[k-1] if len(min_heap) >= k else -1
