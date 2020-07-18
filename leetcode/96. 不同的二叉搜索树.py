class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        # :G(n) = G(0)*G(n-1)+G(1)*(n-2)+...+G(n-1)*G(0)
        for i in range(2, n + 1):
            for j in range(1, n):
                dp[i] += dp[j - 1] * dp[i - j]
        print(dp)
        return dp[-1]


# G(n) = G(0)*G(n-1)+G(1)*(n-2)+...+G(n-1)*G(0)

class Solution1:
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(dp)):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[-1]


if __name__ == "__main__":
    print(Solution().numTrees(2))
    print(Solution1().numTrees(4))
