class Solution(object):
    def search(self, nums, target):
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        if len(nums)==2:
            if nums[0] == target:
                return 0
            if nums[1] == target:
                return 1
        index1 = 0
        index2 = len(nums) - 1
        while index2 - index1 > 1:
            mid = (index1 + index2) // 2
            # if nums[index1] > nums[index2]:
            if nums[index1] == target or nums[index2] == target or nums[mid] == target:
                if nums[index1] == target:
                    return index1
                if nums[index2] == target:
                    return index2
                return mid
            if nums[mid] >= nums[index1]:
                if nums[index1] <= target <= nums[mid]:
                    index2 = mid
                else:
                    index1 = mid
            elif nums[index1] <= nums[mid] <= nums[index2]:
                if nums[mid] >= target:
                    index2 = mid
                else:
                    index1 = mid
            else:
                if nums[mid] <= target <= nums[index2]:
                    index1 = mid
                else:
                    index2 = mid
        return -1


if __name__ == "__main__":
    nums = [1,3]
    target = 1
    print(Solution().search(nums, target))
