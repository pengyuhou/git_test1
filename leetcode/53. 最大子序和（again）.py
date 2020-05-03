class Solution1(object):
    def maxSubArray(self, nums):
        ret = []
        val = -float('inf')
        for i in range(len(nums)):
            ret.append(nums[i])
            if nums[i] > sum(ret):
                ret = [nums[i]]
            val = max(val,sum(ret))
        return val

class Solution:
    def maxSubArray(self,nums):
        l = len(nums)
        if l == 1:
            return nums[0]
        mid = l//2
        left = self.maxSubArray(nums[:mid])
        right = self.maxSubArray(nums[mid:])

        left_val = -float('inf')
        ret = []
        for i in range(mid-1,-1,-1):
            ret.append(nums[i])
            left_val = max(left_val,sum(ret))

        right_val = -float('inf')
        ret = []
        for i in range(mid,l):
            ret.append(nums[i])
            right_val = max(right_val, sum(ret))

        return max(left,right,right_val+left_val)


if __name__ == "__main__":
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
