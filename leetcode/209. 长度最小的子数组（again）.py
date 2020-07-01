class Solution(object):
    def minSubArrayLen(self, s, nums):
        left = 0
        right = 0
        ret = float('inf') 
        l = len(nums)
        while left <=right and right < l:
            if sum(nums[left:right + 1]) < s:
                right += 1
            else:
                ret = min(ret, right + 1 - left)
                left += 1
        return ret if ret != float('inf') else 0


print(Solution().minSubArrayLen(s=7, nums=[2, 3, 1, 2, 4, 3]))
