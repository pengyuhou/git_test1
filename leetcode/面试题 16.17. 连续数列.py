class Solution(object):
    def maxSubArray(self, nums):
        if nums==[]:
            return -1
        l = len(nums)
        tmp = nums[0]
        max_val = nums[0]
        for i in range(1,l):
            if nums[i] + tmp < nums[i]:
                tmp = nums[i]
                if max_val < tmp:
                    max_val = tmp
                continue
            tmp += nums[i]
            if max_val < tmp:
                max_val = tmp
        return max_val




if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    nums = [-2,1]
    print(Solution().maxSubArray(nums))


