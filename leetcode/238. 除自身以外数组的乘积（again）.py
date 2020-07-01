class Solution:
    def productExceptSelf(self, nums: list) -> list:
        l = len(nums)
        dp1 = [0] * l
        dp2 = [0] * l
        ret = []
        dp1[0] = 1
        for i in range(1, l):
            dp1[i] = dp1[i - 1] * nums[i - 1]
        dp2[-1] = 1
        for i in range(l - 2, -1, -1):
            dp2[i] = dp2[i + 1] * nums[i + 1]
        for i, j in zip(dp1, dp2):
            ret.append(i * j)
        return ret


print(Solution().productExceptSelf([1, 2, 3, 4]))
