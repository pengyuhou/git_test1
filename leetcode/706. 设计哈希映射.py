class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.a = {}

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """

        self.a[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        try:
            return self.a[key]
        except:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        try:
            self.a.pop(key)
        except:
            pass









