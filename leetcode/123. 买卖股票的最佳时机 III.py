"""
k==2


base case
dp[i][0][0] = 0
dp[i][0][1] = -infinity
dp[-1][k][0] = 0
dp[-1][k][1] = -infinity
"""
class Solution(object):
    def maxProfit(self, prices):
        if prices==[]:
            return 0
        l = len(prices)
        dp = []
        for i in range(l):
            ret = []
            for j in range(3):
                ret.append([None,None])
            dp.append(ret)
        for i in range(l):
            dp[i][0][0]=0
            dp[i][0][1]=-float('inf')
        for i in range(l):
            for j in range(1,3,1):
                if i==0:
                    dp[i][j][0]=0
                    dp[i][j][1]=-prices[i]
                    continue
                dp[i][j][0] = max((dp[i - 1][j][0], dp[i - 1][j][1] + prices[i]))
                dp[i][j][1] = max((dp[i - 1][j][1], dp[i - 1][j-1][0] - prices[i]))
        return dp[-1][2][0]

"""
int max_k = 2;
int[][][] dp = new int[n][max_k + 1][2];
for (int i = 0; i < n; i++) {
    for (int k = max_k; k >= 1; k--) {
        if (i - 1 == -1) { 
            dp[i][k][0] = 0;
            dp[i][k][1] = -prices[i];
            continue;
        }
        dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i]);
        dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i]);
    }
}
return dp[n - 1][max_k][0];




"""



if __name__ == "__main__":
    prices = [3,3,5,0,0,3,1,4]
    prices = [1,2,3,4,5]
    prices = [7,6,4,3,1]
    print(Solution().maxProfit(prices))
