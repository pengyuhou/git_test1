"""
硬币。给定数量不限的硬币，币值为25分、10分、5分和1分
，编写代码计算n分有几种表示法。(结果可能会很大，你需要将结果模上1000000007)
输入: n = 5
 输出：2
 解释: 有两种方式可以凑成总金额:
5=5
5=1+1+1+1+1

"""

class Solution:
    def waysToChange(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        coins = [1,5,10,25]
        for coin in coins:
            for i in range(coin,n+1):
                dp[i] = (dp[i]+dp[i-coin])%1000000007
        return dp[-1]





if __name__ == "__main__":
    print(Solution().waysToChange(5))










