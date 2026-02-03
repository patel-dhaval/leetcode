from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        queue = collections.deque()

        max_heap = []

        task_count = dict(Counter(tasks))

        for k, v in task_count.items():
            heapq.heappush(max_heap, -v)

        while max_heap or queue:
            time += 1
            
            if max_heap:
                count = heapq.heappop(max_heap)
                updated_count = count + 1
                if updated_count < 0:
                    queue.append([updated_count, time + n])

            if queue and queue[0][1] == time:
                ready_task = queue.popleft() 
                heapq.heappush(max_heap, ready_task[0])
        
        return time