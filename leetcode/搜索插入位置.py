nums = [1,3,1,6]
target = 5


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        for i in range(len(nums)):
            if nums[i] == target:
                return i

        nums.append(target)
        nums.sort()
        return nums.index(target)



s=Solution()
print(s.searchInsert(nums, target))


