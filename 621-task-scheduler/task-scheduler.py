import heapq
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_heap = []
        heapq.heapify(max_heap)
        temp = deque()
        val = Counter(tasks)
    
        for k, v in val.items():
            heapq.heappush(max_heap, [-v, k, 0])
        
        time = 0
        while max_heap or temp:
            time += 1
            if max_heap:
                v, k, time_passed = heapq.heappop(max_heap)
                v = abs(v)
                v -= 1
                if v != 0:
                    temp.append([-v, k, time+n])

            if temp and temp[0][2] == time:
                temp_val = temp.popleft()
                heapq.heappush(max_heap, temp_val)
    
        return time
        