class TimeMap:

    def __init__(self):
        self.map = defaultdict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append([timestamp, value])
        else:
            self.map[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.map:
            return ""
        else:
            values = self.map.get(key, [])

            l = 0
            r = len(values) - 1

            while l <= r:
                m = (l+r)//2
                if values[m][0] <= timestamp:
                    res = values[m][1]
                    l = m + 1
                else:
                    r = m - 1
            
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)