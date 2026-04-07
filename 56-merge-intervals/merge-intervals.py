"""
ip: [[1,3], [2,5], [4,7], [8,10]]
 
init_start = 8
init_end = 10
interval =[8,10]
res = [[1,7], [8,10]]
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        initial_start = intervals[0][0]
        initial_end = intervals[0][1]
        res = []
        for interval in intervals[1:]:
            if interval[0] <= initial_end:
                initial_end = max(initial_end, interval[1])
            elif interval[0] > initial_end:
                res.append([initial_start, initial_end])
                initial_start = interval[0]
                initial_end = interval[1]
        
        res.append([initial_start, initial_end])

        return res