class Solution:
    def fun(self):
        la, lb = map(int, input().split())
        sa = input()
        sb = input()
        dp = [[0 for _ in range(lb + 1)] for _ in range(la + 1)]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if sa[i - 1] == sb[j - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        return dp[-1][-1]
print(Solution().fun())
