class Solution(object):
    def maxProfit(self, prices):
        if prices==[]:
            return 0
        l = len(prices)
        dp = [[None]*2]*l
        for i in range(0,l,1):
            if i-1==-1:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
            dp[i][0]=max((dp[i-1][0],dp[i-1][1]+prices[i]))
            dp[i][1]=max((dp[i-1][1],-prices[i]))
        return dp[l-1][0]

"""
int n = prices.length;
int[][] dp = new int[n][2];
for (int i = 0; i < n; i++) {
    dp[i][0] = Math.max(dp[i-1][0], dp[i-1][1] + prices[i]);
    dp[i][1] = Math.max(dp[i-1][1], -prices[i]);
}



"""


if __name__ == "__main__":
    nums = [7, 1, 5, 3, 6, 4]
    # nums = [7,6,4,3,1]
    print(Solution().maxProfit(nums))



