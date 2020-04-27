class Solution(object):
    def coinChange(self, coins, amount):
        ret = [float('inf')]*(amount+1)
        ret[0] = 0
        for coin in coins:
            for x in range(coin,amount+1):
                ret[x] = min(ret[x-coin]+1,ret[x])
        return ret[-1] if ret[-1]!=float('inf') else -1

if __name__ == "__main__":
    coins = [1,2,5]
    amount = 11
    coins = [2]
    amount = 3
    coins = [186,419,83,408]
    amount = 6249
    print(Solution().coinChange(coins,amount))



