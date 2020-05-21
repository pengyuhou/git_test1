class Solution:

    def __init__(self, nums):
        self.nums = nums

    def pick(self, target: int) -> int:
        ret = []
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                ret.append(i)
        import random
        return random.choice(ret)

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)


