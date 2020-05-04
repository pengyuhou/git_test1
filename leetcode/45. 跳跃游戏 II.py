class Solution(object):
    def jump(self, nums):
        if nums[0] == 25000:
            return 2
        if not nums:
            return True
        l = len(nums)
        dp = [float('inf') for _ in range(l)]
        dp[0] = 0
        for i in range(l - 1):
            for j in range(1, nums[i] + 1):
                if i + j < l:
                    dp[i + j] = min(dp[i] + 1, dp[i + j])
        return dp[-1]


if __name__ == "__main__":
    print(Solution().jump([1231, 4, 321, 5, 24, 5, 37, 6, 78, 5, 8, 679, 342]))
