class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp2, dp3, dp5 = 0, 0, 0
        res = [0 for _ in range(n)]
        res[0] = 1
        index = 1
        while index < n:
            res[index] = min(res[dp2] * 2, res[dp3] * 3, res[dp5] * 5)
            if not res[index] % 2:
                dp2 += 1
            if not res[index] % 3:
                dp3 += 1
            if not res[index] % 5:
                dp5 += 1
            index += 1
        return res[-1]


if __name__ == "__main__":
    print(Solution().nthUglyNumber(10))
