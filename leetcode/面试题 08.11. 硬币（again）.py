class Solution:
    def __init__(self):
        self.count = 0

    def waysToChange(self, n: int) -> int:
        coins = [1, 5, 10, 25]
        def dfs(p, res):
            if sum(res) >= n:
                if sum(res) == n:
                    self.count += 1
                return
            for coin in coins:
                if not res:
                    res.append(coin)
                    dfs(p, res)
                    res.pop()
                elif coin >= res[-1]:
                    res.append(coin)
                    dfs(p, res)
                    res.pop()
        dfs(coins, [])
        return self.count

if __name__ == "__main__":
    print(Solution().waysToChange(10))









