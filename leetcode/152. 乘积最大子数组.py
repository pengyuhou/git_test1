class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = nums[0]
        pre_max = nums[0]
        pre_min = nums[0]

        for i in range(1, len(nums)):
            cur_max = max(nums[i] * pre_max, nums[i] * pre_min, nums[i])
            cur_min = min(nums[i] * pre_max, nums[i] * pre_min, nums[i])
            ret = max(ret, cur_max)
            pre_min = cur_min
            pre_max = cur_max
        return ret


if __name__ == "__main__":
    nums = [-4, -3, -2]
    print(Solution().maxProduct(nums))
