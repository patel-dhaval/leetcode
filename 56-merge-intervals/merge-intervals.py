class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        soln = []
        start_ptr = intervals[0][0]
        end_ptr = intervals[0][1]


        for i in range(1, len(intervals)):
            
            if intervals[i][0] in range(start_ptr,end_ptr+1):
                if end_ptr < intervals[i][1]:
                    end_ptr = intervals[i][1]
            else:
                soln.append([start_ptr, end_ptr])
                start_ptr = intervals[i][0]
                end_ptr = intervals[i][1]
        
        soln.append([start_ptr, end_ptr])
        
        return soln