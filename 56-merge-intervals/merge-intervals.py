class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        start = intervals[0][0]
        end = intervals[0][1]
        res = []
        for idx in range(1, len(intervals)):
            if end >= intervals[idx][0]:
                end = max(end, intervals[idx][1])
            else:
                res.append([start, end])
                start = intervals[idx][0]
                end = intervals[idx][1]

        res.append([start, end])
        return res