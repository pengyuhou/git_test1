class Solution(object):
    def search(self, nums, target):
        if not nums:
            return False
        left = 0
        right = len(nums)-1
        while right-left>1:
            mid = (left+right)//2
            if nums[mid]==target or nums[left]==target or nums[right]==target:
                return True
            if nums[mid]==nums[left]==nums[right]!=target:
                left += 1
            if nums[mid]<target<nums[right]:
                left =mid
            if nums[left]<target:
                right = mid
            if nums[right]<target:
                left = mid
            if target<nums[left] and target<nums[right]:
                left = mid

        if nums[left]==target or nums[right]==target:
            return True
        else:
            return False

if __name__ == "__main__":
    nums = [1,1,3,1]
    target = 3
    print(Solution().search(nums,target))










