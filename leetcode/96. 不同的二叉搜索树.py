class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        # :G(n) = G(0)*G(n-1)+G(1)*(n-2)+...+G(n-1)*G(0)
        for i in range(2,n+1):
            for j in range(1,n):
                dp[i] += dp[j-1]*dp[i-j]
        return dp[-1]



if __name__ == "__main__":
    print(Solution().numTrees(4))















