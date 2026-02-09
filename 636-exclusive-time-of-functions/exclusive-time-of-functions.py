class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n
        prev_time = 0
        stack = []
        for log in logs:
            f_id, function, timestamp = log.split(":")
            f_id = int(f_id)
            timestamp = int(timestamp)
            if function == "start":
                if stack:
                    result[stack[-1]] += timestamp - prev_time
                
                stack.append(f_id)
                prev_time = timestamp

            else:
                result[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1
        
        return result

