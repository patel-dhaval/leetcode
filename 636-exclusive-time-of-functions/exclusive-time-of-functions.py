"""
DRY RUN:

stack = []
pid = 0
time = 7
func = end
temp_time = 7
res = [7,1] 
"""

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = [0] * n
        temp_time = 0
        for log in logs:
            pid, function, time = log.split(":")
            pid = int(pid)
            time = int(time)
            
            if function == "start":
                if stack:
                    res[stack[-1]] += (time - temp_time)
                stack.append(pid)
                temp_time = time
            else:
                res[stack[-1]] += (time - temp_time + 1)
                temp_time = time + 1
                stack.pop()

        return res