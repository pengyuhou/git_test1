class Solution(object):
    def findDuplicate(self, nums):
        left, right = 0, len(nums) - 1
        l = len(nums)
        while right - left > 1:
            mid = (left + right) // 2
            count = 0
            for i in range(l):
                if nums[i] <= mid:
                    count += 1
            if count > mid:
                right = mid
            else:
                left = mid + 1
        return left

if __name__ == "__main__":
    nums = [3, 1, 3, 4, 2]
    print(Solution().findDuplicate(nums))
