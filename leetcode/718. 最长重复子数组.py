class Solution(object):
    def findLength(self, a, b):
        dp = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
        ret = -float('inf')
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if a[j - 1] == b[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ret = max(ret, dp[i][j])
        return ret if ret != -float('inf') else 0


print(Solution().findLength([1, 0, 0, 0, 0], [0, 0, 0, 0, 1]
                            ))
