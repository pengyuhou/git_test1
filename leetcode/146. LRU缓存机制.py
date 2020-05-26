class LRUCache:

    def __init__(self, capacity: int):
        self.a = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.a.keys():
            self.a[key] = self.a.pop(key)
            return self.a[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.a.keys():
            self.a.pop(key)
        if len(self.a) == self.capacity:
            self.a.pop(list(self.a)[0])
        self.a[key] = value

#
# # Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(3)
# # param_1 = obj.get(key)
# # obj.put(key,value)
# print(obj.put(2, 5))
# print(obj.put(2, 4))
# print(obj.get(2))


a = {1: 5, 3: 7, 8: 6}
print(a.pop(list(a.keys())[0]))

print(list(a))
