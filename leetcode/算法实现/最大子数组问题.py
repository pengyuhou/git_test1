class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]
        l = len(nums)
        mid = l // 2
        left_max_val = self.maxSubArray(nums[:mid])
        right_max_val = self.maxSubArray(nums[mid:])

        right_sum = -float('inf')
        sum1 = 0
        for i in range(mid , l):
            sum1 += nums[i]
            if sum1 > right_sum:
                right_sum = sum1
        left_sum = -float('inf')
        sum2 = 0
        for i in range(mid-1, -1, -1):
            sum2 += nums[i]
            if sum2 > left_sum:
                left_sum = sum2
        if left_sum == -float('inf') and right_sum != -float('inf'):
            return max(left_max_val, right_max_val, right_sum)
        elif left_sum != -float('inf') and right_sum == -float('inf'):
            return max(left_max_val,right_max_val,left_sum)
        elif left_sum == -float('inf') and right_sum == -float('inf'):
            return max(left_max_val, right_max_val)
        else:
            return max(left_max_val, right_max_val,right_sum+left_sum)


if __name__ == "__main__":
    nums = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    # nums =  [-2,1,-3,4,-1,2,1,-5,4]
    # nums = [1,2]
    # nums = [1,-1,2]
    print(Solution().maxSubArray(nums))
