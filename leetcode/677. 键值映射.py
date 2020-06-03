class MapSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        self.d = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        self.d[key] = val

    def sum(self, prefix: str) -> int:
        cnt = 0
        for i in self.d.keys():
            if prefix in i and i[:len(prefix)] == prefix:
                cnt += self.d[i]
        return cnt

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
