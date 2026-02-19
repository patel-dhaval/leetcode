"""
DRY RUN:
n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]

res = [,4]
stack = [0]
prev_time = 5
"""

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        prev_time = 0
        stack = []
        for log in logs:
            idx, function, time_stamp = log.split(":")
            idx = int(idx)
            timestamp = int(time_stamp)
            if function == "start":
                if stack:
                    curr_idx = stack[-1]
                    res[curr_idx] += timestamp - prev_time
                stack.append(idx)
                prev_time = timestamp
            else:
                curr_idx = stack.pop()
                res[curr_idx] += timestamp - prev_time + 1
                prev_time = timestamp + 1
        
        return res