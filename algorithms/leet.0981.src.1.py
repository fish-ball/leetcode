class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.d.get(key, [])
        idx = bisect.bisect_left(arr, (timestamp, '~'))
        if idx < 1:
            return ''
        return arr[idx-1][1] if idx >= 1 else ''
        



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
