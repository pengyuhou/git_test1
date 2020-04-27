class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        indexs = [1 for _ in range(primes)]
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        for i in range(1, len(dp)):

            for j in range(len(indexs)):
                if indexs[j] * primes[j]







if __name__ == "__main__":
    print(Solution().nthSuperUglyNumber(12, [2, 7, 13, 19]))
