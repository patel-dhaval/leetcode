class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key= lambda x:x[0])
        start_time = intervals[0][0]
        end_time = intervals[0][1]
        res = []
        for start, end in intervals[1:]:
            if start <= end_time:
                if end_time <= end:
                    end_time = end
            else:
                res.append([start_time, end_time])
                start_time = start
                end_time = end
        
        res.append([start_time, end_time])
        return res