"""
DRY RUN:
res = [8]
stack = [0]
prev_time = 7
time_stamp = 7
"""
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        prev_time = 0
        for log in logs:
            tid, function,timestamp = log.split(":")
            tid = int(tid)
            timestamp = int(timestamp)

            if function == "start":
                if stack:
                    res[stack[-1]] += timestamp - prev_time
                stack.append(tid)
                prev_time = timestamp
            else:
                res[stack[-1]] += timestamp - prev_time + 1
                stack.pop()
                prev_time = timestamp + 1

        return res