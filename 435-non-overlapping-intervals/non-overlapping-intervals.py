class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        end = intervals[0][1]
        count = 0
        for idx in range(1, len(intervals)):
            if end > intervals[idx][0]:
                end = min(end, intervals[idx][1])
                count +=1 
            else:
                end = intervals[idx][1]

        return count