class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res_stack = []
        if not intervals and newInterval:
            return [newInterval]
        
        if intervals and not newInterval:
            return [intervals]

        new_interval_merged = False
        i = 0
        while i in range(0, len(intervals)):
            if not new_interval_merged:
                if newInterval[0] <= intervals[i][1] and newInterval[1] >= intervals[i][0]:
                    start = min(intervals[i][0], newInterval[0])
                    end = max(intervals[i][1], newInterval[1])
                    res_stack.append([start, end])
                    new_interval_merged = True
                else:
                    res_stack.append(intervals[i])
            elif intervals[i][0] <= res_stack[-1][1] and intervals[i][1] > res_stack[-1][1]:
                    start = min(res_stack[-1][0], intervals[i][0])
                    end = max(res_stack[-1][1], intervals[i][1])
                    res_stack.pop()
                    res_stack.append([start, end])
            elif intervals[i][0] <= res_stack[-1][1] and intervals[i][1] <= res_stack[-1][1]:
                i+=1
                continue
            else:
                res_stack.append(intervals[i])
            i+=1

        if not new_interval_merged:
            res_stack.append(newInterval)
        res_stack.sort()
        return res_stack