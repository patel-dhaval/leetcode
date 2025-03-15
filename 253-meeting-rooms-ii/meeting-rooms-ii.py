"""
sort on start time, add end times to heap, pop when a greater start time comes. at the end the len of heap will have min no of rooms needed.

ip: [[0,30],[5,10],[15,20]]
op: 2

ip: [[0,30],[5,10],[15,20]]
heap: [30], [10, 30], [20, 30]

i = 1, 2
start_times:  5, 15

return len(heap)

"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        heap = []

        intervals.sort(key = lambda x:x[0])

        heapq.heappush(heap, intervals[0][1])

        for i in range(1, len(intervals)):
            if heap[0] <= intervals[i][0]:
                heapq.heappop(heap)
            
            heapq.heappush(heap, intervals[i][1])
        
        return len(heap)
