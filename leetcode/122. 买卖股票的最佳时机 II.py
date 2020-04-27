# k >= 1
class Solution(object):
    def maxProfit(self, prices):
        if prices==[]:
            return 0
        l = len(prices)
        dp = [[None,None]]*l
        for i in range(l):
            if i==0:
                dp[i][0]=0
                dp[i][1]=-prices[i]
            dp[i][0] = max((dp[i-1][0],dp[i-1][1]+prices[i]))
            dp[i][1] = max((dp[i-1][1],dp[i-1][0]-prices[i]))
        return dp[-1][0]



if __name__ == "__main__":
    nums = [7,1,5,3,6,4]
    print(Solution().maxProfit(nums))
