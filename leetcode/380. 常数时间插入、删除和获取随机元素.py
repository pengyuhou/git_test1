class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.li = set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        l = len(self.li)
        self.li.add(val)
        return not l == len(self.li)

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        try:
            self.li.remove(val)
            return True
        except:
            return False


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        import random
        res = random.choice(list(self.li))
        return res






# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
print(param_1)
param_2 = obj.remove(2)
print(param_2)
print(obj.insert(2))
print(obj.getRandom())
print(obj.remove(1))


