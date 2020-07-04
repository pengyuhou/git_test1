class Solution:
    def fun(self):
        nums, v = list(map(int, input().split()))
        res = []
        for i in range(nums):
            res.append(list(map(int, input().split())))
        dp = [[0 for _ in range(v + 1)] for _ in range(nums + 1)]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if j - res[i - 1][0] >= 0:
                    dp[i][j] = max(dp[i-1][j], dp[i - 1][j - res[i - 1][0]] + res[i - 1][1])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
print(Solution().fun())