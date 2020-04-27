class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        for coin in coins:
            for i in range(coin, len(dp)):
                if i-coin>=0:
                    dp[i] += dp[i-coin]
        return dp[-1]


if __name__ == "__main__":
    amount = 5
    coins = [1, 2, 5]
    print(Solution().change(amount, coins))
