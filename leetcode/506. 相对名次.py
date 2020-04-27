class Solution(object):
    def findRelativeRanks(self, nums):
        x = sorted(nums, reverse=True)
        a = range(1, len(nums) + 1)
        res = {}
        for i, j in zip(a, x):
            res[j] = i

        for i in range(len(nums)):
            nums[i] = res[nums[i]]

        for i in range(len(nums)):
            if nums[i] == 1:
                nums[i] = "Gold Medal"
            if nums[i] == 2:
                nums[i] = "Silver Medal"
            if nums[i] == 3:
                nums[i] = "Bronze Medal"
            else:
                nums[i] = str(nums[i])
        return nums


if  __name__ == "__main__":
    nums = [5, 4, 3, 2, 1]
    print(Solution().findRelativeRanks(nums))






















