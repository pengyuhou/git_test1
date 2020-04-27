class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        index1 = 1
        index2 = 1
        index3 = 1
        dp = [0 for _ in range(n + 1)]
        dp[0] = 0
        for i in range(1, len(dp)):
            dp[i] = min(a * index1, b * index2, c * index3)
            if not dp[i] % a:
                index1 += 1
            if not dp[i] % b:
                index2 += 1
            if not dp[i] % c:
                index3 += 1
        return dp[-1]


if __name__ == "__main__":
    print(Solution().nthUglyNumber(5,2,11,13))
