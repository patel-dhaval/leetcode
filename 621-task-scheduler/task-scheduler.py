"""
Approach

Since we have frequencies of tasks, we can use heap as it will give us the max of the freq in log time
There is a timeout which is present, after which the same 2 tasks can be processed.
To track this time, we can use a queue, where we add the updated freq of the task as well as the time when it will be avaialbe to be processed
Loop through till there are tasks in heap or queue
Track time intervals
If time interval == queue[0][1]: pop the value from queue and push it up on heap

"""

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time