class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.a = set()

    def add(self, key: int) -> None:
        self.a.add(key)

    def remove(self, key: int) -> None:
        try:
            self.a.remove(key)
        except:
            pass

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.a

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
