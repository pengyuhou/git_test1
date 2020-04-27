class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf') for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 1

        l = len(dp)
        for i in range(l):
            for j in range(int(i**0.5)+1):
                if i-j*j>=0:
                    dp[i] = min(dp[i],dp[i-j*j]+1)
        return dp[-1]


if __name__ == "__main__":
    print(Solution().numSquares(2194))












