class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        dp = [[None, None] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, len(dp)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            if i - 2 >= 0:
                dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
            if i == 1:
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[-1][0]


if __name__ == "__main__":
    print(Solution().maxProfit([2, 1, 4]))
