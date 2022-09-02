class TimeMap:

    def __init__(self):
        self.map = collections.defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        i = bisect.bisect_right(self.map[key], timestamp, key=lambda x: x[0])
        return self.map[key][i - 1][1] if i else ''