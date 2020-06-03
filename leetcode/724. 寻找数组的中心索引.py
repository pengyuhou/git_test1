class Solution:
    def pivotIndex(self, nums: list) -> int:
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i + 1:]):
                return i
        return -1


print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))
