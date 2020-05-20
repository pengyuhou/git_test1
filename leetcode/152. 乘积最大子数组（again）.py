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
            cur_max = max(pre_max * nums[i], pre_min * nums[i], nums[i])
            cur_min = min(pre_max * nums[i], pre_min * nums[i], nums[i])
            ret = max(cur_max,cur_min,ret)
            pre_max = cur_max
            pre_min = cur_min
        return ret



if __name__ == "__main__":
    print(Solution().maxProduct([2, 3, -2, 4]))
