class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for coin in coins:
            for i in range(min(coins),amount+1):
                if i-coin>=0:
                    dp[i] = min(dp[i-coin]+1,dp[i])
        return dp[-1] if dp[-1]!=float('inf') else -1




if __name__ == "__main__":
    coins = [1,2147483647]
    amount = 2
    print(Solution().coinChange(coins,amount))


