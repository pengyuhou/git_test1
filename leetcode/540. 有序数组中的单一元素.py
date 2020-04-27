class Solution(object):
    def singleNonDuplicate(self, nums):
        left = 0
        right = len(nums) - 1
        while right > left:
            mid = (left + right) // 2
            if nums[mid-1]==nums[mid]:
                l1 = len(nums[left:mid-1])
                if l1 % 2:
                    right = mid - 2
                else:
                    left = mid + 1
            if nums[mid+1]==nums[mid]:
                l1 = len(nums[left:mid])
                if l1%2:
                    right = mid-1
                else:
                    left = mid + 2
            if nums[mid+1]!=nums[mid] and nums[mid]!=nums[mid-1]:
                return nums[mid]
        return nums[left]


if __name__ == "__main__":
    print(Solution().singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
