class Solution:

    def __init__(self, nums):
        from copy import deepcopy
        self.nums = nums
        self.tmp = deepcopy(self.nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        self.nums[:] = self.tmp
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        import random
        random.shuffle(self.nums)
        return self.nums


# Your Solution object will be instantiated and called as such:
obj = Solution([1, 2, 3])
print(obj.shuffle())
print(obj.reset())
