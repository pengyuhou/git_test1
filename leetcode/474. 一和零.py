class Solution(object):
    def findMaxForm(self, strs, m, n):
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        return dp[-1][-1]

if __name__ == "__main__":
    print(Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))
