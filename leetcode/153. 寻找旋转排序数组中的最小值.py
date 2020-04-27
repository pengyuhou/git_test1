class Solution1(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                return nums[i]
        return nums[0]


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while right - left > 1:
            mid = (right + left) // 2

            if nums[left] > nums[right]:
                if nums[left]>nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[right]>nums[mid]:
                    right = mid
                else:
                    left = mid

        return min(nums[right], nums[left])


if __name__ == "__main__":
    nums = [3, 4, 5, 1, 2]
    print(Solution().findMin([3, 4, 5, 1, 2]))
