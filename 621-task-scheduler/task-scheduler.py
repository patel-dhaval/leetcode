class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        ## Max heap to track the max_counts values up top, since the goal would be to schedule them earlier 
        max_heap = []
        heapq.heapify(max_heap)
        
        temp = deque()
        ## Counter gives us a dict of the keys and the counts of the keys
        val = Counter(tasks)
    
        for k, v in val.items():
            ## Appending the max counts first - so that the heap sorts on it
            heapq.heappush(max_heap, [-v, k, 0])
        
        time = 0
        while max_heap or temp:
            time += 1
            ## Process heap - pick up a task, update its time and add to queue
            if max_heap:
                v, k, time_passed = heapq.heappop(max_heap)
                v = abs(v)
                v -= 1
                if v:
                    temp.append([-v, k, time+n])
            ## Check if vals in queue, check time of the task, and execute the tasks if the time matches
            if temp and temp[0][2] == time:
                temp_val = temp.popleft()
                heapq.heappush(max_heap, temp_val)
    
        return time