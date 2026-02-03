from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        queue = collections.deque()

        max_heap = []

        task_count = dict(Counter(tasks))

        for k, v in task_count.items():
            heapq.heappush(max_heap, [-v, k])

        while max_heap or queue:
            time += 1
            
            if max_heap:
                count, char = heapq.heappop(max_heap)
                updated_count = count
                updated_count += 1
                if updated_count < 0:
                    queue.append([updated_count,char,time + n])

            if queue and queue[0][2] == time:
                ready_task = queue.popleft() 
                heapq.heappush(max_heap, [ready_task[0],ready_task[1]])
        
        return time