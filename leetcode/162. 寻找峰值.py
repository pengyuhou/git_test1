class Solution1(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.insert(0, -float('inf'))
        nums.append(-float('inf'))
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i - 1


class Solution:
    def findPeakElement(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid + 1] > nums[mid]:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == "__main__":
    # print(Solution1().findPeakElement([3, 2, 1]))
    print(Solution().findPeakElement([1,2,3,4]))
