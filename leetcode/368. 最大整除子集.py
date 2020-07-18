class Solution(object):
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []
        nums.sort()
        dp = [[i] for i in nums]
        for j in range(1, len(nums)):
            for i in range(j - 1, -1, -1):
                # dp[i][j] = dp[i][j - 1][:]
                if not nums[j] % nums[i]:
                    dp[j] = max(dp[j], dp[i] + [nums[j]], key=len)
        return max(dp, key=len)





if __name__ == "__main__":
    print(Solution().largestDivisibleSubset([3, 6, 9, 12]))
